#### TDL:
 - Test prediction results and location with resized images
 - Translate the data I recieve from the prediction results to fit the needs of the back-end, i.e. thrust vectors or smth like that
 - Once everything is working, remove the bit of code that saves the images, it would be of no further use

### Optional TDL:
 - Draw a circle on the image preview so that the prediction results are clearly visible in a GUI (cv2.circle(), though I still have to figure out if it's a completely opaque circle or a circumference, also I don't think putting the label and the confidence will be possible)
 - Improve roboflow dataset so that the thing detects more stuff and not just really common things like plastic bottles and the ocasional disposable cup
