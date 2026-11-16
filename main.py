import cv2

stream=cv2.VideoCapture(0)
print()
if not stream.isOpened():
    print("No stream:(")
    exit()
    
    while(true):
        ret,frame=stream.read()
        if not ret:
            print("No more stream :(")
            break
        cv2.imshow("webcam!", frame)
        if cv2.waitKey(1)==ord('q'):
            break
        
    stream.release()
    cv2.destroyAllWindows()

            