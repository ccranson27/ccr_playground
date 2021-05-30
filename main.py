import sys
import matplotlib.pyplot as plt
from os import path
from frame_gathering import *

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
    plt.title('Frame ' + str(i+1))
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


