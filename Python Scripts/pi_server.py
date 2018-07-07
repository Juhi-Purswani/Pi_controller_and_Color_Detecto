import Servomotor
import socket 
from time import ctime
import RPi.GPIO as GPIO

Servomotor.setup()

ctrCmd = ['forward','backward','right','left']

HOST = socket.gethostname()
PORT = 1998
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print(ADDR)

while True:
    print("waiting for coonection")
    print("before accepted method")
    tcpCliSock,addr = tcpSerSock.accept()
    print("after accepted method")
    print('...connected from :',addr)
    try:
        while True:
            data = ''
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                print("breaking")
                break
            if data == ctrCmd[0]:
                Servomotor.ServoForward()
                print('forward button is clicked')
                break
            if data == "backward":
                Servomotor.ServoFBackward()
                print('backward button is clicked')
            if data == ctrCmd[2]:
                Servomotor.ServoRight()
                print('Right button is clicked')
            if data == ctrCmd[3]:
                Servomotor.ServoLeft()
                print('Left button is clicked')
    except KeyboardInterrupt:
        tcpCliSock.close
        Servomotor.close()
        GPIO.cleanup()
