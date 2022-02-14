import cv2

# Image 1
img_raw = 'car1.jpg'

img_raw = "img_cars/cars_back/car1.jpg"

# pre-trained car classifier
trained_classifier = 'car_detector.xml'

# create an opencv image
img = cv2.imread(img_raw)

# Display the image with cars spotted.
cv2.imshow('Bumbleous Image Detector', img) 

# Don't autoclose (Wait and listen for a key press)
cv2.waitKey()
 
print("Operation Completed")  
