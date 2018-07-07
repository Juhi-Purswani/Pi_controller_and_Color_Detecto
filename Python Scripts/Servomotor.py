import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def setup():
    
    global LM1
    LM1 = 17
    global LM2 
    LM2 = 27
    global RM1
    RM1 = 5
    global RM2
    RM2 = 6
    GPIO.setup(LM1,GPIO.OUT)
    GPIO.setup(LM2,GPIO.OUT)
    GPIO.setup(RM1,GPIO.OUT)
    GPIO.setup(RM2,GPIO.OUT)
    print("setup")


def ServoForward():
    GPIO.output(LM1,True)
    GPIO.output(LM2,False)
    GPIO.output(RM1,True)
    GPIO.output(RM2,False)
    print("forward")
    
def ServoBackward():
    GPIO.output(LM2,True)
    GPIO.output(LM1,False)
    GPIO.output(RM2,True)
    GPIO.output(RM1,False)
    print("backward")
    
def ServoRight():
    GPIO.output(LM1,True)
    GPIO.output(LM2,False)
    GPIO.output(RM1,False)
    GPIO.output(RM2,False)
    print("right")
    
def ServoLeft():
    GPIO.output(LM1,False)
    GPIO.output(LM2,False)
    GPIO.output(RM1,True)
    GPIO.output(RM2,False)
    print("Left")

def close():
    print("close")


if __name__ == '__main__':
    setup()
