import cv2 as cv
import mediapipe as mp
import time


capture = cv.VideoCapture(0)
cTime = 0
pTime = 0
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=4)
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = capture.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handlms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img,str(int(fps)), (10,70), cv.FONT_HERSHEY_SIMPLEX,
               3, (255,0,255),3)
    cv.imshow("Image", img)
    cv.waitKey(1)