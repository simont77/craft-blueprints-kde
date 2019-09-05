import info
import os

class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = 'a desktop planetarium'
        self.displayName = "KStars Desktop Planetarium"
        
        self.svnTargets['Latest'] = "https://github.com/KDE/kstars.git"
        
        for ver in ['3.1.1']:
            self.targets[ver] = 'http://download.kde.org/stable/kstars/kstars-%s.tar.xz' % ver
            self.targetInstSrc[ver] = 'kstars-%s' % ver
            
        self.defaultTarget = '3.1.1'

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/qt5/qtdatavis3d"] = None
        self.runtimeDependencies["libs/qt5/qtwebsockets"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kdoctools"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kwidgetsaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knewstuff"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kdbusaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kinit"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kjobwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kplotting"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifications"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifyconfig"] = None
        self.runtimeDependencies["libs/eigen3"] = None
        self.runtimeDependencies["libs/cfitsio"] = None
        self.runtimeDependencies["libs/wcslib"] = None
        self.runtimeDependencies["libs/libraw"] = None
        self.runtimeDependencies["libs/gsl"] = None
        self.runtimeDependencies["qt-libs/qtkeychain"] = None
        
        self.runtimeDependencies["libs/libgphoto2"] = "default"
        self.runtimeDependencies["libs/astrometry.net"] = "default"
        self.runtimeDependencies["libs/astrometry.netForKStars"] = "default"
        self.runtimeDependencies["libs/netpbm"] = "default"
        self.runtimeDependencies["libs/netpbmForKStars"] = "default"
        self.runtimeDependencies["libs/xplanet"] = "default"
        self.runtimeDependencies["libs/dbus-kstars"] = "default"
        self.runtimeDependencies["libs/gsc"] = "default"
        #Making these dependencies doesn't seem to download the latest versions, it downloads the default.
        #self.runtimeDependencies["libs/indiserver"] = "Latest"
        #self.runtimeDependencies["libs/indiserver3rdParty"] = "Latest"

        # Install proper theme
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
        
        if not CraftCore.compiler.isMacOS:
            self.runtimeDependencies["qt-libs/phonon-vlc"] = None


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
        imageDir = self.imageDir()
        craftRoot = CraftCore.standardDirs.craftRoot()
        KSTARS_APP = os.path.join(buildDir , 'kstars' , 'KStars.app')
        KSTARS_RESOURCES = os.path.join(KSTARS_APP , 'Contents' , 'Resources')
        KSTARS_PLUGINS = os.path.join(KSTARS_APP , 'Contents' , 'PlugIns')
        KStarsMacFiles = os.path.join(packageDir , 'KStarsMacFiles')
        
        #	The Data Directory
        utils.system("cp -rf " + imageDir + "/share/kstars " + KSTARS_RESOURCES)
        #Note that the folder in the old script was called data, so that is what KStars is looking for.
        utils.system("mv " + KSTARS_RESOURCES + "/kstars " + KSTARS_RESOURCES + "/data ")
        
        #	The Translations Directory
        utils.system("cp -rf " + craftRoot + "/share/locale " + KSTARS_RESOURCES)
				
        #	INDI Drivers
        utils.system("mkdir -p " + KSTARS_APP + "/Contents/MacOS/indi")
        utils.system("cp -f " + craftRoot + "/bin/indi* " + KSTARS_APP + "/Contents/MacOS/indi/")
        
        #	INDI firmware files"
        utils.system("mkdir -p " + KSTARS_RESOURCES + "/DriverSupport/")
        utils.system("cp -rf " + craftRoot + "/usr/local/lib/indi/DriverSupport " + KSTARS_RESOURCES)
        
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
        
        utils.system("cp -f  " + KStarsMacFiles + "/astrometry.cfg " + astrometryDestDir + "/bin/")
        
        #	Netpbm for astrometry
        netpbmBinDir =  os.path.join(craftRoot , 'netpbm', 'bin')
        netpbmDestDir = "" + KSTARS_APP + "/Contents/MacOS/netpbm"
        utils.system("mkdir -p " + netpbmDestDir)
        utils.system("cp -Rf " + netpbmBinDir + " " + netpbmDestDir)

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
        GPHOTO_VERSION = $(craft --print-installed | grep 'libs/libgphoto2' | cut -f 2 -d :)
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
        utils.system("tar -xzf " + KStarsMacFiles + "/FrameworksForVLC.zip -C " + KSTARS_APP + "/Contents/")
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
        
        # qt.conf
        confContents = "[Paths]\n"
        confContents += "Prefix = " + craftRoot + "\n"
        confContents += "Plugins = plugins\n"
        confContents += "Imports = qml\n"
        confContents += "Qml2Imports = qml\n"
        
        utils.system("touch " + KSTARS_RESOURCES + "/qt.conf")
        utils.system("echo \"" + confContents + "\" >> " + KSTARS_RESOURCES + "/qt.conf")
        
        #	Editing the info.plist file
        pListFile = KSTARS_APP + "/Contents/info.plist"

        utils.system("plutil -insert NSPrincipalClass -string NSApplication " + pListFile)
        utils.system("plutil -insert NSHighResolutionCapable -string True " + pListFile)
        utils.system("plutil -insert NSRequiresAquaSystemAppearance -string NO " + pListFile)
        utils.system("plutil -replace CFBundleName -string KStars " + pListFile)
        utils.system("plutil -replace CFBundleVersion -string ${KSTARS_VERSION} " + pListFile)
        utils.system("plutil -replace CFBundleLongVersionString -string ${KSTARS_VERSION} " + pListFile)
        utils.system("plutil -replace CFBundleShortVersionString -string ${KSTARS_VERSION} " + pListFile)
        utils.system("plutil -replace NSHumanReadableCopyright -string \"© 2001 - 2018, The KStars Team, Freely Released under GNU GPL V2\" "  + pListFile)

        return True
