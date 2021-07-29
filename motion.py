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

    cv2.imshow('Normal Frame',frame)
    cv2.imshow('Gray Scale Image',gray_scale_img)
    cv2.imshow('Blur Frame',blured_frame)

    press_key=cv2.waitKey(1)
    if press_key==ord('q'):
        break
    
face_capture.release()
cv2.destroyAllWindows()
