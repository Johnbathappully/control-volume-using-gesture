 

# mediapipe

findHands method--------------- that processes the input image and detects hands. If hands are detected and the draw parameter is set to True, the hand landmarks and connections are drawn on the image.

findPosition method-------------- that extracts the positions of the hand landmarks, creates a bounding box around the hand, and optionally draws circles on the landmarks and a bounding box around the hand.

 fingersUp method ---------------that determines whether each finger is up (extended) or down (folded) by comparing the positions of their landmarks.

findDistance method---------------- that calculates the distance between two landmarks and optionally draws circles on the landmarks, a line connecting them, and a circle at the midpoint.


# control-volume-using-gesture
use Gesture Control to change the volume of a computer. application of hand tracking and then we will use the hand landmarks to find gestures of our hand to change the volume.


##Increasing Volume

![Screenshot (4081)](https://user-images.githubusercontent.com/114779060/235749450-8a83403b-0277-4505-a8ab-1e71af591bb4.png)


##Lowering Volume

![Screenshot (4080)](https://user-images.githubusercontent.com/114779060/235749480-c7c8de06-3d8b-47f3-878b-e0d4dc2d5c70.png)


control-mouse-using-fingers

steps

Start an infinite loop for continuous frame processing. Read a frame from the video capture object and find the hand landmarks using the hand detector.

Find the hand landmark positions and bounding box. If there are landmarks, get the x, y coordinates of the index and middle finger tips.

Get a list of which fingers are up. Draw a rectangle on the frame to define the mouse control area.

If the index finger is up and the middle finger is down, enable the "Moving Mode".Convert the index finger tip's coordinates to screen coordinates
.
Smooth the movement of the mouse(reduce jitter) by averaging the previous and current locations.Move the mouse and draw a circle at the index finger tip's location.
Update the previous location with the current location.

If both index and middle fingers are up, enable the "Clicking Mode".Find the distance between the index and middle finger tips and draw a line between them.
If the distance between the fingers is less than 40, click the mouse.

Calculate the frame rate and display it on the frame.Show the frame in an OpenCV window and wait for 1 millisecond before proceeding to the next frame.
