import cv2
import os
import json

from moviepy import VideoFileClip


def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: cannot open video.")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        filename = f"{frame_count:010d}.jpg"
        filepath = os.path.join(output_folder, filename)

        cv2.imwrite(filepath, frame)

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

def extract_audio(video_path, output_extra_data_path):
    clip = VideoFileClip(video_path)
    if clip.audio is not None:
        clip.audio.write_audiofile(output_extra_data_path, logger=None)

def extract_video_info(video_path, output_extra_data_path):
    clip = VideoFileClip(video_path)

    video_info = {
        "fps": clip.fps,
    }

    with open(output_extra_data_path, 'w') as f:
        json.dump(video_info, f, indent=4)

    clip.close()
    cv2.destroyAllWindows()

video_title = 'asd'
video_path = f"../video_in/{video_title}.mp4"
frames_output = f"../video_out/{video_title}/images"
audio_output = f"../video_out/{video_title}/{video_title}.mp3"
info_output = f"../video_out/{video_title}/{video_title}_data.json"

extract_frames(video_path, frames_output)
extract_audio(video_path, audio_output)
extract_video_info(video_path, info_output)