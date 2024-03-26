# PyJISA
Python package for easily setting up JISA for use in a CPython (i.e. normal Python) environment using JPype.

To install:

```
pip install git+https://github.com/OE-FET/PyJISA.git
```

Now whenever you want to use JISA in Python, simply import `pyjisa` and call `pyjisa.load()`:

```python
import pyjisa
pyjisa.load()
```

to start being able to import and use JISA classes:

```python
import pyjisa
pyjisa.load()

from jisa.devices.smu import K2612B
from jisa.addresses import TCPIPAddress

keithley = K2612B(TCPIPAddress("192.168.0.5"))

channelA = keithley.getSMU(0)
channelB = keithley.getSMU(1)

channelA.setVoltage(5.0)
channelB.setCurrent(500e-3)

channelA.turnOn()
channelB.turnOn()

```

The first time you do this, it will download the JISA.jar file (which may take a few seconds). If you don't have one installed, it may also download a Java Runtime Environment (JRE). If you want to update the library in the future then just call `updateJISA()` like so:

```python
import pyjisa
pyjisa.updateJISA()
```

To manually select which Java installation to use, supply the path to the folder it resides in to `load()` like so:

```python
import pyjisa
pyjisa.load("/usr/lib/jvm/java-13-openjdk-amd64")
```

or

```python
import pyjisa
pyjisa.load("C:\\Program Files\\AdoptOpenJDK\\jdk-13.0.2.8-hotspot")
```

If you have GUI elements open, then you may find that you need to tell python to wait for the GUI to be stopped like so:

```python
import pyjisa; pyjisa.load();

from jisa.gui import GUI, Plot

plot = Plot("Title", "X", "Y")
plot.setExitOnClose(True)
plot.show()

# If we don't do this, python will quit and close the GUI immediately
GUI.waitForExit()
```
