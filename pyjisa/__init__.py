# Import JPype
import os
import jpype
import jpype.imports
import urllib.request
import atexit
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))

def load(jvmPath=None):

    if jpype.isJVMStarted() and (os.path.join(path, "JISA.jar") not in jpype.getClassPath()):
        jpype.shutdownJVM()

    if not jpype.isJVMStarted():

        complete = ""

        if jvmPath is None:
            complete = jpype.getDefaultJVMPath()
        else:
            linux = os.path.join(jvmPath, "lib", "server", "libjvm.so")
            win = os.path.join(jvmPath, "bin", "server", "jvm.dll")
            mac = os.path.join(jvmPath, "lib", "server", "libjvm.dylib")

            if os.path.exists(linux):
                complete = linux
            elif os.path.exists(win):
                complete = win
            elif os.path.exists(mac):
                complete = mac

        # Start the JVM
        jpype.startJVM(jvmpath=complete, convertStrings=True)

        atexit.register(shutdown)


def shutdown():
    
    if jpype.isJVMStarted():
        
        from jisa.gui import GUI
        GUI.stopGUI()
        jpype.shutdownJVM()


def updateJISA():
    
    print("Downloading latest JISA.jar library...", end=" ", flush=True)
    urllib.request.urlretrieve("https://github.com/OE-FET/JISA/raw/master/JISA.jar", os.path.join(path, "JISA.jar"))
    print("Done.")



if not os.path.exists(os.path.join(path, "JISA.jar")):
    updateJISA()

# Link in JISA.jar classes
jpype.addClassPath(os.path.join(path, "JISA.jar"))
jpype.imports.registerDomain("jisa")