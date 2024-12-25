import cv2
import os

root_path = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(root_path,'images','Facebook_2.mp4')

# Add debug print statements to verify the path
print(f"Looking for video at: {video_path}")
print(f"File exists: {os.path.exists(video_path)}")

video = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not video.isOpened():
    print("Error: Could not open video file")
    exit()

while True:
    ret, frame = video.read()
    
    # Break the loop if video ends
    if not ret:
        print("End of video")
        break
        
    cv2.imshow('Video', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()

