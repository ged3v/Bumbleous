import cv2

# Image 1
img_raw = 'car1.jpg'
img_raw = "images/img_cars/cars_back/car1.jpg"

# pre-trained car classifier
trained_classifier = 'car_detector.xml'

# create an opencv image
img = cv2.imread(img_raw)

# convert to grayscale (needed for haar cascade algorithm)
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Create a car classifier
car_tracker = cv2.CascadeClassifier(trained_classifier)


# Display image with car's spotted.
cv2.imshow('Bumbleous Image Detector', gray_scale)

 
 # Don't autoclose (Wait and listen for a key press)
cv2.waitKey()
 
 
print("Operation Completed") 
