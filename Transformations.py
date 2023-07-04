import cv2 as cv
import numpy as np
img = cv.imread('cat.jpg')
cv.imshow('cat',img)

def translate(img,x,y):
    tansmat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,tansmat,dim)


#1 Translating a image
# -x --> left
# -y --> up
# x --> right
# y --> down


translated = translate(img,100,100)
cv.imshow('translated',translated)

#2 Rotation
def rotate (img,angle, rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated',rotated)

#3 flipping

flip = cv.flip(img,1)
cv.imshow('Flip',flip)

#cropped

cropped = img[200:400,300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)

