# Resistor-Identifier 
### (See Resistor_Identifier.pptx for more introduction and video demo)
The main purpose of this project is to construct an automated resistor identifier. The resistors are locating with a Haar Cascade Classifier. The classifier is trainned on 1000 positive images and 1500 negative images. Then the color is read through thresholding certain color ranges in HSV color space.

## Hareware setup
* camera: Logitech C920

> If different camera is used, it may be necessary to modify resolution setting for camera capture.

## Software dependency
* numpy=1.16.4
* opencv-python=3.4.3

## Execution
Run the program with the following command:
``` bash
python main.py
```
Note that the index in ```Videocapture(0)``` may need to be change according to different conputer and camera.



