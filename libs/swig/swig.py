# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['3.0.12']:
            self.targets[ver] = 'https://downloads.sourceforge.net/project/swig/swig/swig-' + ver + '/swig-' + ver + '.tar.gz'
            self.archiveNames[ver] = "swig-%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'swig-' + ver
        self.description = 'Generate scripting interfaces to C/C++ code'
        self.defaultTarget = '3.0.12'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/pcreTest"] = "default"

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        self.subinfo.options.configure.autoreconf = False
        self.subinfo.options.configure.args += "--disable-dependency-tracking"
        self.subinfo.options.configure.args += " --prefix=" + prefix







