import cv2
import os

cascade_path = r"./data/"

face_cascade = cv2.CascadeClassifier(
    os.path.join(cascade_path, "haarcascade_frontalface_default.xml")
)

smile_cascade = cv2.CascadeClassifier(
    os.path.join(cascade_path, "haarcascade_smile.xml")
)

eye_cascade = cv2.CascadeClassifier(
    os.path.join(cascade_path, "haarcascade_eye.xml")
)

# Verify that the files loaded correctly
print("Face:", not face_cascade.empty())
print("Smile:", not smile_cascade.empty())
print("Eyes:", not eye_cascade.empty())

if face_cascade.empty() or smile_cascade.empty() or eye_cascade.empty():
    raise Exception("Could not load Haar Cascade files!")

def detect_features(frame):
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w, h) in faces:
        frame=cv2.rectangle(frame, (x, y),(x+w, y+h),
                            color=(0, 0,255), thickness=5)
        face=frame[y : y+h, x : x+w]
        gray_face=gray[y : y+h, x : x+w]
        smiles=smile_cascade.detectMultiScale(gray_face,
                        2.5, minNeighbors=9)
        for(xp, yp, wp, hp)in smiles:
            face=cv2.rectangle(face,(xp, yp),(xp+wp, yp+hp),
                                color=(0, 255, 0), thickness=5)
            
            eyes=eye_cascade.detectMultiScale(gray_face,
                                              2.5, minNeighbors=5)
            for(xp, yp, wp, hp)in eyes:
                face=cv2.rectangle(face,(xp, yp),(xp+wp, yp+hp),
                                color=(255, 0, 0), thickness=5)
                
                    
        
    return frame 
    


stream=cv2.VideoCapture(0)
print()
if not stream.isOpened():
    print("No stream:(")
    exit()
    
fps=stream.get(cv2.CAP_PROP_FPS)
width=int(stream.get(3))
height=int(stream.get(4))
output=cv2.VideoWriter("assets/video.mp4",
            cv2.VideoWriter_fourcc('m', 'p','4', 'v'  ),
            fps=fps, frameSize=(width,height))

while(True):
    ret,frame=stream.read()
    if not ret:
        print("No more stream :(")
        break
    
    frame=detect_features(frame) 
    output.write(frame)
    cv2.imshow("webcam!", frame)
    if cv2.waitKey(1)==ord('q'):
        break
    
stream.release()
output.release()

cv2.destroyAllWindows()
print(output)

            
