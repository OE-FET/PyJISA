# PyJISA
Python package for easily setting-up JISA for use in a python environment using JPype.

To install:

```
pip install git+https://github.com/OE-FET/PyJISA.git
```

Then in Python, simply import `pyjisa`:

```python
import pyjisa
```

to start being able to import and use JISA classes:

```python
import pyjisa
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
