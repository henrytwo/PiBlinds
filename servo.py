import board
import busio
import adafruit_pca9685
from gpiozero import LED

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 50

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def ccw(i):
 kit.servo[i].angle = 180

def cw(i):
 kit.servo[i].angle = 0

def stop(i):
 kit.servo[i].angle = 90

def throttle(i, a):
 kit.servo[i].angle = 180 * (a + 1) / 2
