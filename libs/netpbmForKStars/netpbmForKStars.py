#!/usr/bin/env python3
import info
import os
import sys
import fileinput


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['10.73.18'] = "svn://svn.code.sf.net/p/netpbm/code/stable"
        self.targetInstSrc['10.73.18'] = ''
        self.targetDigests['10.73.18'] = 'd2e8b4a2ccbebcd5147475bdfb7e4362c92fc1e1'
        self.description = 'Image manipulation'
        self.defaultTarget = '10.73.18'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/netpbm"] = "default"
        self.runtimeDependencies["libs/jasper"] = "default"
        self.runtimeDependencies["libs/libjpeg-turbo"] = "default"
        self.runtimeDependencies["libs/libpng"] = "default"
        self.runtimeDependencies["libs/tiff"] = "default"
        
from Package.MakeFilePackageBase import *

class Package(MakeFilePackageBase):
    def __init__(self, **args):
        MakeFilePackageBase.__init__(self)
        self.subinfo.options.useShadowBuild = True
        
    def configure(self):
        self.enterSourceDir()
        craftLibDir = os.path.join(CraftCore.standardDirs.craftRoot(), 'lib')
        craftIncludeDir = os.path.join(CraftCore.standardDirs.craftRoot(), 'include')
        builddebug = "yes" if self.buildType() == "Debug" else "no"
        utils.copyFile(os.path.join(self.sourceDir(), "config.mk.in"), os.path.join(self.sourceDir(), "config.mk"), linkOnly=False)
        f1name = os.path.join(self.sourceDir(), "config.mk.in")
        f2name = os.path.join(self.sourceDir(), "config.mk")
        f1 = open(f1name, 'r')
        f2 = open(f2name, 'w')
        filedata = f1.read()
        filedata = filedata.replace('#CFLAGS = -I/usr/local/include', 'CFLAGS += -I' + craftIncludeDir)
        filedata = filedata.replace('NETPBMLIBTYPE = unixshared', 'NETPBMLIBTYPE = dylib')
        filedata = filedata.replace('NETPBMLIBSUFFIX = so', 'NETPBMLIBSUFFIX = dylib')
        filedata = filedata.replace('LDSHLIB = -shared -Wl,-soname,$(SONAME)', '#LDSHLIB = -shared -Wl,-soname,$(SONAME)')
        
        #Not sure why these are not working, they do in homebrew
        #filedata = filedata.replace('JPEGLIB = NONE', 'JPEGLIB = -ljpeg')
        #filedata = filedata.replace('PNGLIB = NONE', 'PNGLIB = -lpng')
        #filedata = filedata.replace('ZLIB = NONE', 'ZLIB = -lz')
        #filedata = filedata.replace('TIFFLIB = NONE', 'TIFFLIB = -ltiff')
        
        #Absolute paths instead, this should not be the case!
        filedata = filedata.replace('JPEGLIB = NONE', 'JPEGLIB =' + os.path.join(craftLibDir, 'libjpeg.a'))
        filedata = filedata.replace('PNGLIB = NONE', 'PNGLIB = ' + os.path.join(craftLibDir, 'libpng.dylib'))
        filedata = filedata.replace('ZLIB = NONE', 'ZLIB = ' + os.path.join(craftLibDir, 'libz.dylib'))
        filedata = filedata.replace('TIFFLIB = NONE', 'TIFFLIB = ' + os.path.join(craftLibDir, 'libtiff.dylib'))
        
        filedata = filedata.replace('NEED_RUNTIME_PATH = N', 'NEED_RUNTIME_PATH = Y')
        
        #This is for the one in a package for KStars
        filedata = filedata.replace('NETPBMLIB_RUNTIME_PATH = ', 'NETPBMLIB_RUNTIME_PATH = ' + os.path.join(CraftCore.standardDirs.craftRoot(), 'netpbm', 'lib'))
        #This is for the one in the craft dir
        #filedata = filedata.replace('NETPBMLIB_RUNTIME_PATH = ', 'NETPBMLIB_RUNTIME_PATH = ' + craftLibDir)
        
        filedata = filedata.replace('#LDSHLIB=-dynamiclib -install_name', 'LDSHLIB=-dynamiclib -install_name')
        f2.write(filedata)
        f1.close()
        f2.close()
        return True
        
    def make(self):
        self.enterSourceDir()
        utils.system("make")
        self.cleanImage()
        # Note that it has to be in a child folder, otherwise netpbm won't build it.
        buildDir=os.path.join(self.buildDir(), 'build')
        utils.system("make package pkgdir=" + buildDir)
        return True
        
    def install(self):
        utils.system("make package pkgdir=" + self.imageDir())
        # Deleting the netpbm files which have licensing restrictions on distribution or are unknown status
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'hpcdtoppm'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pcdindex'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'ppmtogif'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pamchannel'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pamtopnm'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pbmto4425'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pbmtoln03'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pbmtolps'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pbmtopk'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'pktopbm'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'ppmtopjxl'))
        utils.deleteFile(os.path.join(self.imageDir(), 'bin', 'spottopgm'))
        
        #This is for the one in a package for KStars
        netpbmDir = os.path.join(CraftCore.standardDirs.craftRoot(), 'netpbm')
        #This is for the one in the craft dir
        #netpbmDir = CraftCore.standardDirs.craftRoot()
        
        binaryDir = os.path.join(netpbmDir, 'bin')
        includeDir = os.path.join(netpbmDir,  'include')
        libDir = os.path.join(netpbmDir,  'lib')
        
        utils.system("mkdir -p " + netpbmDir)
        
        utils.system("mkdir -p " + binaryDir)
        utils.system("mkdir -p " + libDir)
        utils.system("cp " + self.imageDir() + "/bin/* " + binaryDir)
        utils.system("cp -r " + self.imageDir() + "/include/* " + includeDir)
        utils.system("cp " + self.imageDir() + "/lib/* " + libDir)
        return True



