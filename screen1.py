import numpy as np
import cv2
from mss import mss
from PIL import Image # grab screen
from pyautogui import press, keyDown,keyUp, hotkey # for keyboard
import time
count =0
dino_origin=80,170 # (x,y)
first_time=0

########### change the distance between dino and points########
dist_x=-25
##########################################


uy,ux=129,170+dist_x # PIXELS(inverted y,x) NOT COORDINATES of the point
ly,lx=154,170+dist_x 
ly1,lx1=164,164+dist_x

bgy,bgx=50,300
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
    image = cv2.putText(img, 'Background', (305,50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 0, 255), 1, cv2.LINE_AA)
###################    

        
bounding_box = {'top': 100, 'left': 350, 'width': 650, 'height': 220}

sct = mss()

x=input("make sure dino the game is in right place and Enter any key to start")
while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    #print(img[166,516],type(img[166,516]))
    px_d=list(img[ly,lx]) # lower pixel
    px_d1=list(img[ly1,lx1])
    px_u=list(img[uy,ux]) # upper pixel
    px_bg=list(img[bgy,bgx])
    #print(px_d,"   ",px_u)        
    #print(px_bg)

    if px_bg == [255,255,255,255]:# for white background
        if (px_d != [255,255,255,255]) or (px_d1 != [255,255,255,255]) or (px_u != [255,255,255,255]): #[255,255,255,255] for black obtracles
            #press('space') # loooong jump
            press('space')
            time.sleep(0.08)
            press('down')

            #count=count+1
            #print("jump ", count)
            #print(px_d,"   ",px_u)           
 
    elif px_bg != [255,255,255,255]:# for black background
        print(px_d,"   bg= ",px_bg)

        ##if (px_d == [172,172,172,255] or px_d == [8,8,0,255]) or (px_u == [172,172,172,255] or px_u == [8,8,0,255]): #[172,172,172,255] for grey obtracles
        if (px_d != [0,0,0,255]) or (px_u != [0,0,0,255]):
            #press('space') # loooong jump
            press('space')
            time.sleep(0.08)
            press('down')

    draw()
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
