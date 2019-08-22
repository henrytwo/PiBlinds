from servo import *
import RPi.GPIO as GPIO
import time
from flask import Flask, request, Response, render_template
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

SAFETY_TIME = 10

def close():
 start_time = time.time()

 while True:
  if GPIO.input(22) or time.time() - start_time > SAFETY_TIME:
   throttle(0, 0)
   break
  else:
   throttle(0, -1)

def open():
 start_time = time.time()

 while True:
  if GPIO.input(27) or time.time() - start_time > SAFETY_TIME:
   throttle(0, 0)
   break
  else:
   throttle(0, 1)

if __name__ == '__main__':
 print('Blind server!')

 template_dir = os.path.abspath('template')
 app = Flask(__name__, template_folder=template_dir)

 @app.route('/openBlinds', methods=['POST'])
 def openBlinds():
  open()
  return 'ok'

 @app.route('/closeBlinds', methods=['POST'])
 def closeBlinds():
  close()
  return 'ok'

 @app.route('/')
 def root():
  return render_template('index.html')

 app.run(host='0.0.0.0', port='80')
