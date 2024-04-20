# HSV-Detection

## Color Tracking using OpenCV
This Python script demonstrates color tracking using OpenCV's cv2 library. It captures video from the default camera (VideoCapture(0)) and allows you to specify lower and upper HSV (Hue, Saturation, Value) values using trackbars for color segmentation.

## Requirements
Python 3.x
OpenCV (cv2)
NumPy (numpy)
Installation
You can install OpenCV and NumPy using pip:

``` bash
pip install opencv-python numpy
```
Usage
Run the script (python HSV-Detection.py).
## Adjust the trackbars to define the lower and upper HSV bounds for the color you want to track.
The script will display three windows:
img: Shows the original video frame.
mask: Displays the binary mask of the color within the specified HSV range.
res: Displays the result of bitwise AND operation between the frame and the mask, highlighting the tracked color.
Controls
Use the trackbars to adjust the lower and upper HSV values to isolate the desired color.
Press Esc to exit the program.
