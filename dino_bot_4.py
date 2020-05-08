# this code is for half screen  http://www.trex-game.skipser.com/ game

import numpy as np
import cv2
from mss import mss
from PIL import Image # grab screen
from pyautogui import press, keyDown,keyUp, hotkey # for keyboard
import time


## base line to set dinosaur game
lx1,ly1= 180,158
lx2,ly2= 210,158

## x from left increase to go rigth 
## y from top increase to go down
px0,py0= 230,142 # lower point of square
px1,py1=230,112  # upper square
w0,h0=5,5  # weidth and height downward of square

#pixel below dino
dist=0
t=True
px2,py2=175,148 # rect on dino on the dino

eyex,eyey=180,126

bgx,bgy=50,130

## mouse callback function for testing
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=img[y,x]
        print(px)

def get_image():
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    # Convert image to gray then black/ white
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bwImage) = cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY)
    bwImage = cv2.cvtColor(bwImage, cv2.COLOR_GRAY2RGB)
    return bwImage
def roi():
    global roi0,roi1,px_sum
    # # roi0 to detect obstacle
    roi0=int(np.sum(img[py0:py0+h0,px0:px0+w0]))# region o i 208,240 = x,y
    #print(roi0)# = 19125 white
    roi1=np.sum(img[py1:py1+h0,px1:px1+w0])
    px_list=[]
    for i in range(0,60,4): # 2,4,6,8
        px=sum(img[py2,px2+i])
        px_list.append(px)
    px_sum=sum((px_list))
    
def draw():
    cv2.line(img,(lx1,ly1),(lx2,ly2),(0,0,255),2) # red line 
    # square for cactus
    cv2.rectangle(img,(px0,py0),(px0+w0,py0+h0),(0,0,255),1)   
    # square for bird
    cv2.rectangle(img,(px1,py1),(px1+w0,py1+h0),(0,0,255),1)
    #dino eye
    cv2.circle(img, (eyex,eyey), 2, (0, 0, 255), -1)  
    ##points
    for i in range(0,60,4):
        cv2.circle(img, (px2+i,py2), 2, (255, 0, 0), -1)  

def update_px(): # for changing speeds and updating detector dist
    global t,px0,px1
    if (t==True) and (jump==45):
        px0=px0+10
        t=False
    if (t==False)and jump==70:
        px0=px0+10
        t=True
    if (t==True) and (jump==100):
        px0=px0+10
        px1=px1+15
        t=False
    if (t==False) and (jump==150):
        px0=px0+10
        t=True
    if (t==True) and (jump==300): # mostly constant after this point
        px0=px0+10
        t=False
    if (t==False) and (jump==2000):
        px0=px0+5
        t=True

bounding_box = {"top": 300, "left": 0, "width": 830, "height": 300}
sct = mss()

x=input("Enter any key to start")
jump=0
prev=0
last_time=time.time()
while True:
    img=get_image()
    roi() #get pixel data
    if roi0 != 19125:
        press('space')
        b=0
        while(1):
            b=b+1# internal loop breaker
            img=get_image()
            roi()
            #print(px_sum)
            if px_sum==11475:
                press('down')
                break
            elif b>50:
                break # break internal loop
        #time.sleep(0.08)
        #press('down')
        jump=jump+1
    elif roi1 != 19125: # px1,py1 upper square
        keyDown('down')
        time.sleep(0.08)
        keyUp('down')
    # update detector dist
    update_px()
    if jump !=prev:
        print(jump)
        prev=jump
    
    cv2.putText(img, str(jump), (bgx,bgy), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 1, cv2.LINE_AA)
    draw()
    cv2.imshow('screen',img )
    #cv2.setMouseCallback('screen',find_value)
    print("time = {}".format(time.time()-last_time))
    last_time=time.time()
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
