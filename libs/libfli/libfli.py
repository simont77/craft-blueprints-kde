import glob
from xml.etree import ElementTree as et

import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['1.7.3'] = "https://github.com/indilib/indi.git||v1.7.3"
        self.description = 'INDI Library:  FLI Camera Library'
        self.defaultTarget = '1.7.3'
        self.targetInstSrc['1.7.3'] = "3rdparty/libfli"

    def setDependencies(self):
        self.buildDependencies["dev-utils/grep"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/libnova"] = "default"
        self.runtimeDependencies["libs/cfitsio"] = "default"
        


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        root = CraftCore.standardDirs.craftRoot()
        self.subinfo.options.configure.args = "-DCMAKE_INSTALL_PREFIX=" + root + " -DCMAKE_BUILD_TYPE=Debug"
