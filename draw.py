import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)

# paint the image a certain colour
# blank[200:300,200:300] = 0,225,0
# cv.imshow('green',blank)

# draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,225,0),1)
# cv.imshow('Rectangle',blank)

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,225,0),1)
# cv.imshow('Circle',blank)

cv.putText(blank,'hello',(225,225),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(225,0,0),2)
cv.imshow('text',blank)


cv.waitKey(0)