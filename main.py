import os

from helpers.loader import Loader
from video_procesing.images_to_model import video_images_to_model
from video_procesing.images_to_video import convert_images_to_video
from video_procesing.video_player import play_video
from video_procesing.video_to_images import process_video_to_images

def get_video_inputs():
    video_folder = "./video_in"
    video_files = [f for f in os.listdir(video_folder) if f.lower().endswith('.mp4')]

    if not video_files:
        print("No video files found in the folder.")
        exit()


    print("Select a video file:")
    for i, file in enumerate(video_files):
        print(f"{i + 1}. {file}")

    print("------------------------------------")

    return video_files

def get_user_input(video_files):
    while True:
        try:
            choice = int(input("Enter the number of the video file: "))
            if 1 <= choice <= len(video_files):
                selected_video = video_files[choice - 1]
                print(f"You selected: {selected_video}")
                return selected_video
            else:
                print("Invalid number, try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    video_inputs = get_video_inputs()
    user_input = get_user_input(video_inputs)

    file_name = os.path.splitext(user_input)[0]

    loader = Loader("Processing video...")
    loader.start()

    process_video_to_images(file_name)
    video_images_to_model(file_name)
    convert_images_to_video(file_name)

    loader.stop()

    play_video(file_name)


