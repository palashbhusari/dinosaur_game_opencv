import numpy as np
import cv2
from mss import mss
from PIL import Image

# mouse callback function
def find_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px=image[x,y]
        print(px)



bounding_box = {'top': 100, 'left': 0, 'width': 1000, 'height': 400}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    img=np.array(sct_img)
    #print(img[166,516],type(img[166,516]))
    px1=list(img[166,516])
    #print(px1)
    if px1 != [255,255,255,255]:
        print("jump")
    cv2.circle(img, (516,166), 2, (255, 0, 0), -1)
    cv2.circle(img, (516,140), 2, (255, 0, 0), -1)
    
    
    cv2.imshow('screen',img )
    cv2.setMouseCallback('screen',find_value)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
