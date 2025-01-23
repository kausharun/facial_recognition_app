import threading
import cv2
from deepface import DeepFace

#Capture from my laptops one camera hence '0'
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#set height and width
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)