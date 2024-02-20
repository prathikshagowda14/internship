import cv2
import os

# Path to your video file
video_path = r"‪C:\\Users\\hp\\Downloads\\pexels_videos_2670 (1080p).mp4‪"

# Output folder for frames
output_folder = r"‪C:\\Users\\hp\\Documents\\output"

# Open the video file
video_capture = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

# Read and save frames in a loop
frame_count = 0
i

    # Save the frame to the output folder
frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
cv2.imwrite(frame_filename, frame)

    # Increment frame count
frame_count += 1

# Release the video capture object
video_capture.release()

print(f"Frames saved to {output_folder}")
