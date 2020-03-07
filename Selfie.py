import cv2 as cv
import os
import time

def set_path():
    photos = os.listdir('Pics/')
    pic_index = len(photos)
    path ='Pics/Selfie'+'_'+str(pic_index)+'.jpg'
    return path

def click(path):
    camera = cv.VideoCapture(0)    # webcam Index
    if (camera.isOpened() != True):
        camera.open()
    ret,frame = camera.read()
    cv.imwrite(path,frame)
    cv.imshow('Image',frame)
    
    cv.destroyAllWindows()
    
    print('Photo saved Sucessfully at '+path)
    
    fd = open('History.txt','a+')
    fd.write(path)
    fd.write(' ')
    fd.write(time.ctime())
    fd.write('\n')
    fd.close()

path = set_path()
click(path)

