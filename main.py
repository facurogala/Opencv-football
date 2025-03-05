import os
import argparse
import cv2
import numpy as np

from frame_processor import process_video
from motion_detector import detect_motion
from visualizer import visualize_results

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Sports Motion Detection")
    parser.add_argument("--fps", type=int, default=5, help="Target frames per second")
    return parser.parse_args()

def main():
    """Main function to run the motion detection pipeline."""
    # Parse arguments
    args = parse_args()

    # Get the first video file from the "videos" folder
    video_folder = "videos"
    video_files = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]
    if not video_files:
        print("No video files found in the 'videos' folder.")
        return

    video_path = os.path.join(video_folder, video_files[0])

    # Obtener el nombre del archivo de video sin la extensión
    video_filename = os.path.basename(video_path)
    video_name_without_extension = os.path.splitext(video_filename)[0]

    # Crear la ruta de salida basada en el nombre del video
    output_directory = os.path.join("output", video_name_without_extension)
    os.makedirs(output_directory, exist_ok=True)

    print(f"Processing video: {video_path}")

    # Step 1: Extract frames from video
    frames = process_video(video_path, args.fps)
    print(f"Extracted {len(frames)} frames")

    # Step 2: Detect motion in frames
    motion_results = []
    for i, frame in enumerate(frames):
        print(f"Processing frame {i + 1}/{len(frames)}")
        motion_boxes = detect_motion(frames, i)
        motion_results.append(motion_boxes)

    # Step 3: Visualize and save results
    visualize_results(frames, motion_results, output_directory)

    print(f"Processing complete. Results saved to {output_directory}")

if __name__ == "__main__":
    main()