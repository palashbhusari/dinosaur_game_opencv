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

px0,py0= 215,337 # lower point of rect
w0,h0=10,10  # weidth and height downward 

px1,py1=210,312  # upper rect

px2,py2=146,337 # rect on dino on the dino
w2,h2=60,5
bgx,bgy=50,330

def draw():
    cv2.line(img,(lx1,ly1),(lx2,ly2),(0,0,255),2) # red line
    cv2.circle(img, (bgx,bgy), 2, (255, 0, 0), -1)  
    # rect in front
    # square for cactus
    cv2.rectangle(img,(px0,py0),(px0+w0,py0+h0),(0,0,255),1)   
    # square for bird
    cv2.rectangle(img,(px1,py1),(px1+w0,py1+h0),(0,0,255),1)
    # rect below dino
    cv2.rectangle(img,(px2,py2),(px2+w2,py2+h2),(0,0,255),1)
    
    ##points
    #cv2.circle(img, (px0,py0), 2, (255, 0, 0), -1)  
    #cv2.circle(img, (px1,py1), 2, (255, 0, 0), -1)  
    #cv2.circle(img, (px2,py2), 2, (255, 0, 0), -1)
# mouse callback function for testing
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=img[y,x]
        print(px)

def roi():
    global roi0,roi1,roi2
    # # roi0 to detect obstacle
    roi0=int(np.sum(img[py0:py0+h0,px0:px0+w0]))# region o i 208,240 = x,y
    #print((np.sum(roi0)))# = 24700
    roi1=np.sum(img[py1:py1+h0,px1:px1+w0])

    ##roi2 to detect obstale under dino
    roi2=int(np.sum(img[py2:py2+h2,px2:px2+w2]))# region o i 208,240 = x,y
    #print(roi2,type(roi2)) #=
    
bounding_box = {"top": 100, "left": 0, "width": 830, "height": 500}
sct = mss()

x=input("Enter any key to start")
while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    ##gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## check background pixel value
    background=img[bgy,bgx]

    roi()

    ##pixel values
    #px_d0= img[py0,px0]# lower front pixel
    #px_d1= img[py1,px1]# upper front pixel 
    #px_d2= img[py2,px2] 
    
    #if (px_d1 != background) or (px_d0 != background): #[255,255,255,255] for white back ground
    if roi0 != 24700:
        press('space')
        while(1):
            sct_img = sct.grab(bounding_box)
            img=np.array(sct_img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            roi()
            
            if (roi0 == 24700) and (roi2 == 74100):
                press('down')
                break

    elif roi1 != 24700:
        keyDown('down')
        time.sleep(0.08)
        keyUp('down')

    draw()
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
