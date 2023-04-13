import numpy as np
import cv2
from picamera2 import Picamera2 
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()


while True:
		frame = picam2.capture_array()
		#print(frame)
		# Our operations on the frame come here
		
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#Threshold of yellow on HSV space
		lower_yellow = np.array([20, 100, 100])
		upper_yellow = np.array([30, 255, 255])
		
		#blob detector
		#detector = cv2.SimpleBlobDetector()
		
		mask = cv2.inRange(gray, lower_yellow, upper_yellow)
		result = cv2.bitwise_and(frame, frame, mask = mask)
		
		
		#keypoints = detector.detect(gray)
		#im_with_keypoints = cv2.drawKeypoints(gray,   keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		# Display the resulting frame
		#cv2.imshow('frame',gray)
		cv2.imshow('mask', mask)
		cv2.imshow('result', result)
		#cv2.imshow('mask', im_with_keypoints)
		if cv2.waitKey(1) & 0xFF == ord('q'):
				break

# When everything done, release the capture
cv2.destroyAllWindows()
