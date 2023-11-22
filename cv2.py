import cv2

# Create a VideoCapture object to capture video from the webcam (usually the default webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam")
    exit()

# Read frame by frame from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is empty
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Display the frame (optional, for visualization purposes)
    cv2.imshow('Webcam Output', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close any open windows
cap.release()
cv2.destroyAllWindows()
