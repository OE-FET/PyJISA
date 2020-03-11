# PyJISA
Python package for easily setting-up JISA for use in a python environment using JPype.

To install:

```
pip install git+https://github.com/OE-FET/PyJISA.git
```

Then in Python, simply import `pyjisa` and call `pyjisa.load()`:

```python
import pyjisa
pyjisa.load()
```

to start being able to import and use JISA classes:

```python
import pyjisa
pyjisa.load()

from jisa.devices import K2600B
from jisa.addresses import GPIBAddress

smu = K2600B(GPIBAddress(24))

channelA = smu.getChannel(0)
channelB = smu.getChannel(1)

channelA.setVoltage(5.0)
channelB.setCurrent(500e-3)

channelA.turnOn()
channelB.turnOn()

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
