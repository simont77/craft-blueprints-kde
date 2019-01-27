import glob
from xml.etree import ElementTree as et

import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['1.7.3'] = "https://github.com/indilib/indi.git||v1.7.3"
        self.description = 'INDI Library 3rd Party'
        self.defaultTarget = '1.7.3'
        self.targetInstSrc['1.7.3'] = "3rdParty"
    
    def setDependencies(self):
        self.buildDependencies["dev-utils/grep"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/libnova"] = "default"
        self.runtimeDependencies["libs/cfitsio"] = "default"
        
        self.runtimeDependencies["libs/libftdi"] = "default"
        self.runtimeDependencies["libs/libdc1394"] = "default"
        self.runtimeDependencies["libs/fftw"] = "default"
        
        self.runtimeDependencies["libs/indiserver"] = "default"
        self.runtimeDependencies["libs/libapogee"] = "default"
        #self.runtimeDependencies["libs/libdpsau"] = "default"
        self.runtimeDependencies["libs/libfishcamp"] = "default"
        self.runtimeDependencies["libs/libfli"] = "default"
        self.runtimeDependencies["libs/libqhy"] = "default"
        self.runtimeDependencies["libs/libqsi"] = "default"
        self.runtimeDependencies["libs/libsbig"] = "default"



from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        root = CraftCore.standardDirs.craftRoot()
        craftLibDir = os.path.join(root,  'lib')
        self.subinfo.options.configure.args = "-DCMAKE_INSTALL_PREFIX=" + root + " -DCMAKE_BUILD_TYPE=Debug -DCMAKE_MACOSX_RPATH=1 -DCMAKE_INSTALL_RPATH=" + craftLibDir
