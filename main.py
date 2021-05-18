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

# Method: getEdges
# Purpose: gets the edges in an image via converting to gray scale than bluring the image
# Parameters: frame_list: list of frames
#             line_size: how large the lines should be on edges
#             blur_value: how blurred the image should be    
def getEdges(frame_list, line_size, blur_value):
  frame_edges = []
  for i in frame_list:
     gray_image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
     gray_blurred_image = cv2.medianBlur(gray_image, blur_value)
     frame_edges.append(cv2.adaptiveThreshold(gray_blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value))
     
  return frame_edges
    
# Capture Video input from an mp4 file
cap = cv2.VideoCapture('Videos/zoom_0.mp4')

# Get frames from first video file 
frames = getFrames(cap, 3, 3)
edges = getEdges(frames, 9, 5)
for i in range(len(edges)):
   cv2.imshow('Frame: ' + str(i), edges[i])
   cv2.waitKey(0)

# Release all windows upon completion
cap.release()
cv2.destroyAllWindows()


