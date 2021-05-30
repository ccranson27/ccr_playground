import sys
import cv2
# import numpy as np
import matplotlib.pyplot as plt
# import os.path
from os import path


# Method: getFrames
# Purpose: Extract a predefined number of frames from a provided video
# Parameters: video_capture: provided video
#             frame_num: the desired number of frames
#             frame_start: optional value to input for start of frame
def get_frames(video_capture, frame_num, frame_start=0):
    counter = 0
    image_arr = []
    frame_num = frame_start + frame_num
   
    # Loop through and create individual frames that were captured from the video file
    while True and counter < frame_num:
        is_image_good, image = video_capture.read()
        if not is_image_good:
            if counter == 0:
                print('Video cannot be read from file')
            break
      
        # Use opencv to write the frame that was extracted from the video
        if counter >= frame_start:
            image_arr.append(image)
      
        # Increment the counter as more frames are extracted
        counter += 1
   
    # Frames to be returned
    return image_arr


# Method: getEdges
# Purpose: gets the edges in an image via converting to gray scale than blurring the image
# Parameters: frame_list: list of frames
#             line_size: how large the lines should be on edges
#             blur_value: how blurred the image should be    
def get_edges(frame_list, line_size, blur_value):
    frame_edges = []
    for i in frame_list:
        gray_image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        gray_blurred_image = cv2.medianBlur(gray_image, blur_value)
        frame_edges.append(cv2.adaptiveThreshold(gray_blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value))
     
    return frame_edges


# Method: rgb2gray
# Purpose: Algorithm to convert a color image to gray scale in matplotlib
# Parameters: image (The image array to convert)
def rgb2gray(image):
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    return 0.2989 * red + 0.5870 * green + 0.1140 * blue


# Capture Video input from an mp4 file
video = input("Please enter the name of the video:\n") # All videos must be in 'Videos' directory
if not path.isfile('Videos/' + video):
    print('Invalid video input')
    sys.exit(1)
cap = cv2.VideoCapture('Videos/' + video)

# Get frames from first video file 
number_of_frames = int(input("Please enter the number of frames to obtain:\n"))
start_frame = int(input("Please enter the first frame to be collected and processed:\n"))
output_info = int(input("Please enter 1 for frames only, 2 for edges only, or 3 for both:\n"))
frames = get_frames(cap, number_of_frames, start_frame)
if output_info == 2 or output_info == 3:
    edges = get_edges(frames, 9, 5)

figure_count = 1
for i in range(len(frames)):
    plt.figure(figure_count)
    plt.title('Frame '+ str(i+1))
    plt.imshow(frames[i])
    plt.draw()
    figure_count += 1
    plt.figure(figure_count)
    gray_frame = rgb2gray(frames[i])
    plt.title('Gray Scale Frame ' + str(i+1))
    plt.imshow(gray_frame, cmap="gray")
    plt.draw()
    if output_info == 2 or output_info == 3:
        figure_count += 1
        plt.figure(figure_count)
        plt.title('Edge '+ str(i+1))
        plt.imshow(edges[i])
        plt.draw()
    figure_count += 1

# Show each of the selected frames by the user
plt.show()

# Release all windows upon completion
cap.release()
cv2.destroyAllWindows()


