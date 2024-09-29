import cv2

# Capture video from the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load the classifier from the cascade file
majinBooClassif = cv2.CascadeClassifier('../cars_train/classifier/cascade.xml')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects in the frame using the classifier
    toy = majinBooClassif.detectMultiScale(
        gray,
        scaleFactor=4,
        minNeighbors=70,
        minSize=(50, 50)
    )

    # Draw a rectangle and label around detected objects
    for (x, y, w, h) in toy:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Car', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the video frame with the detections
    cv2.imshow('frame', frame)

    # Exit on pressing the 'Esc' key
    if cv2.waitKey(1) == 27:
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
