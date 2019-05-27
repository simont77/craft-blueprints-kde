import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "[git]https://github.com/ampl/gsl.git"
        for ver in ["2.5"]:
            self.targets[ver] = f"https://ftp.gnu.org/gnu/gsl/gsl-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"gsl-{ver}"
            self.archiveNames[ver] = f"gsl-{ver}.tar.gz"
        self.targetDigests['2.5'] = (
            ['0460ad7c2542caaddc6729762952d345374784100223995eb14d614861f2258d'], CraftHash.HashAlgorithm.SHA256)
        self.description = 'GNU Scientific Library'
        self.defaultTarget = '2.5'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None


from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        self.subinfo.options.configure.bootstrap = True
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        self.subinfo.options.configure.args += " --prefix=" + prefix

