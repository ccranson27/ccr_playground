import cv2
import numpy as np
import matplotlib.pyplot as plt


# Method: getFrames
# Purpose: Extract a predefined number of frames from a provided video
# Parameters: video_capture: provided video
#             frame_num: the desired number of frames
#             frame_start: optional value to input for start of frame
def getFrames(video_capture, frame_num, frame_start=0):
   counter = 0
   image_arr = []
   frame_num = frame_start + frame_num
   
   # Loop through and create individual frames that were captured from the video file
   while True and counter < frame_num:
      flaggy_flag,image = video_capture.read()
      if not flaggy_flag:
         if counter == 0:
            print('Video cannot be read from file')
         break
      
      # Use opencv to write the frame that was extracted from the video
      if counter >= frame_start:
         # cv2.imshow(frame_name, image)
         # cv2.waitKey(0)
         image_arr.append(image)
      
      # Increment the counter as more frames are extracted
      counter += 1
   
   # Frames to be returned
   return image_arr 
    
# Capture Video input from an mp4 file
cap = cv2.VideoCapture('Videos/zoom_0.mp4')

# Get frames from first video file 
frames = getFrames(cap, 3, 3)
for i in range(len(frames)):
   cv2.imshow('Frame: ' + str(i), frames[i])
   cv2.waitKey(0)

# Release all windows upon completion
cap.release()
cv2.destroyAllWindows()


