import cv2
from PIL import Image
from util import get_limits

video_path = "yellow_object.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Define the target color (Yellow in BGR)
yellow = [0, 255, 255]

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Stop when video ends

    # Convert frame to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get color limits for yellow
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Create a binary mask
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert mask to Image object to find bounding box
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    # Draw bounding box if yellow is detected
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Show the frame
    cv2.imshow("Yellow Detection", frame)

    # Press 'q' to quit early
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Release and close windows
cap.release()
cv2.destroyAllWindows()