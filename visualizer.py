import os
import cv2
import numpy as np


def visualize_results(frames, motion_results, output_dir):
    """
    Create visualization of motion detection results.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        output_dir: Directory to save visualization results
    """
    # Create output directory for frames
    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    # Get dimensions for the output video
    height, width = frames[0].shape[:2]

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(output_dir, "motion_detection.mp4")
    video_writer = cv2.VideoWriter(video_path, fourcc, 5, (width, height))

    # Process each frame
    for i, frame in enumerate(frames):
        # Create a copy for visualization
        vis_frame = frame.copy()

        # Draw bounding boxes for motion regions
        if i > 0:  # Skip the first frame as it has no motion data
            for box in motion_results[i]:
                x, y, w, h, team_class = box

                # Choose color and label based on team classification
                if team_class == 0:
                    color = (0, 0, 255)  # Red for Team A
                    label = "Red Team"
                else:
                    color = (255, 0, 0)  # Blue for Team B
                    label = "Blue Team"

                # Draw rectangle around motion region
                cv2.rectangle(vis_frame, (x, y), (x + w, y + h), color, 2)

                # Add label above the rectangle
                cv2.putText(
                    vis_frame,
                    label,
                    (x, y - 10),  # Position the label above the rectangle
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,  # Font size
                    color,  # Text color (same as rectangle color)
                    1,  # Thickness
                )

        # Add frame number
        cv2.putText(
            vis_frame,
            f"Frame: {i}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        # Save frame as image
        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.jpg")
        cv2.imwrite(frame_path, vis_frame)

        # Write frame to video
        video_writer.write(vis_frame)

    # Release video writer
    video_writer.release()

    print(f"Visualization saved to {video_path}")
    print(f"Individual frames saved to {frames_dir}")