# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['Latest'] = "https://github.com/gphoto/libgphoto2"
        self.description = 'Gphoto2 digital camera library'
        self.defaultTarget = '2.5.25b'

    def setDependencies(self):
        self.buildDependencies["libs/gettext"] = "default"
        self.buildDependencies["dev-utils/pkg-config"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/glibtool"] = "default"
        self.runtimeDependencies["libs/libusb-compat"] = "default"
        #gd and libexif might be needed too

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
       	#self.subinfo.options.configure.bootstrap = True
       	self.subinfo.options.useShadowBuild = False
        self.subinfo.options.configure.args += " --disable-dependency-tracking" \
        " --disable-silent-rules" \
        " --prefix=" + prefix







