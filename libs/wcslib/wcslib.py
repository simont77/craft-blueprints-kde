import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['6.3']:
            self.targets[ver] = 'https://www.atnf.csiro.au/pub/software/wcslib/wcslib-%s.tar.bz2' % ver
            self.archiveNames[ver] = "wcslib-%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'wcslib-' + ver

        self.defaultTarget = '6.3'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None


from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        #self.subinfo.options.configure.bootstrap = True
        self.subinfo.options.useShadowBuild = False
        self.subinfo.options.configure.args += " --disable-dependency-tracking" \
        " --prefix=#{prefix}" \
        " --without-pgplot" \
        " --disable-fortran"
        
        craftLibDir = os.path.join(prefix,  'lib')
        self.subinfo.options.configure.ldflags += '-Wl,-rpath,' + craftLibDir