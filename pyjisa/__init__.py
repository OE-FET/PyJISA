# Import JPype
import os
import jpype
import jpype.imports
import urllib.request
import atexit
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))

def load(jvmPath=None):

    if not jpype.isJVMStarted():

        javaPath = findJava(jvmPath)

        if (javaPath is None) or (not os.path.exists(javaPath)):
            installJVM()
            javaPath = findJava()

        # Start the JVM
        jpype.startJVM(jvmpath=javaPath, convertStrings=True)

        atexit.register(shutdown)
        

def findJava(jvmPath = None):
    
    if jvmPath is None and os.path.exists(os.path.join(path, "JVM")):
        jvmPath = os.path.join(path, "JVM")

    complete = ""

    if jvmPath is None:
        complete = jpype.getDefaultJVMPath()
        
    else:
        
        linux = os.path.join(jvmPath, "lib", "server", "libjvm.so")
        win   = os.path.join(jvmPath, "bin", "server", "jvm.dll")
        mac   = os.path.join(jvmPath, "lib", "server", "libjvm.dylib")

        if os.path.exists(linux):
            complete = linux
        elif os.path.exists(win):
            complete = win
        elif os.path.exists(mac):
            complete = mac
            
            
    return complete if complete != "" else None


def shutdown():
    
    if jpype.isJVMStarted():
        
        from jisa.gui import GUI
        
        GUI.stopGUI()
        jpype.shutdownJVM()


def updateJISA():
    
    print("Downloading latest JISA.jar library...", end=" ", flush=True)
    urllib.request.urlretrieve("https://github.com/OE-FET/JISA/raw/master/JISA.jar", os.path.join(path, "JISA.jar"))
    print("Done.")


def installJVM():
    
    import jdk
    
    print("No Java runtime found on system, downloading JRE 11...", end=" ", flush=True)
    installed = jdk.install(version="11", jre=True, path=path)
    os.rename(installed, os.path.join(path, "JVM"))
    print("Done.")


if not os.path.exists(os.path.join(path, "JISA.jar")):
    updateJISA()


# Link in JISA.jar classes
jpype.addClassPath(os.path.join(path, "JISA.jar"))
jpype.imports.registerDomain("jisa")