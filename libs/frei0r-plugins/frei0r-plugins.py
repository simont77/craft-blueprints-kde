import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.description = 'Minimalistic plugin API for video effects, plugins collection'
        self.webpage = 'http://frei0r.dyne.org/'
        for ver in ['1.6.1']:
            self.targets[ ver ] = f"https://github.com/dyne/frei0r/archive/v{ver}.tar.gz"
            self.targetInstSrc[ ver ] = f"frei0r-{ver}"
        self.targetDigests['1.6.1'] = '69a2330997c95d4afc9dc025d7970b11446ea686'
        self.targetDigests['1.6.1'] = (['dae0ca623c83173788ce4fc74cb67ac7e50cf33a4412ee3d33bed284da1a8437'], CraftHash.HashAlgorithm.SHA256)

        self.svnTargets['master'] = 'https://github.com/dyne/frei0r.git'
        self.defaultTarget = '1.6.1'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        #self.runtimeDependencies["libs/opencv"] = None
        #self.runtimeDependencies["libs/cairo"] = None
        #self.runtimeDependencies["libs/gavl"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
