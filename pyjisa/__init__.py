# Import JPype
import os
import jpype
import jpype.imports

path = os.path.dirname(os.path.realpath(__file__))

def load(jvmPath=jpype.getDefaultJVMPath()):
    
    # Link in JISA.jar classes
    jpype.addClassPath(os.path.join(path, "JISA.jar"))
    jpype.imports.registerDomain("jisa")

    # Start the JVM
    jpype.startJVM(jvmpath=jvmPath, convertStrings=True)
