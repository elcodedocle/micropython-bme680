
Introduction
============

Micropython driver for BME680 sensor over I2C - Adapted from https://github.com/adafruit/Adafruit_CircuitPython_BME680

Dependencies
=============
This driver depends on:

* `Micropython <https://github.com/micropython/micropython>`_

Installing
==========
From host
```bash
wget https://raw.githubusercontent.com/elcodedocle/micropython-bme680/5aa1a520e8a406b548f06d164c76f68541ac0b5d/bme680.py
ampy --port /dev/tty<yourPort> bme680.py
```
From device
```bash
import mip
mip.install("https://raw.githubusercontent.com/elcodedocle/micropython-bme680/5aa1a520e8a406b548f06d164c76f68541ac0b5d/bme680.py")
```
(See https://docs.micropython.org/en/v1.23.0/reference/packages.html)

Usage Example
=============

See [examples/bme680_simpletest.py](examples/bme680_simpletest.py)
