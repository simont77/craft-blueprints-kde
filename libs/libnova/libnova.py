import info


#
# this library is used by kdeedu/kstars
# the library is c-only
#
class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['0.13.0+svn270'] = 'download.sourceforge.net/kde-windows/libnova-0.13.0+svn270.tar.bz2'
        self.targetInstSrc['0.13.0+svn270'] = 'libnova'
        self.targetDigests['0.13.0+svn270'] = '1d618a5a1f4282e531b2a3d434407bac941cd700'
        # self.patchToApply['0.13.0+svn270'] = [('libnova-20101215.diff', 1),('libnova-20130629.diff', 1)]
        self.description = "a Celestial Mechanics, Astrometry and Astrodynamics library"
        self.defaultTarget = '0.13.0+svn270'

    def setDependencies(self):
       # self.buildDependencies["libs/glibtool"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"


from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        self.subinfo.options.configure.bootstrap = True
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        self.subinfo.options.configure.cflags += "-march=core2"
        self.subinfo.options.configure.cxxflags += "-march=core2"
        self.subinfo.options.configure.args += " --prefix=" + prefix

