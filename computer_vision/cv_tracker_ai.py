import cv2

#car img_ file
img_file = 'car1.jpg'
img_file = ("images/img_cars/cars_back/car1.jpg")
#video 
video = cv2.VideoCapture('vid1.mp4')
video = cv2.VideoCapture('images/vid_cars/vid1.mp4')

# pre-trained car classifier
classifier_file= 'car_detector.xml'
classifier_file = "trained_classifiers/car_detector.xml"
#car tracker
car_tracker = cv2.CascadeClassifier(classifier_file)

#while loop for the video
while True:
    #Read the current frame
    (read_successfull, frame) = video.read()

    #safe coding
    if read_successfull:
        graysacled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect the cars
    cars = car_tracker.detectMultiScale(graysacled_frame)

    #Draw the rectangles 
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2) 

        # display the image with the cars spotted
    cv2.imshow('Clever Programmer Car Detector', frame) #img color and #black_white 


  # Wait for keypress.
    cv2.waitKey(1)

print("Operation Successful")
