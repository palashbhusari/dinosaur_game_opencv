
# this code is for half screen  http://www.trex-game.skipser.com/ game

import numpy as np
import cv2
from mss import mss
from PIL import Image # grab screen
from pyautogui import press, keyDown,keyUp, hotkey # for keyboard
import time

########### change the distance between dino and points########
dist_x=25
##########################################
count =0

uy,ux=283,200+dist_x # PIXELS(inverted y,x) NOT COORDINATES of the point
ly,lx=307,200+dist_x 
ly1,lx1=317,194+dist_x

bgy,bgx=50,50 # background

#######################
# mouse callback function for testing
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=img[y,x]
        print(px)
#####################
def draw():
    cv2.circle(img, (lx,ly), 2, (255, 0, 0), -1)  #(216,156)lower point COORDINATES
    cv2.circle(img, (lx1,ly1), 2, (255, 0, 0), -1)  #(216,156)lower point COORDINATES
    
    cv2.circle(img, (ux,uy), 2, (255, 0, 0), -1)#(216,140)lower point COORDINATES
    cv2.circle(img, (bgx,bgy), 2, (255, 0, 0), -1) # backgrund check coordinates
    cv2.putText(img, 'Background', (305,50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 0, 255), 1, cv2.LINE_AA)
###################    

bounding_box = {"top": 100, "left": 0, "width": 830, "height": 500}

sct = mss()

x=input("Enter any key to start")
while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    #print(img[166,516],type(img[166,516]))
    px_d=list(img[ly,lx]) # lower pixel
    px_d1=list(img[ly1,lx1])
    px_u=list(img[uy,ux]) # upper pixel
    px_bg=list(img[bgy,bgx])

    if px_bg == [247,247,247,255]: # http://www.trex-game.skipser.com/
        if (px_d != [247,247,247,255]) or (px_d1 != [247,247,247,255]) or (px_u != [247,247,247,255]): #[255,255,255,255] for black obtracles
            #press('space') # loooong jump
            press('space')
            time.sleep(0.08)
            press('down')

            #count=count+1
            #print("jump ", count)  

    draw()
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
