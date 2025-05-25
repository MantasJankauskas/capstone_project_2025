import os
import json
import shutil

from moviepy import ImageSequenceClip, AudioFileClip
from natsort import natsorted

def frames_to_video(video_title, frames_folder, audio_path, output_video_path, fps=30):
    os.makedirs(output_video_path, exist_ok=True)

    image_files = natsorted([
        os.path.join(frames_folder, f)
        for f in os.listdir(frames_folder)
        if f.endswith('.jpg')
    ])

    clip = ImageSequenceClip(image_files, fps=fps)


    if os.path.exists(audio_path):
        audio_clip = AudioFileClip(audio_path)
        clip.audio = audio_clip

    clip.write_videofile(f"{output_video_path}/{video_title}.mp4", codec='libx264', audio_codec='aac', logger=None)


def get_fps_from_json(json_path):
    with open(json_path, 'r') as f:
        video_info = json.load(f)

    fps = video_info.get("fps")
    return fps

def delete_old_files(frames_input, audio_input, info_input):
    shutil.rmtree(frames_input)
    os.remove(audio_input)
    os.remove(info_input)

def convert_images_to_video(video_title):
    frames_input = f"../video_out/{video_title}/model_output"
    audio_input = f"../video_out/{video_title}/{video_title}.mp3"
    info_input = f"../video_out/{video_title}/{video_title}_data.json"
    video_out = f"../video_out/{video_title}/final"

    frames_to_video(video_title, frames_input, audio_input, video_out, fps=get_fps_from_json(info_input))
    delete_old_files(frames_input, audio_input, info_input)
