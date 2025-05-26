import os
import numpy as np
import cv2
from ultralytics import YOLO

def process_frames_with_yolo(model_path, input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    model = YOLO(model_path)

    frame_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

    for i, file_name in enumerate(frame_files):
        input_path = os.path.join(input_folder, file_name)
        original_img = cv2.imread(input_path)
        original_h, original_w = original_img.shape[:2]

        results = model(input_path, conf=0.2, verbose=False)
        result = results[0]

        if result.masks is not None:
            masks = result.masks.data.cpu().numpy()

            for mask in masks:
                mask_resized = cv2.resize(mask.astype(np.uint8), (original_w, original_h), interpolation=cv2.INTER_NEAREST)

                blurred_img = cv2.GaussianBlur(original_img, (81, 81), 0)

                mask_3ch = np.stack([mask_resized] * 3, axis=-1)

                original_img = np.where(mask_3ch == 1, blurred_img, original_img)

        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, original_img)


def video_images_to_model(video_title):
    input_frames = os.path.join(f"./video_out/{video_title}/images")
    output_frames = os.path.join(f"./video_out/{video_title}/model_output")
    model_path = "./debug_faces_and_car_pates_v1/yolov8n_ch_2_weight_decay_0_001/weights/best.pt"

    process_frames_with_yolo(model_path, input_frames, output_frames)
