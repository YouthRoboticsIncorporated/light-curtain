import cv2 as cv

cv.namedWindow("preview")
vc = cv.VideoCapture(-1)

if vc: # try to get the first frame
    vc.set(cv.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    vc.set(cv.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    retval, frame = vc.read()

while retval:
    # Split the frame into components.
    green_img = cv.split(frame)[1]
    
    # Find the maximum pixel value in the green image.
    [minVal, maxVal, minLoc, maxLoc] = cv.minMaxLoc(green_img)
    
    # Don't show anything below this fraction of the max pixel value. Trial and error.
    margin = 0.92
    
    # Threshold value in pix value to be extracted
    thresh = int( maxVal * margin)
    
    # Do the thresholding.
    retval, thresh_img = cv.threshold(green_img, thresh, 255, cv.cv.CV_THRESH_BINARY)
    
    # Show the result
    cv.imshow("preview", thresh_img)
    
    # Get the next frame
    retval, frame = vc.read()
    
    key = cv.waitKey(20)
    if key != -1: # exit on any key
        break
    # Loop forever...
