import  pywapi
import string
import RPi.GPIO as GPIO
import datetime
import locale

precip = 0

d = datetime.datetime.today()
weather_com_result = pywapi.get_weather_from_weather_com('JAXX6842:1:JA') #地域の指定

if d.hour < 16:
    precip = float(weather_com_result['forecasts'][0]['day']['chance_precip'])/100.0
else:
    precip = float(weather_com_result['forecasts'][0]['night']['chance_precip'])/100.0

REDPIN = 18
BLUEPIN = 13
GREENPIN = 19

GPIO.setmode(GPIO.BCM) #BCMでピン番号指定
GPIO.setup(REDPIN,GPIO.OUT)
GPIO.setup(BLUEPIN,GPIO.OUT)
GPIO.setup(GREENPIN,GPIO.OUT)

print precip

if precip > 0.81:
    GPIO.output(REDPIN,GPIO.LOW)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.HIGH)
elif precip > 0.55:
    GPIO.output(REDPIN,GPIO.LOW)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.LOW)
elif precip > 0.30:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.LOW)
    GPIO.output(GREENPIN,GPIO.HIGH)
elif precip > 0.20:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.LOW)
    GPIO.output(GREENPIN,GPIO.LOW)
else:
    GPIO.output(REDPIN,GPIO.HIGH)
    GPIO.output(BLUEPIN,GPIO.HIGH)
    GPIO.output(GREENPIN,GPIO.HIGH)
pass
