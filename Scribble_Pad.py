import time
import serial
# from pynput.mouse import Controller, Button
# import cv2
import keyboard
import turtle

#Arduino serial port and BaudRate
arduino =serial.Serial('COM3',9600)

t = turtle.Turtle()
t.circle(10)
t.write("Write Something")

# mouse = Controller()
while True:
    data = arduino.readlines(3)
    string = data[0].decode("utf-8").split('\n')[0]
    # print(string)
    try:
        LDR,TL,TR,BL,BR =  map(int,string.split(','))
        time.sleep(1)

        data = arduino.readlines(3)
        string = data[0].decode("utf-8").split('\n')[0]

        LDR1, TL1, TR1, BL1, BR1 = map(int, string.split(','))
        x = int((TL+BR)/2)
        y= int((TR+BL)/2)

        x1 = int((TL1+BR1)/2)
        y1= int((TR1+BL1)/2)


        dx = int((x-x1)/2)
        dy= int((y-y1))
        angle = ((TL+TR+BL+BR)%360)
        if LDR>50:

            dy = [dy, 100][abs(dy) > 100]
            dx = [dx, 100][abs(dx) > 100]
            #
            if dx>dy:
                t.forward(dx)
            else:
                t.dot()

                t.left(angle)
                t.forward(dy)
            print(t.pos())
            # t.penup()
            t.goto(dx, dy)
            # t.pendown()

            if abs(t.pos()[0])>150 :
                t.goto(100, 0)
            if abs(t.pos()[1])>150:
                t.goto(0,100)
        else:
            # t.penup()
            t.circle(10)
            t.write("Write Something")
            # t.reset()

    except:
        pass

    if keyboard.is_pressed('Esc'):
        break

    time.sleep(0)


# 1366x768
