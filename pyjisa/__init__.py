# Import JPype
import os
import jpype
import jpype.imports
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))

def load(jvmPath=None):
    
    complete = ""
    
    if jvmPath == None:
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
    
    # Link in JISA.jar classes
    jpype.addClassPath(os.path.join(path, "JISA.jar"))
    jpype.imports.registerDomain("jisa")

    # Start the JVM
    jpype.startJVM(jvmpath=complete, convertStrings=True)
    
    
def toRunnable(function):
    from jisa.control import SRunnable
    return SRunnable.fromJProxy(JProxy("java.lang.Runnable", dict={"run": function}))


def toPredicate(function):
    return JProxy("java.util.function.Predicate", dict={"test": function})


def toEvaluable(function):
    return JProxy("jisa.experiment.ResultTable.Evaluable", dict={"evaluate": function})

