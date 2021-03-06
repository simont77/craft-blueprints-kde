# -*- coding: utf-8 -*-
# Copyright 2018 Łukasz Wojniłowicz <lukasz.wojnilowicz@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import info

from Package.AutoToolsPackageBase import *
from Package.PackageBase import *
from Package.VirtualPackageBase import VirtualPackageBase


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["3.5.17"]:
            self.targets[ver] = "ftp://ftp.gnutls.org/gcrypt/gnutls/v3.5/gnutls-%s.tar.xz" % ver
            self.targetInstSrc[ver] = "gnutls-%s" % ver
        self.targetDigests['3.5.17'] = (['86b142afef587c118d63f72ccf307f3321dbc40357aae528202b65d913d20919'], CraftHash.HashAlgorithm.SHA256)
        self.description = "A library which provides a secure layer over a reliable transport layer"
        self.defaultTarget = "3.5.17"

    def setDependencies(self):
        self.runtimeDependencies["libs/gcrypt"] = None
        self.runtimeDependencies["libs/nettle"] = None
        self.runtimeDependencies["libs/libidn"] = None
        self.runtimeDependencies["libs/libunistring"] = None
        self.runtimeDependencies["libs/libtasn1"] = None
        self.runtimeDependencies["libs/p11kit"] = None
        if CraftCore.compiler.isMinGW():
            self.buildDependencies["dev-utils/msys"] = None


class PackageAutoTools(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        # 2018-02-11: without --enable-openssl-compatibility xmlmerge.exe from gwenhywfar doesn't display any console output and in effect doesn't allow compilation of aqbanking
        # 2018-02-11: --enable-nls is probably needed on the same ground as above
        self.subinfo.options.configure.args = "--enable-shared --disable-static --with-zlib --enable-cxx --enable-nls --disable-gtk-doc --enable-local-libopts --enable-libopts-install --disable-tests --enable-openssl-compatibility "

if not CraftCore.compiler.isMSVC():
    class Package(PackageAutoTools):
        def __init__(self):
            PackageAutoTools.__init__(self)
else:
    class Package(VirtualPackageBase):
        def __init__(self):
            VirtualPackageBase.__init__(self)
