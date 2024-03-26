# PyJISA
Python package for easily setting up JISA for use in a CPython (i.e. normal Python) environment using JPype.

To install:

```
pip install git+https://github.com/OE-FET/PyJISA.git
```

Now whenever you want to use JISA in Python, simply import `pyjisa.autoload`, like so:

```python
import pyjisa.autoload
```

The first time you do this, it will download the JISA.jar file (which may take a
few seconds). Also, if pyjisa is unable to find one installed on your system, it
may also download a Java Runtime Environment (JRE):

```python
>>> import pyjisa.autoload
Downloading latest JISA.jar library... Done.
No Java Runtime Environment found on system, downloading JRE 11... Done.
>>> _
```

After this, you're good to import `JISA` classes as if they were written in Python:

```python
import pyjisa.autoload

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

To manually select which Java installation to use, just import `pyjisa` (not `pyjisa.autoload`), and call `pyjisa.load(...)` directly, supplying the path like so:

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
import pyjisa.autoload

from jisa.gui import GUI, Plot

plot = Plot("Title", "X", "Y")
plot.setExitOnClose(True)
plot.show()

# If we don't do this, python will quit and close the GUI immediately
GUI.waitForExit()
```
