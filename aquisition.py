
# Based on Adafruit_CircuitPython_DHT Library Example

import time
import board
import adafruit_dht
import serial
import psutil
import RPi.GPIO as GPIO
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c =busio.I2C(board.SCL, board.SDA)
ads= ADS.ADS1115(i2c)
channel = AnalogIn(ads, ADS.P0)


#Uncomment for DHT11
sensor = adafruit_dht.DHT11(board.D17)

while True:
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity
        light = channel.voltage
        print("Temp={}ºC Humidity={}% Voltage={}".format(temperature_c, humidity, light))
        

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
        

    time.sleep(3.0)
