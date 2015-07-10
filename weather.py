import  pywapi
import string
import RPi.GPIO as GPIO
import datetime
import locale

d = datetime.datetime.today()
day = 0
result = pywapi.get_weather_from_weather_com('JAXX6842:1:JA')

if d.hour > 16:
    day = float(result['forecasts'][0]['day']['chance_precip'])/100.0
else:
    day = float(result['forecasts'][0]['night']['chance_precip'])/100.0

REDPIN = 18
BLUEPIN = 13
GREENPIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(REDPIN,GPIO.OUT)
GPIO.setup(BLUEPIN,GPIO.OUT)
GPIO.setup(GREENPIN,GPIO.OUT)

print day

if day > 0.81:
    GPIO.output(REDPIN,GPIO.LOW)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.HIGH)
elif day > 0.55:
    GPIO.output(REDPIN,GPIO.LOW)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.LOW)
elif day > 0.30:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.LOW)
    GPIO.output(GREENPIN,GPIO.HIGH)
elif day > 0.20:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.LOW)
    GPIO.output(GREENPIN,GPIO.LOW)
else:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.HIGH)
pass
