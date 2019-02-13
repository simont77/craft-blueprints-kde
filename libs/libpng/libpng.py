import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['1.6.34']:
            self.targets[ver] = 'http://downloads.sourceforge.net/libpng/libpng-' + ver + '.tar.gz'
            self.targetInstSrc[ver] = 'libpng-' + ver
        
        self.description = 'A library to display png images'
        self.defaultTarget = '1.6.34'

    def setDependencies(self):
        self.runtimeDependencies["libs/zlib"] = "default"
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
        
    #	Note that this setting of the environment flags to nothing solves a build error on Sierra because the system headers have issues.
    def configure(self):
        self.shell.environment["CXXFLAGS"]=""
        self.shell.environment["CFLAGS"]=""
        AutoToolsPackageBase.configure(self)
        return True