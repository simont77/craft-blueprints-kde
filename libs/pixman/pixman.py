# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['0.34.0']:
            self.targets[ver] = 'https://cairographics.org/releases/pixman-%s.tar.gz' % ver
            self.archiveNames[ver] = "pixman-%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'pixman-' + ver
        self.description = 'Low-level library for pixel manipulation'
        self.defaultTarget = '0.34.0'
        self.patchToApply['0.34.0'] = ("pixman-0.34.0-shuffle.patch", 1)

    def setDependencies(self):
        self.buildDependencies["dev-utils/pkg-config"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        self.subinfo.options.configure.args += "--disable-dependency-tracking" \
        " --disable-gtk" \
        " --disable-silent-rules" \
        " --prefix=" + prefix







