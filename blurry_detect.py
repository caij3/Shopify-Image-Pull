import cv2
import argparse
from imutils import paths
import os
from os import listdir

def detect_blur_and_bright_spot(image_path, threshold):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding for bright spot detection
    _, binary_image = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Apply Laplacian filter for edge detection
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Calculate maximum intensity and variance
    _, max_val, _, _ = cv2.minMaxLoc(gray)
    binary_variance = binary_image.var()
    laplacian_variance = laplacian.var()

    # Initialize result variables
    blur_text = "Not Blurry"
    bright_spot_text = "No Bright Spot"

    # Check blur condition based on variance of Laplacian image
    if laplacian_variance < threshold:
        blur_text = "Blurry"

    # Check bright spot condition based on variance of binary image
    if 5000 < binary_variance < 8500:
        bright_spot_text = "Bright Spot"

    # Add labels to the image
    cv2.putText(image, blur_text, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.putText(image, bright_spot_text, (15, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# get the path/directory
folder_dir = "C:\\Users\\j-cai\\Downloads\\blurry_images\\images"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".jpg")):
        #print(folder_dir + "\\" + images)
        detect_blur_and_bright_spot(folder_dir + "\\" + images, 300)
