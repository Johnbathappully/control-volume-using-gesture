 

# mediapipe

findHands method--------------- that processes the input image and detects hands. If hands are detected and the draw parameter is set to True, the hand landmarks and connections are drawn on the image.

findPosition method-------------- that extracts the positions of the hand landmarks, creates a bounding box around the hand, and optionally draws circles on the landmarks and a bounding box around the hand.

 fingersUp method ---------------that determines whether each finger is up (extended) or down (folded) by comparing the positions of their landmarks.

findDistance method---------------- that calculates the distance between two landmarks and optionally draws circles on the landmarks, a line connecting them, and a circle at the midpoint.


# control-volume-using-gesture

Steps 

 Define the width and height of the camera feed (wCam and hCam).

Initialize the camera using OpenCV, set its width and height, and initialize a variable to store the previous time (pTime).

Create an instance of the handDetector class from the HandTrackingModule with a detection confidence of 0.7 and a maximum of 1 hand.

Initialize pycaw to control the audio volume of the system. Get the minimum and maximum volume levels and initialize variables to store the volume, volume bar, and volume percentage.

Initialize a variable to store the area of the hand bounding box, and set the initial volume bar color.

Read a frame from the camera feed.
Find the hand in the image using the handDetector.Get the list of hand landmarks and bounding box of the detected hand.If landmarks are detecteCalculate the area of the bounding box, and filter based on size.If the area is within the specified range:Find the distance between the thumb and index finger landmarks.Map the distance to volume bar and percentage values.Smooth the volume percentage by rounding to the nearest multiple of 10.Determine which fingers are up using the handDetector.If the pinky finger is down, set the system volume to the calculated volume percentage and change the volume bar color to green. Otherwise, set the color to red.

Draw a static volume bar and the current volume bar on the image.

Display the volume percentage on the image.

Display the current system volume and set the color based on the pinky finger state.



##Increasing Volume

![Screenshot (4081)](https://user-images.githubusercontent.com/114779060/235749450-8a83403b-0277-4505-a8ab-1e71af591bb4.png)


##Lowering Volume

![Screenshot (4080)](https://user-images.githubusercontent.com/114779060/235749480-c7c8de06-3d8b-47f3-878b-e0d4dc2d5c70.png)


control-mouse-using-fingers

Steps

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
