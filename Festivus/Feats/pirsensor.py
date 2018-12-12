import serial
import time

# PIRSensor class
# This is a crude way of detecting if a Zilog PIR sensor is triggered on the Raspberry Pi
# It has been created for the Reindeer project http://www.penguintutor.com/electronics/reindeer
# There is little in the way of handling any errors or checking
# This is suitable for basic toy type detection, but would need further development for a more robust solution


class PIRSensor:
	'''Class for reading PIR sensor'''
	
	# Commands issued to the PIR module
	STATUS_CMD = 'a'
	SENS_CMD = 's' # Not using this in the current version
	DELAY = 0.5
	
	# Time in seconds between each sample 
	
	
	def __init__(self):
		self.connect_status = 0
		
	def connect(self):
		self.serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
		# Note no checking to see if this has worked (would be a good idea for future)
		# set internal status to connected
		self.connect_status = 1
		print("Connected")
		
		
	def disconnect(self):
		''' just set status to disconnected ''' 
		self.connect_status = 0
		
	# Gets a single value for status of PIR sensor
	# returns directly Y = Yes, N = No, U = Unavaialble (eg. not yet initialised)
	def getstatus(self):
		if self.connect_status == 1 :
			self.serial.write(self.STATUS_CMD)
			data = self.serial.read()
			return data
		else :
			return 0
		
	def detect(self, pirsample, pirreq):
		''' pirsample is number of samples to take, pirreq is number of Y required to return a Y - otherwise return a N'''
		yes_count = 0
		for i in range(0, pirsample) :
			if (self.getstatus() == 'Y'): 
				yes_count +=1
			time.sleep(self.DELAY) # wait before trying again
		if (yes_count >= pirreq):
			return True 
		else :
			return False
			
			
