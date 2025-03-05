HomeTeam Network: AI Engineer Take-Home Project
Simple Sports Motion Detection
Project Overview
This project implements a basic motion detection system for sports videos. The system identifies and highlights areas of activity by processing video frames, detecting motion using frame differencing, and visualizing the results with bounding boxes. The code has been enhanced to classify motion regions by team based on dominant colors (red for Team A, blue for Team B).

Changes Made to the Starter Code Template
1. Frame Processor (frame_processor.py):
Functionality: Extracts frames from a video at a specified frame rate and resizes them to a standard resolution.

Changes: No significant changes were made to this file as it already met the requirements for video processing.

2. Motion Detector (motion_detector.py):
Functionality: Detects motion by comparing the current frame with the previous frame using frame differencing. Applies Gaussian blur to reduce noise and uses contour detection to identify significant motion areas.

Changes:

Added team classification based on the dominant color in the motion region (red for Team A, blue for Team B).

Modified the function to return bounding boxes along with team classification.

3. Visualizer (visualizer.py):
Functionality: Creates a visualization of the motion detection results by drawing bounding boxes around detected motion regions and saving the output as a video and individual frames.

Changes:

Added team-specific colors and labels for bounding boxes (red for Team A, blue for Team B).

Enhanced the visualization by adding team labels above the bounding boxes.

4. Main Script (main.py):
Functionality: Orchestrates the video processing, motion detection, and visualization steps.

Changes:

Modified the script to handle video files from a specified folder (videos) and create output directories based on the video name.

Added support for command-line arguments to specify the target FPS.

How to Run the Code
Prerequisites
Python 3.x

OpenCV (pip install opencv-python)

NumPy (pip install numpy)

Steps
Clone the repository:

bash
Copy
git clone <repository-url>
Place your video files in the videos folder.

Run the main script:

bash
Copy
python main.py --fps 5
The --fps argument specifies the target frames per second (default is 5).

The processed video and frames will be saved in the output directory under a subfolder named after the video file.

Approach and Design Decisions
Video Processing: Frames are extracted at a regular interval (default is 5 fps) and resized to a standard resolution (640x480) to ensure consistent processing.

Motion Detection: Frame differencing is used to detect motion. Gaussian blur is applied to reduce noise, and contours are filtered by area to ignore small movements.

Team Classification: The dominant color in the motion region is used to classify the team (red for Team A, blue for Team B).

Visualization: Bounding boxes are drawn around detected motion regions with team-specific colors and labels. The results are saved as a video and individual frames.

Challenges Encountered
Noise Reduction: Initial motion detection included a lot of noise. Applying Gaussian blur and filtering contours by area helped reduce false positives.

Team Classification: Determining the dominant color in a region was challenging due to varying lighting conditions. Using the HSV color space improved the classification accuracy.

Future Improvements
Advanced Motion Detection: Implement more sophisticated motion detection algorithms, such as optical flow, to improve accuracy.

Team Tracking: Extend the system to track players over multiple frames and provide more detailed statistics.

User Interface: Develop a graphical user interface (GUI) for easier interaction with the system.

Performance Optimization: Optimize the code for faster processing, especially for longer videos.

Conclusion
This project successfully implements a basic motion detection system for sports videos. It meets the requirements by processing video frames, detecting motion, and visualizing the results with team-specific bounding boxes. The code is well-organized, documented, and ready for further enhancements.


GitHub Repository: https://github.com/facurogala/Opencv-football

