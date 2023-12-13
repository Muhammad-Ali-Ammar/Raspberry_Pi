"""
MuhammadAliAmmar.pythonanywhere.com
Okay Google, activate Turn On Led
Okay Google, activate Turn Off Led
"""


import RPi.GPIO  as GPIO
import requests 
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin as an output
GPIO.setup(26, GPIO.OUT)


while True : 
	
	
	Led = requests.get("https://muhammadaliammar.pythonanywhere.com/rpi")
	Led = int(Led.text)
	GPIO.output(26, Led)



