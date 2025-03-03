import cv2
import numpy as np


def detect_motion(frames, frame_idx, threshold=25, min_area=100):
    """
    Detect motion in the current frame by comparing with previous frame.

    Args:
        frames: List of video frames
        frame_idx: Index of the current frame
        threshold: Threshold for frame difference detection
        min_area: Minimum contour area to consider

    Returns:
        List of tuples containing bounding boxes and their team classification (0 for team A, 1 for team B)
    """
    # We need at least 2 frames to detect motion
    if frame_idx < 1 or frame_idx >= len(frames):
        return []

    # Get current and previous frame
    current_frame = frames[frame_idx]
    prev_frame = frames[frame_idx - 1]

    # Convert frames to grayscale
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    current_blur = cv2.GaussianBlur(current_gray, (5, 5), 0)
    prev_blur = cv2.GaussianBlur(prev_gray, (5, 5), 0)

    # Calculate absolute difference between frames
    frame_diff = cv2.absdiff(prev_blur, current_blur)

    # Apply threshold to highlight differences
    _, thresh = cv2.threshold(frame_diff, threshold, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area and get bounding boxes
    motion_boxes = []
    for contour in contours:
        if cv2.contourArea(contour) < min_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        # Extract the region of interest (ROI) from the current frame
        roi = current_frame[y:y + h, x:x + w]

        # Classify the color of the ROI
        team_class = classify_team(roi)

        # Append the bounding box and its team classification
        motion_boxes.append((x, y, w, h, team_class))

    return motion_boxes


def classify_team(roi):
    """
    Classify the team based on the dominant color in the ROI.

    Args:
        roi: Region of interest (a portion of the frame)

    Returns:
        0 for Team A (e.g., red), 1 for Team B (e.g., blue)
    """
    # Convert ROI to HSV color space
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define color ranges for Team A (red) and Team B (blue)
    lower_red = np.array([0, 100, 100])  # Lower range for red
    upper_red = np.array([10, 255, 255])  # Upper range for red
    lower_blue = np.array([100, 100, 100])  # Lower range for blue
    upper_blue = np.array([130, 255, 255])  # Upper range for blue

    # Create masks for each color
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Count the number of pixels for each color
    red_pixels = cv2.countNonZero(mask_red)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Classify based on the dominant color
    if red_pixels > blue_pixels:
        return 0  # Team A (red)
    else:
        return 1  # Team B (blue)