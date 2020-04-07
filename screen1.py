import numpy as np
import cv2
from mss import mss
from PIL import Image # grab screen
from pyautogui import press, typewrite, hotkey # for keyboard

count =0
lower_px=158,220 # PIXELS(inverted y,x) NOT COORDINATES of the point
lower_px1=164,220
upper_px=140,220
bg=50,300
#######################
# mouse callback function for testing
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=img[y,x]
        print(px)
#####################
def draw():
    cv2.circle(img, (216,156), 2, (255, 0, 0), -1)  #(216,156)lower point COORDINATES
    cv2.circle(img, (216,164), 2, (255, 0, 0), -1)  #(216,156)lower point COORDINATES
    
    cv2.circle(img, (216,140), 2, (255, 0, 0), -1)#(216,140)lower point COORDINATES
    cv2.circle(img, (300,50), 2, (255, 0, 0), -1) # backgrund check coordinates
    image = cv2.putText(img, 'Background', (305,50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 0, 255), 1, cv2.LINE_AA)
###################    

        
bounding_box = {'top': 100, 'left': 300, 'width': 1000, 'height': 400}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    #print(img[166,516],type(img[166,516]))
    px_d=list(img[lower_px]) # lower pixel
    px_d1=list(img[lower_px1])
    px_u=list(img[upper_px]) # upper pixel
    px_bg=list(img[bg])
    #print(px_d,"   ",px_u)
    #print(px_bg)
    if px_bg == [255,255,255,255]:# for white background
        if (px_d != [255,255,255,255]) or (px_d1 != [255,255,255,255]) or (px_u != [255,255,255,255]): #[255,255,255,255] for black obtracles
            press('space')
            count=count+1
            print("jump ", count)
            print(px_d,"   ",px_u)
    
    else:# for black background
        ##if (px_d == [172,172,172,255] or px_d == [8,8,0,255]) or (px_u == [172,172,172,255] or px_d == [8,8,0,255]): #[172,172,172,255] for grey obtracles
        if (px_d != [0,0,0,255]) or (px_u != [0,0,0,255]):
            press('space')
            count=count+1
            print("jump ", count)

    draw()
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
