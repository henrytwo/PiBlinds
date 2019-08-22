# PiBlinds
Raspberry Pi powered IoT Blinds
<br>
Demo: https://www.youtube.com/watch?v=M4cTFb5kdck
<br>
## Hardware Setup<br>
A generic 360 degree continuous servo was used with an Adafruit PWM Board (https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython)<br><br>
Two magnetic reed switches were setup at the upper and lower boundaries to prevent damanage to the blind. In the demo setup, GPIO 22 was assigned to the lower boundary and GPIO 27 was assigned to the upper. This can be modified in `main.py` to accomodate a different setup.
<br><br>
The sprocket was a 120% scale print of https://www.thingiverse.com/thing:70179 
<br>
## Software Setup<br>
Install dependences:<br>
`sudo pip3 install adafruit-circuitpython-pca9685`<br>
`sudo pip3 install flask`
<br><br>
Run `python3 main.py` and go to the ip address of the Raspberry Pi (Flask should be bound to all interfaces available).
<br>
To control the system from outside the network, you can tunnel the Pi to a remote server via a VPN and remote proxy the webapp. Alternatively, you could port forward.
<br><br>
Created by Henry Tu, August 2019
