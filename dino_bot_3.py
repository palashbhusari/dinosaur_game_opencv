# this code is for half screen  http://www.trex-game.skipser.com/ game

import numpy as np
import cv2
from mss import mss
from PIL import Image # grab screen
from pyautogui import press, keyDown,keyUp, hotkey # for keyboard
import time



#base line to set dinosaur game
lx1,ly1= 148,358
lx2,ly2= 210,358

# x from left increase to go rigth 
# y from top increase to go down
px0,py0= 208,348
px1,py1=208,342 
px2,py2=142,342 # point on the dino
bgx,bgy=50,330

def draw():
    cv2.line(img,(lx1,ly1),(lx2,ly2),(0,0,255),2) # red line
    cv2.circle(img, (bgx,bgy), 2, (255, 0, 0), -1)  
    #points
    cv2.circle(img, (px1,py1), 2, (255, 0, 0), -1)  
    cv2.circle(img, (px2,py2), 2, (255, 0, 0), -1)
# mouse callback function for testing
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=img[y,x]
        print(px)

bounding_box = {"top": 100, "left": 0, "width": 830, "height": 500}
sct = mss()

x=input("Enter any key to start")
while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    # check background pixel value
    background=list(img[bgy,bgx])

    px_d0= list(img[py0,px0]) # lower front pixel
    px_d1= list(img[py1,px1]) # upper front pixel
    px_d2= list(img[py2,px2])
    #px_u=list(img[uy,ux]) 
    
    if (px_d1 != background) or (px_d0 != background): #[255,255,255,255] for white back ground
        press('space')
        while(1):
            sct_img = sct.grab(bounding_box)
            img=np.array(sct_img)
            px_d1= list(img[py1,px1])
            px_d2= list(img[py2,px2])
            background=list(img[bgy,bgx])
            if (px_d1 == background) and (px_d2 == background):
                press('down')
                break
 
    draw()
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
