import  RPi.GPIO as GPIO
import time
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG =4
ECHO= 18
LM1 = 17
LM2 = 27
RM1 = 5
RM2 = 6

GPIO.setup(LM1,GPIO.OUT)
GPIO.setup(LM2,GPIO.OUT)
GPIO.setup(RM1,GPIO.OUT)
GPIO.setup(RM2,GPIO.OUT)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
	step =0
	_,img = cap.read()

	if _ is True:
        	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
   	 else:
        	continue
    

    	red_lower = np.array([136,87,111],np.uint8)
   	red_upper=np.array([180,255,255],np.uint8)

    	blue_lower = np.array([99,115,150],np.uint8)
    	blue_upper=np.array([110,255,255],np.uint8)

    	yellow_lower = np.array([22,60,200],np.uint8)
    	yellow_upper=np.array([160,255,255],np.uint8)

    #finding the range of red, blue and yellow color
    	red=cv2.inRange(hsv,red_lower,red_upper)
    
    	blue=cv2.inRange(hsv,blue_lower,blue_upper)
    

    	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)

    #Morphological transformation, Dilation
    	kernal = np.ones((5,5),"uint8")

    	red=cv2.dilate(red,kernal)
    	res=cv2.bitwise_and(img,img,mask=red)

    	blue=cv2.dilate(blue,kernal)
    	res1=cv2.bitwise_and(img,img,mask=blue)

    	yellow=cv2.dilate(yellow,kernal)
    	res2=cv2.bitwise_and(img,img,mask=yellow)

    #Tracking the red color
	if step==0:
    		(_,contours,hierarchy)=cv2.findContours(red
                                            ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	else if step==1:
		(_,contours,hierarchy)=cv2.findContours(blue
                                            ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	else if step ==2:
		(_,contours,hierarchy)=cv2.findContours(yellow
                                            ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

   	for pic, contour in enumerate(contours):
        	area = cv2.contourArea(contour)
        	pt= Point(0,0) 
        	if(area>150):
            		x,y,w,h = cv2.boundingRect(contour)

            		img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            		cv2.putText(img,"Red color",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))


    #image show
    	cv2.imshow("color tracking",img)
    	if cv2.waitKey(10) & 0xFF == ord('q'):
        	cap.release()
        	cv2.destroyAllWindows()
       		break


	GPIO.output(TRIG,True)
	time.sleep(0.0001)	
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO)==False:
		start=time.time()
	while GPIO.input(ECHO)==True:
		end=time.time()
	sig_time = end-start
	distance= sig_time/0.000058
	print("x is")

       	print (x , " ,y is " , y," distance=",distance)

	if distance < 10:
		GPIO.output(LM1,False)
		GPIO.output(LM2,False)
		GPIO.output(RM2,False)
		GPIO.output(RM1,False)
		step++
		print('STOP ')
	else if x < 310:
		GPIO.output(LM1,True)
		GPIO.output(LM2,False)
		print('right')
		GPIO.output(RM2,False)
		GPIO.output(RM1,False)
	else if x >320:
		GPIO.output(LM1,False)
                GPIO.output(LM2,False)
                print('left')
                GPIO.output(RM2,False)
                GPIO.output(RM1,True)
	else if x<320&& x>310:
		GPIO.output(LM1,True)
                GPIO.output(LM2,False)
                print('straight')
                GPIO.output(RM2,False)
                GPIO.output(RM1,True)
GPIO.cleanup()
