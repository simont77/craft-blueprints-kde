import info
import os

class subinfo(info.infoclass):
    def setTargets(self):
        self.description = 'a desktop planetarium'
        self.svnTargets['Latest'] = "https://github.com/KDE/kstars.git"
        self.targetInstSrc['Latest'] = ""
        self.displayName = "KStars Desktop Planetarium"
        self.defaultTarget = 'Latest'

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = "default"
        self.runtimeDependencies["libs/qt5/qtsvg"] = "default"
        self.runtimeDependencies["libs/qt5/qtdatavis3d"] = "default"
        self.runtimeDependencies["libs/qt5/qtwebsockets"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kdoctools"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kwidgetsaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/knewstuff"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kdbusaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kinit"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kjobwidgets"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kplotting"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/knotifications"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/knotifyconfig"] = "default"
        self.runtimeDependencies["libs/eigen3"] = "default"
        self.runtimeDependencies["libs/cfitsio"] = "default"
        self.runtimeDependencies["libs/wcslib"] = "default"
        self.runtimeDependencies["libs/indiclient"] = "default"
        self.runtimeDependencies["libs/libraw"] = "default"
        self.runtimeDependencies["libs/gsl"] = "default"
        self.runtimeDependencies["qt-libs/phonon-vlc"] = "default"
        self.runtimeDependencies["qt-libs/qtkeychain"] = "default"
        
        self.runtimeDependencies["libs/libgphoto2"] = "default"
        self.runtimeDependencies["libs/astrometry.net"] = "default"
        self.runtimeDependencies["libs/astrometry.netForKStars"] = "default"
        self.runtimeDependencies["libs/netpbm"] = "default"
        self.runtimeDependencies["libs/netpbmForKStars"] = "default"
        self.runtimeDependencies["libs/xplanet"] = "default"
        self.runtimeDependencies["libs/gsc"] = "default"
        self.runtimeDependencies["libs/indiserver-latest"] = "default"
        self.runtimeDependencies["libs/indiserver3rdParty-latest"] = "default"

        # Install proper theme
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.ignoredPackages.append("binary/mysql")
        self.blacklist_file = ["blacklist.txt"]
        
    def make(self):
        if not super().make():
            return False
            
            
        #Copying things needed for MacOS KStars
        
        #	Defining Craft Directories
        buildDir = self.buildDir()
        sourceDir = self.sourceDir()
        packageDir = self.packageDir()
        craftRoot = CraftCore.standardDirs.craftRoot()
        KSTARS_APP = os.path.join(buildDir , 'kstars' , 'KStars.app')
        KSTARS_RESOURCES = os.path.join(KSTARS_APP , 'Contents' , 'Resources')
        KSTARS_PLUGINS = os.path.join(KSTARS_APP , 'Contents' , 'PlugIns')
        KStarsMacFiles = os.path.join(packageDir , 'KStarsMacFiles')
        
        #	The Data Directory
        utils.system("cp -rf " + sourceDir + "/kstars/data " + KSTARS_RESOURCES)
        
        #Translations Directory??
        
        #	INDI Drivers
        utils.system("mkdir -p " + KSTARS_APP + "/Contents/MacOS/indi")
        utils.system("cp -f " + craftRoot + "/bin/indi* " + KSTARS_APP + "/Contents/MacOS/indi/")
        
        #	INDI firmware files"
        utils.system("mkdir -p " + KSTARS_RESOURCES + "/DriverSupport/")
        utils.system("cp -rf " + craftRoot + "/lib/indi/DriverSupport " + KSTARS_RESOURCES)
        
        #	Driver XML Files
        utils.system("cp -f " + craftRoot + "/share/indi/* " + KSTARS_RESOURCES + "/DriverSupport/")
        
        #missed xml?
        
        #	Math Plugins
        utils.system("cp -rf " + craftRoot + "/lib/indi/MathPlugins " + KSTARS_RESOURCES)
        
        #	The gsc executable
        utils.system("cp -f " + craftRoot + "/bin/gsc " + KSTARS_APP + "/Contents/MacOS/indi/")
        
        #	The astrometry files.  this one is way too complex, need to be like homebrew. Finish later
        astometryBinDir = os.path.join(craftRoot , 'astrometry', 'bin')
        astometryLibDir = os.path.join(craftRoot , 'astrometry', 'lib')
        astrometryDestDir = "" + KSTARS_APP + "/Contents/MacOS/astrometry"
        
        utils.system("mkdir -p " + astrometryDestDir)
        utils.system("cp -Rf " + astometryBinDir + " " + astrometryDestDir + "/")
        utils.system("cp -Rf " + astometryLibDir + " " + astrometryDestDir + "/")
        
        utils.system("cp -f  " + craftRoot + "/etc/astrometry.cfg " + astrometryDestDir + "/bin/")
        
        #	Netpbm for astrometry
        netpbmBinDir =  os.path.join(craftRoot , 'netpbm', 'bin')
        netpbmDestDir = "" + KSTARS_APP + "/Contents/MacOS/netpbm"
        utils.system("mkdir -p " + netpbmDestDir)
        utils.system("cp -Rf " + netpbmBinDir + " " + netpbmDestDir)
        
        #Embedded python and required packages for astrometry.  Note, homebrew is required for this part.
        utils.system("mkdir -p " + KSTARS_APP + "/Contents/MacOS/python/bin")
        utils.system("cp -f /usr/local/lib/python2.7/bin/python2 ${KSTARS_APP}/Contents/MacOS/python/bin/python")
        utils.system("mkdir -p " + KSTARS_APP + "/Contents/MacOS/python/bin/site-packages")
        utils.system("cp -RLf /usr/local/lib/python2.7/site-packages/numpy " + KSTARS_APP + "/Contents/MacOS/python/bin/site-packages/")
        utils.system("cp -RLf /usr/local/lib/python2.7/site-packages/pyfits " + KSTARS_APP + "/Contents/MacOS/python/bin/site-packages/")
        
        #	xplanet
        #planet picture setup?
        xplanet_dir = KSTARS_APP + "/Contents/MacOS/xplanet"
        utils.system("mkdir -p " + xplanet_dir + "/bin")
        utils.system("mkdir -p " + xplanet_dir + "/share")
        utils.system("cp -f " + craftRoot + "/bin/xplanet " + xplanet_dir + "/bin/")
        utils.system("cp -rf " + craftRoot + "/share/xplanet " + xplanet_dir + "/share/")
        
        #	Adds some planet pictures for XPlanet
        utils.system("tar -xzf " + KStarsMacFiles + "/maps_alien-1.0.tar -C " + xplanet_dir + " --strip-components=2")
        
        #	GPhoto Plugins
        GPHOTO_VERSION = "2.5.18"
        PORT_VERSION = "0.12.0"
        utils.system("mkdir -p " + KSTARS_RESOURCES + "/DriverSupport/gphoto/IOLIBS")
        utils.system("mkdir -p " + KSTARS_RESOURCES + "/DriverSupport/gphoto/CAMLIBS")
        utils.system("cp -rf " + craftRoot + "/lib/libgphoto2_port/" + PORT_VERSION + "/* " + KSTARS_RESOURCES + "/DriverSupport/gphoto/IOLIBS/")
        utils.system("cp -rf " + craftRoot + "/lib/libgphoto2/" + GPHOTO_VERSION + "/* " + KSTARS_RESOURCES + "/DriverSupport/gphoto/CAMLIBS/")
        
        #	DBus programs and files
        utils.system("cp -f " + craftRoot + "/bin/dbus-daemon " + KSTARS_APP + "/Contents/MacOS/")
        utils.system("cp -f " + craftRoot + "/bin/dbus-send " + KSTARS_APP + "/Contents/MacOS/")
        utils.system("mkdir -p " + KSTARS_APP + "/Contents/PlugIns/dbus")
        utils.system("cp -f " + KStarsMacFiles + "/kstars.conf " + KSTARS_PLUGINS + "/dbus/kstars.conf")
        utils.system("cp -f " + KStarsMacFiles + "/org.freedesktop.dbus-kstars.plist " + KSTARS_PLUGINS + "/dbus/")
        
        #	Phonon backend and vlc plugins
        utils.system("tar -xzf " + KStarsMacFiles + "/backend.zip -C " + KSTARS_PLUGINS)
        utils.system("tar -xzf " + KStarsMacFiles + "/vlc.zip -C " + KSTARS_PLUGINS)
        
        #   Plugins
        utils.system("cp -rf " + craftRoot + "/plugins/* " + KSTARS_PLUGINS)
        
        #	Notifications
        utils.system("cp -rf " + craftRoot + "/share/knotifications5 " + KSTARS_RESOURCES)
        
        #	Sounds
        utils.system("cp -rf " + craftRoot + "/share/sounds " + KSTARS_RESOURCES)
        
        #	icons
        utils.system("mkdir " + KSTARS_RESOURCES + "/icons")
        utils.system("cp -f " + craftRoot + "/share/icons/breeze/breeze-icons.rcc " + KSTARS_RESOURCES + "/icons/")
        utils.system("cp -f " + craftRoot + "/share/icons/breeze-dark/breeze-icons-dark.rcc " + KSTARS_RESOURCES + "/icons/")

        return True

    def createPackage(self):
        self.defines["executable"] = "bin\\kstars.exe"
        #self.defines["setupname"] = "kstars-latest-win64.exe"
        self.defines["icon"] = os.path.join(self.packageDir(), "kstars.ico")

        return TypePackager.createPackage(self)
