import cv2

import numpy as np

from tkinter import *

from tkinter import filedialog

root = Tk()

root.filename = filedialog.askopenfilename(title= 'Choose your image',filetypes=(('jpeg files','*.jpg'),('all files','*.*')))

def nothing(x):

    pass

def ResizeWithAspectRatio(image,width=None, height=None, inter=cv2.INTER_AREA):

    dim=None

    (h,w)= image.shape[:2]

    if width is None and height is None:

        return image

    if width is None:

        r= height/float(h)

        dim=(int(w*r),height)

    else :

        r = width/float(w)

        dim=(width,int(h*r))

    return cv2.resize(image,dim,interpolation=inter)

cv2.namedWindow("Trackbars")

cv2.resizeWindow('Trackbars',600,250)

cv2.createTrackbar('Huemin','Trackbars',0,180,nothing)

cv2.createTrackbar('Huemax','Trackbars',180,180,nothing)

cv2.createTrackbar('Satmin','Trackbars',0,255,nothing)

cv2.createTrackbar('Satmax','Trackbars',255,255,nothing)

cv2.createTrackbar('Valmin','Trackbars',0,255,nothing)

cv2.createTrackbar('Valmax','Trackbars',255,255,nothing)

while True:

    imag = cv2.imread(root.filename)

    image=ResizeWithAspectRatio(imag,width=550)

    hmin=cv2.getTrackbarPos('Huemin','Trackbars')

    hmax = cv2.getTrackbarPos('Huemax', 'Trackbars')

    smin = cv2.getTrackbarPos('Satmin', 'Trackbars')

    smax = cv2.getTrackbarPos('Satmax', 'Trackbars')

    vmin = cv2.getTrackbarPos('Valmin', 'Trackbars')

    vmax = cv2.getTrackbarPos('Valmax', 'Trackbars')

    print(hmin,hmax,smin,smax,vmin,vmax)

    lower=np.array([hmin,smin,vmin])

    upper = np.array([hmax,smax,vmax])

    mask = cv2.inRange(image,lower,upper)

    final_result = cv2.bitwise_and(image,image,mask=mask)

    cv2.imshow("Final Output",final_result)

    cv2.imshow("Mask",mask)

    cv2.imshow('Output',image)

    cv2.waitKey(1)
