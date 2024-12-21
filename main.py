import cv2
import numpy as np
from windowcapture import WindowCapture  # Import your WindowCapture class

# Initialize WindowCapture for your application
wincap = WindowCapture('RuneLite')  # Replace 'RuneLite' with your actual window title

# Global variables to store the live HSV image
hsv = None

# Mouse callback to print HSV values
def pick_hsv(event, x, y, flags, param):
    global hsv
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click
        # Get HSV value at the clicked point
        if hsv is not None:  # Ensure image is available
            pixel = hsv[y, x]  # Get pixel HSV values
            h, s, v = pixel
            print(f"HSV Value at ({x}, {y}): H={h}, S={s}, V={v}")

# Create a named window
cv2.namedWindow("Live Feed")
cv2.setMouseCallback("Live Feed", pick_hsv)

print("Click anywhere on the window to get HSV values. Press 'q' to quit.")

# Main loop to capture and display live images
while True:
    # Capture a screenshot from the window
    screenshot = wincap.get_screenshot()

    # Resize if necessary for better visibility (optional)
    screenshot = cv2.resize(screenshot, (800, 600))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

    # Display the live feed
    cv2.imshow("Live Feed", screenshot)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
