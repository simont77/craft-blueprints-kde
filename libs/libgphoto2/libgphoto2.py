# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['Latest'] = "https://github.com/gphoto/libgphoto2.git"
        self.description = 'Gphoto2 digital camera library'
        self.defaultTarget = 'Latest'
        self.targetInstSrc['Latest'] = ""

    def setDependencies(self):
        self.buildDependencies["libs/gettext"] = "default"
        self.buildDependencies["dev-utils/pkg-config"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/glibtool"] = "default"
        self.runtimeDependencies["libs/libusb-compat"] = "default"
        #gd and libexif might be needed too

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        root = CraftCore.standardDirs.craftRoot()
        craftLibDir = os.path.join(root,  'lib')
        self.subinfo.options.configure.args = "-DCMAKE_INSTALL_PREFIX=" + root + " -DCMAKE_BUILD_TYPE=Debug -DCMAKE_MACOSX_RPATH=1 -DCMAKE_INSTALL_RPATH=" + craftLibDir







