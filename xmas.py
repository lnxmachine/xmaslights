# xmas.py

import sys
import os
import json
import RPi.GPIO as GPIO
import time

def main():

	# setup
	GPIO.setmode(GPIO.BCM)
	pin_list = [2, 3, 4, 17, 27, 22, 10, 9]
	for i in pinList: 
		GPIO.setup(i, GPIO.OUT) 
		GPIO.output(i, GPIO.LOW)
	
	keys = []
	# read JSON file
	with open('patterns.json') as data_file:    
		data = json.load(data_file)
		# get keys in JSON file
		for key in data:
			keys.append(key)

	# iterate over each set of patterns
	for key in keys:
		# iterate over each pattern state
		for state in data[key]:
			# modify pins
			for pin in pin_ist:
				if state[1] == 0:
					GPIO.output(pin_list[0], GPIO.LOW)
				else:
					GPIO.output(pin_list[0], GPIO.HIGH)

				if state[2] == 0:
					GPIO.output(pin_list[1], GPIO.LOW)
				else:
					GPIO.output(pin_list[1], GPIO.HIGH)

				if state[3] == 0:
					GPIO.output(pin_list[2], GPIO.LOW)
				else:
					GPIO.output(pin_list[2], GPIO.HIGH)

				if state[4] == 0:
					GPIO.output(pin_list[3], GPIO.LOW)
				else:
					GPIO.output(pin_list[3], GPIO.HIGH)

				if state[5] == 0:
					GPIO.output(pin_list[4], GPIO.LOW)
				else:
					GPIO.output(pin_list[4], GPIO.HIGH)

				if state[6] == 0:
					GPIO.output(pin_list[5], GPIO.LOW)
				else:
					GPIO.output(pin_list[5], GPIO.HIGH)

				if state[7] == 0:
					GPIO.output(pin_list[6], GPIO.LOW)
				else:
					GPIO.output(pin_list[6], GPIO.HIGH)

				if state[8] == 0:
					GPIO.output(pin_list[7], GPIO.LOW)
				else:
					GPIO.output(pin_list[7], GPIO.HIGH)

			# sleep for the specified time
			time.sleep(state[0])

main()
