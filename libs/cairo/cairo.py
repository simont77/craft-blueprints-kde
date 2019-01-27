# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['1.14.12']:
            self.targets[ver] = 'https://cairographics.org/releases/cairo-%s.tar.xz' % ver
            self.archiveNames[ver] = "cairo-%s.tar.xz" % ver
            self.targetInstSrc[ver] = 'cairo-' + ver
        self.description = 'Vector graphics library with cross-device output support'
        self.defaultTarget = '1.14.12'

    def setDependencies(self):
        self.buildDependencies["dev-utils/pkg-config"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/freetype"] = "default"
        self.runtimeDependencies["libs/glib"] = "default"
        self.runtimeDependencies["libs/libpng"] = "default"
        self.runtimeDependencies["libs/pixman"] = "default"
    
from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        self.subinfo.options.configure.args += "--disable-dependency-tracking" \
        " --prefix=" + prefix + "" \
        " --enable-gobject=yes" \
        " --enable-svg=yes" \
        " --enable-tee=yes" \
        " --enable-quartz-image" \
        " --enable-xcb=no" \
        " --enable-xlib=no" \
        " --enable-xlib-xrender=no"







