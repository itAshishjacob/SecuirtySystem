import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('cat',img)

#1 greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blur (reduces noise)
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)


# Edge cascade
cascade = cv.Canny(img,125,175)
cv.imshow('canny',cascade)

#dialating the image
dialated = cv.dilate(cascade,(7,7),iterations=3)
cv.imshow('dialated ',dialated)

#eroding
eroded = cv.erode(dialated,(7,7),iterations=3)
cv.imshow('eroded ',eroded)

cv.waitKey(0)