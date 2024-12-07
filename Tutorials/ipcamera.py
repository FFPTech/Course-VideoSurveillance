# Install packages
# pip install opencv-python
 
# import libraries
import cv2 as cv2

# Replace this with the IP address and port shown by the IP Webcam app
url = 0 # TODO: add your own IP adress here

# Open a connection to the video stream
cap = cv2.VideoCapture(url)

# resizing factor
f = 0.5

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # Resize the resulting frame
    frame = cv2.resize(frame, (0, 0), fx=f, fy=f, interpolation=cv2.INTER_CUBIC)

    # Display the resulting frame
    cv2.imshow('IP Webcam Stream', frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
