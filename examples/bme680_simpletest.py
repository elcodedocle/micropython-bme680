# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries; 2026 elcodedocle
# SPDX-License-Identifier: MIT

import time
import machine
import bme680

# Create sensor object, communicating over the board's default I2C bus
i2c = machine.I2C(0, scl=machine.Pin(12), sda=machine.Pin(13), freq=400000)
sensor = bme680.BME680I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
sensor.sea_level_pressure = 1013.25

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
temperature_offset = -5

while True:
    print("\nTemperature: %0.1f C" % (sensor.temperature + temperature_offset))
    print("Gas: %d ohm" % sensor.gas)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    print("Pressure: %0.3f hPa" % sensor.pressure)
    print("Altitude = %0.2f meters" % sensor.altitude)

    time.sleep(1)
