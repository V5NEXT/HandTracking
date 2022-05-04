import cv2 as cv
# import mediapipe as mp
import time

capture = cv.VideoCapture(0)

while True:
    success, img = capture.read()

    cv.imshow("Image", img)
    cv.waitKey(1)