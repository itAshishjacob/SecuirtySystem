import cv2 as cv


# #caputre image
# img = cv.imread('cat.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)

#################################################################
#rescale for live vid
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


#rescale code
def rescale (frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    
    return cv.resize(frame,dim,)

#capture video


capture = cv.VideoCapture('ep1.mkv')

while True :
    isTrue, frame = capture.read()
    frame_re = rescale (frame)
    cv.imshow('video',frame)
    cv.imshow('video rezised',frame_re)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
