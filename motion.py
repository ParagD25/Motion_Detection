import cv2

frame_first=None
face_capture=cv2.VideoCapture(0)

while True:
    check,frame=face_capture.read()
    gray_scale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_scale_img=cv2.GaussianBlur(gray_scale_img,(21,21),0)

    if frame_first is None:
        frame_first=gray_scale_img
        continue

    blured_frame=cv2.absdiff(frame_first,gray_scale_img)
    
    #Threshold Frame
    threshold_frame=cv2.threshold(blured_frame,35,255,cv2.THRESH_BINARY)[1]
    #Clear frame
    threshold_frame=cv2.dilate(threshold_frame,None,iterations=3)

    #Countour
    (contour,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cntr in contour:
        if cv2.contourArea(cntr)<1000:
            continue

        (x,y,w,h)=cv2.boundingRect(cntr)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Normal Frame',frame) #Normal Image
    cv2.imshow('Gray Scale Image',gray_scale_img) #Gray Image
    cv2.imshow('Blur Frame',blured_frame) #Faded Image
    cv2.imshow('Threshold Frame',threshold_frame) #White And Black Image

    press_key=cv2.waitKey(1)
    if press_key==ord('q'):
        break
    
face_capture.release()
cv2.destroyAllWindows()
