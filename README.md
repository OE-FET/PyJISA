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

from jisa.devices import K2600B
from jisa.addresses import TCPIPAddress

smu = K2600B(TCPIPAddress("192.168.0.5"))

channelA = smu.getChannel(0)
channelB = smu.getChannel(1)

channelA.setVoltage(5.0)
channelB.setCurrent(500e-3)

channelA.turnOn()
channelB.turnOn()

```

The first time you do this, it will download the JISA.jar file (which may take a few seconds). If you want to update the library in the future then just call `updateJISA()` like so:

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
