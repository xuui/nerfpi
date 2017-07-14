#!/usr/bin/python
#coding=utf-8
#author:xuhel

import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image

GPIO.setmode(GPIO.BCM)
 
#define GPIO pin
pin_btn=21
GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

RST = 5
DC = 3
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

logo=Image.open('logo.png').resize((disp.width, disp.height),Image.ANTIALIAS).convert('1')
disp.image(logo)
disp.display()

sight_mod=0
def oledshow(img):
  image=Image.open('Resources/'+img).resize((disp.width, disp.height),Image.ANTIALIAS).convert('1')
  disp.image(image)
  disp.display()

def cleanup():
    print('clean up')
    GPIO.cleanup()
 
def handleSIGTERM(signum, frame):
    cleanup()
	
def onPress(channel):
    global sight_mod
    print('pressed')
    sight_mod+=1
    if sight_mod >6:
        sight_mod=1
    if sight_mod==1:
        #print('sight mode:01')
        oledshow('nerf01.png')
    elif sight_mod==2:
        #print('sight mode:02')
        oledshow('nerf02.png')
    elif sight_mod==3:
        #print('sight mode:03')
        oledshow('nerf03.png')
    elif sight_mod==4:
        #print('sight mode:04')
        oledshow('nerf04.png')
    elif sight_mod==5:
        #print('sight mode:05')
        oledshow('nerf05.png')
    elif sight_mod==6:
        #print('sight mode:06')
        oledshow('nerf06.png')

GPIO.add_event_detect(pin_btn, GPIO.FALLING, callback=onPress, bouncetime=500)
 
try:
    while True:
        if sight_mod==1:
            #print "Mode:[1]"
                
        if sight_mod==2:
            #print "Mode:[2]"
        
        if sight_mod==3:
            #print "Mode:[3]"
        
        if sight_mod==4:
            #print "Mode:[4]"
        
        if sight_mod==5:
            #print "Mode:[5]"
        
        if sight_mod==6:
            #print "Mode:[6]"

        time.sleep(1)

except KeyboardInterrupt:
    print('User press Ctrl+c ,exit;')
finally:
    cleanup()
