# Import JPype
import jpype
import jpype.imports

# Link in JISA.jar classes
jpype.addClassPath("./JISA.jar")
jpype.imports.registerDomain("jisa")

# Start the JVM
jpype.startJVM(convertStrings=True)
