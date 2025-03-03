import cv2
import numpy as np


def process_video(video_path, target_fps=5, resize_dim=(640, 480)):
    """
    Extract frames from a video at a specified frame rate.

    Args:
        video_path: Path to the video file
        target_fps: Target frames per second to extract
        resize_dim: Dimensions to resize frames to (width, height)

    Returns:
        List of extracted frames
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    # Get video properties
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate frame interval for the target FPS
    frame_interval = max(1, int(original_fps / target_fps))

    # Extract frames
    frames = []
    frame_index = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Only keep frames at the target frame rate
        if frame_index % frame_interval == 0:
            # Resize frame
            if resize_dim:
                frame = cv2.resize(frame, resize_dim)
            frames.append(frame)

        frame_index += 1

    # Release video capture
    cap.release()

    return frames
