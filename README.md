# PiBlinds
Raspberry Pi powered IoT Blinds
<br>
## Hardware Setup<br>
A generic 360 degree continuous servo was used with an Adafruit PWM Board (https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython)<br><br>
The sprocket was a 120% scale print of https://www.thingiverse.com/thing:70179 
<br>
## Software Setup<br>
Install dependences:<br>
`sudo pip3 install adafruit-circuitpython-pca9685`<br>
`sudo pip3 install flask`
<br><br>
Run `python3 server.py` and go to the ip address of the Raspberry Pi (Flask should be bound to all interfaces available).
<br>
To control the system from outside the network, you can tunnel the Pi to a remote server via a VPN and remote proxy the webapp. Alternatively, you could port forward.
<br><br>
Created by Henry Tu, August 2019
