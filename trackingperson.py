import cv2
import  time

cam = cv2.VideoCapture('2.mp4')
t=300;
while cam.isOpened():
    ret, frame = cam.read()
    ret, frame2 = cam.read()

    diffrence = cv2.absdiff(frame,frame2)
    grayscale = cv2.cvtColor(diffrence, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated= cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0),2)

    # for c in contours:
    #     if cv2.contourArea(c):
    #         continue
    #     else:
    #         while t:
    #             time.sleep(30);
    #             t=t-30
    #             if cv2.contourArea(c):
    #                 break
    #
    #         if t==0 :
    #             #lights off
    #             print("Lights off")
    #

    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow('Frame', frame)