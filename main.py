import threading
import cv2
from deepface import DeepFace

# Capture from my laptops one camera hence '0'
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not capture.isOpened():
    print("Error: Could not open the camera.")
    exit()
else:
    print("Camera is turned on.")

# set height and width
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

img = cv2.imread("sample_pic.jpg")

# used to check if the frame matches the sample img
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    # camera captures frame
    ret_val, frame = capture.read()

    if ret_val:
        # check every 30 loops using a frame copy
        if counter % 30 == 0: 
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                # since we dont care if we can't recognize the face
                pass
        counter += 1
            
        # display result after chekcing with check_face for verification
        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)

        cv2.imshow("result", frame)
    
    # process user input
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()