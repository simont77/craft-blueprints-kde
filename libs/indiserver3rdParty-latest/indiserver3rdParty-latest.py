import glob
from xml.etree import ElementTree as et

import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['Latest'] = "https://github.com/indilib/indi.git"
        self.description = 'INDI Library 3rd Party'
        self.defaultTarget = 'Latest'
        self.targetInstSrc['Latest'] = "3rdParty"
    
    def setDependencies(self):
        self.buildDependencies["dev-utils/grep"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/libnova"] = "default"
        self.runtimeDependencies["libs/cfitsio"] = "default"
        self.runtimeDependencies["libs/libgphoto2"] = "default"
        self.runtimeDependencies["libs/libftdi"] = "default"
        self.runtimeDependencies["libs/libdc1394"] = "default"
        self.runtimeDependencies["libs/libraw"] = "default"
        self.runtimeDependencies["libs/tiff"] = "default"
        self.runtimeDependencies["libs/fftw"] = "default"
        self.runtimeDependencies["libs/ffmpeg"] = "default"
        self.runtimeDependencies["libs/indiserver-latest"] = "default"
        self.runtimeDependencies["libs/libapogee-latest"] = "default"
        #self.runtimeDependencies["libs/libdspau-latest"] = "default"
        self.runtimeDependencies["libs/librtlsdr"] = "default"
        self.runtimeDependencies["libs/libfishcamp-latest"] = "default"
        self.runtimeDependencies["libs/libfli-latest"] = "default"
        self.runtimeDependencies["libs/libqhy-latest"] = "default"
        self.runtimeDependencies["libs/libqsi-latest"] = "default"
        self.runtimeDependencies["libs/libsbig-latest"] = "default"
        self.runtimeDependencies["libs/libaltair-latest"] = "default"
        self.runtimeDependencies["libs/libtoupcam-latest"] = "default"
        self.runtimeDependencies["libs/libatik-latest"] = "default"



from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        root = CraftCore.standardDirs.craftRoot()
        craftLibDir = os.path.join(root,  'lib')
        self.subinfo.options.configure.args = "-DCMAKE_INSTALL_PREFIX=" + root + " -DCMAKE_BUILD_TYPE=Debug -DCMAKE_MACOSX_RPATH=1 -DCMAKE_INSTALL_RPATH=" + craftLibDir
