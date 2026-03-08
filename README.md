
Introduction
============

Micropython driver for BME680 sensor over I2C - Adapted from https://github.com/adafruit/Adafruit_CircuitPython_BME680
and https://github.com/boschsensortec/BSEC-Arduino-library/blob/master/src/bme68x/bme68x.c

Dependencies
=============
This driver depends on:

* [Micropython](https://github.com/micropython/micropython)

Installing
==========
From host
```bash
wget https://raw.githubusercontent.com/elcodedocle/micropython-bme680/4021ea749d20d66e346667c896c35834f2dbd507/bme680.py
ampy --port /dev/tty<yourPort> bme680.py
```
From device
```bash
import mip
mip.install("https://raw.githubusercontent.com/elcodedocle/micropython-bme680/4021ea749d20d66e346667c896c35834f2dbd507/bme680.py")
```
(See https://docs.micropython.org/en/v1.23.0/reference/packages.html)

Usage Example
=============

See [examples/bme680_simpletest.py](examples/bme680_simpletest.py)
