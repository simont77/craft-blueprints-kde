import glob
from xml.etree import ElementTree as et

import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = 'INDI Library'
        self.svnTargets['Latest'] = "https://github.com/indilib/indi.git"
        self.targetInstSrc['Latest'] = ""
        
        ver = '1.8.3'
        self.svnTargets[ver] = "https://github.com/indilib/indi.git||v" + ver
        self.archiveNames[ver] = 'indi-%s.tar.gz' % ver
        self.targetInstSrc[ver] = ""

        self.defaultTarget = ver

    def setDependencies(self):
        self.buildDependencies["dev-utils/grep"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/libnova"] = "default"
        self.runtimeDependencies["libs/cfitsio"] = "default"
        self.runtimeDependencies["libs/libusb"] = "default"
        self.runtimeDependencies["libs/gsl"] = "default"
        self.runtimeDependencies["libs/libjpeg-turbo"] = "default"
        self.runtimeDependencies["libs/fftw"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        root = CraftCore.standardDirs.craftRoot()
        craftLibDir = os.path.join(root,  'lib')
        self.subinfo.options.configure.args = "-DCMAKE_INSTALL_PREFIX=" + root + " -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_MACOSX_RPATH=1 -DCMAKE_INSTALL_RPATH=" + craftLibDir
