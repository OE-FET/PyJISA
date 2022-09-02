# Import JPype
import os
import jpype
import jpype.imports
import urllib.request
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))


def load(jvmPath=None):
    if not os.path.exists(os.path.join(path, "JISA.jar")):
        updateJISA()

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

    # Link in JISA.jar classes
    jpype.addClassPath(os.path.join(path, "JISA.jar"))
    jpype.imports.registerDomain("jisa")

    # Start the JVM
    jpype.startJVM(jvmpath=complete, convertStrings=True)


def updateJISA():
    print("Downloading latest JISA.jar library...", end=" ", flush=True)
    urllib.request.urlretrieve("https://github.com/OE-FET/JISA/raw/master/JISA.jar", os.path.join(path, "JISA.jar"))
    print("Done.")


class Runnable(JProxy):
    def __init__(self, function):
        super().__init__("java.lang.Runnable", dict={"run": function})


class Task(JProxy):
    def __init__(self, function):
        super().__init__("jisa.control.RTask.Task", dict={"run": function})


class SRunnable(JProxy):
    def __init__(self, function):
        super().__init__("java.control.SRunnable", dict={"run": function})


class Predicate(JProxy):
    def __init__(self, function):
        super().__init__("java.util.function.Predicate", dict={"test": function})


class RowEvaluable(JProxy):
    def __init__(self, function):
        super().__init__("jisa.results.RowEvaluable", dict={"evaluate": function})
