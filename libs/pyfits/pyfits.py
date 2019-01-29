# -*- coding: utf-8 -*-
import info
from Package.PipPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = ''
        self.defaultTarget = 'master'
        
    def setDependencies( self ):
        self.runtimeDependencies["dev-utils/python2"] = None
        self.runtimeDependencies["libs/numpy"] = None

class Package(PipPackageBase):
    def __init__(self, **args):
        PipPackageBase.__init__(self)
        
