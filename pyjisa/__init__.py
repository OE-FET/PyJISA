# Import JPype
import os
import jpype
import jpype.imports

path = os.path.dirname(os.path.realpath(__file__))

# Link in JISA.jar classes
jpype.addClassPath(os.path.join(path, "JISA.jar"))
jpype.imports.registerDomain("jisa")

# Start the JVM
jpype.startJVM(convertStrings=True)
