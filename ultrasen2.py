import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED=21
TRIG=13
ECHO=19

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(TRIG, GPIO.LOW)

#GPIO.output(LED,GPIO.HIGH)
#time.sleep(0.3)
#GPIO.output(LED, GPIO.LOW)
print("Start....")
while True:
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start
	
	distance=pulse_duration * 17150
	
	distance=round(distance, 2)
	
	print "Distance:", distance, "cm"
	if(distance > 15.0):
		GPIO.output(LED, GPIO.LOW)
	elif(distance <= 15.0):
		GPIO.output(LED, GPIO.HIGH)
	
	#GPIO.cleanup()
