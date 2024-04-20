import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def ad(x):
    pass

cv2.namedWindow("color")

cv2.createTrackbar("Lower_H", "color", 0, 255, ad)
cv2.createTrackbar("Lower_S", "color", 0, 255, ad)
cv2.createTrackbar("Lower_V", "color", 0, 255, ad)
cv2.createTrackbar("Upper_H", "color", 255, 255, ad)
cv2.createTrackbar("Upper_S", "color", 255, 255, ad)
cv2.createTrackbar("Upper_V", "color", 255, 255, ad)

while True:
    _,frame =cap.read()
    frame = cv2.resize(frame,(400,400))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lo_h = cv2.getTrackbarPos("Lower_H", "color")
    lo_s = cv2.getTrackbarPos("Lower_S", "color")
    lo_v = cv2.getTrackbarPos("Lower_V", "color")

    up_h = cv2.getTrackbarPos("Upper_H", "color")
    up_s = cv2.getTrackbarPos("Upper_S", "color")
    up_v = cv2.getTrackbarPos("Upper_V", "color")

    lower_bound = np.array([lo_h, lo_s, lo_v])
    upper_bound = np.array([up_h, up_s, up_v])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("img", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()
