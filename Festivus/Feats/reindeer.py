#!/usr/bin/env python
# Code for Raspberry Pi Talking / Singing Reindeer
# See http://www.penguintutor.com/electronics/reindeer


import time, pirsensor
import pygame	# use pygame for playing music
import RPi.GPIO as GPIO
import random
import os


LEDPINS = [23, 17, 22, 24, 25, 4]


# how long to wait after sequence before re-enable sensor
WAIT_SENSOR = 1
# how long to wait between checking status
WAIT_TEST = 2

# settings file holds configuration - such as "play music"
settings_file = 'reindeer.cfg'
# playnow_file if mtime updated then play file now (if in pir / off mode)
playnow_file = 'playnow.cfg'


# These values determine the sensitivity of the sensor
# PIRSAMPLE is the number of times we check for a detection 
# PIRREQ is the number of times that it must provide a Y in the sample
# Suggested values - PIRSAMPLE = 5, PIRREQ =2
# More sensitive use PIRSAMPLE = 2, PIRREQ = 1 (only needs 1 Y to trigger)
PIRSAMPLE = 5
PIRREQ = 2


# List all of the audio files 
# These can be talking, song clips or music
audiofiles = ['happychristmas.wav','happynewyear.wav','hohoho.wav','jinglebells1.wav','rudolph1.wav','wishyoumerrychristmas.wav']


def main():
	print "Reindeer sensor"

	# Connect to PIRSensor
	pir = pirsensor.PIRSensor()
	pir.connect();

	# Store the time the settings file was last modified so we can check for updates
	s_mtime = os.path.getmtime(settings_file)
	# load the settings file into a dictionary
	settings = load_settings(settings_file)
	p_mtime = os.path.getmtime(playnow_file)

	# Setup the GPIO - LED output
	GPIO.setmode(GPIO.BCM)
	for i in range(0, len(LEDPINS)) :
		GPIO.setup(LEDPINS[i], GPIO.OUT, initial=GPIO.HIGH)

	# setup music player
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.init()
	pygame.mixer.music.set_volume(1)

	clip = []

	# load audio files
	for i in range (0, len(audiofiles)) :
		clip.append(pygame.mixer.Sound(audiofiles[i]))


	while True:
	    # Check if settings have changed in which case reload
	    if (s_mtime != os.path.getmtime(settings_file)) :
	        settings = load_settings (settings_file)
	        s_mtime = os.path.getmtime(settings_file)
	    
	    ### Check settings / pir / playnow to determine if we need to play 
	    
	    # Use play_seq to determine if we are going to play
	    play_seq = False
	    
	    # Has "play now" been clicked - (mtime updated on p_mtime)
	    if (p_mtime != os.path.getmtime(playnow_file)) :
	        play_seq = True
	        # reset playnow file time
	        p_mtime = os.path.getmtime(playnow_file)
	        print "Play now pressed"
	    # Is setting play regardless?
	    elif settings['mode'] == 'on' :
	    	play_seq = True
	    	print "Play mode"
	    elif settings['mode'] == 'pir' and pir.detect(PIRSAMPLE, PIRREQ) == True :
	    	play_seq = True
		print "PIR detected"
	    
	    if play_seq == True :
		if(settings['sound']=='on') :
			# Play a random sound clip
			clip[random.randint(0, len(clip)-1)].play()

		### Flash lights 

		# Repeat flash sequence 
		for i in range (0, 3):
		
			# sets LEDS on/off 1=on, 0=off
			set_leds(1,0,0,0,0,1)
			time.sleep(0.5)
			set_leds(1,0,1,1,0,1)
			time.sleep(0.5)
			set_leds(1,1,1,1,1,1)
			time.sleep(1)
	
			set_leds(1,0,0,0,0,1)
			time.sleep(0.5)
			set_leds(1,0,1,1,0,1)
			time.sleep(0.5)
			set_leds(1,1,1,1,1,1)
	
			time.sleep(0.5)
			set_leds(1,0,0,0,0,1)
	
			time.sleep(0.5)
			set_leds(1,0,1,1,0,1)
			time.sleep(0.5)
			set_leds(1,1,0,0,1,1)

		### End of flash lights

		time.sleep(WAIT_SENSOR) # pause
	    else :
		print "Don't play"
		time.sleep(WAIT_TEST) # pause



# Set the leds on or off
# Status can be 1 / GPIO.HIGH etc. for LED on : 0 / GPIO.LOW etc. for LED off
def set_leds(led0,led1,led2,led3,led4,led5):
	GPIO.output (LEDPINS[0], led0)
	GPIO.output (LEDPINS[1], led1)
	GPIO.output (LEDPINS[2], led2)
	GPIO.output (LEDPINS[3], led3)
	GPIO.output (LEDPINS[4], led4)
	GPIO.output (LEDPINS[5], led5)
	

# Loads the settings - audio / work
def load_settings(filename) :
	print "Loading settings"
	settings_file = open(filename, 'r')
	settings = {}
	for linecount, entry in enumerate(settings_file) :
	    if (entry[0] == '#' or len(entry) < 2) :
	        continue
	    entry = entry.rstrip()
	    # split entry into key,value
	    k,v = entry.split("=")
	    # store in dictionary
	    settings[k] = v
	settings_file.close ()
	return settings



if __name__ == "__main__":
	main()
