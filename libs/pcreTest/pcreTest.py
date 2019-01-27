# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['8.42']:
            self.targets[ver] = 'https://ftp.pcre.org/pub/pcre/pcre-%s.tar.bz2' % ver
            self.archiveNames[ver] = "pcreTest-%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'pcre-' + ver
        self.description = 'Perl compatible regular expressions library'
        self.defaultTarget = '8.42'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["libs/libbzip2"] = "default"
        self.runtimeDependencies["libs/zlib"] = "default"
       # self.runtimeDependencies["libs/glibtool"] = "default"

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__( self )
        prefix = self.shell.toNativePath(CraftCore.standardDirs.craftRoot())
        #self.subinfo.options.configure.bootstrap = True
        self.subinfo.options.useShadowBuild = False
        self.subinfo.options.configure.args += " --disable-dependency-tracking" \
        " --prefix=#{prefix}" \
        " --enable-utf8" \
        " --enable-pcre8" \
        " --enable-pcre16" \
        " --enable-pcre32" \
        " --enable-unicode-properties" \
        " --enable-pcregrep-libz" \
        " --enable-pcregrep-libbz2" \
        " --enable-jit"







