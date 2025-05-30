# Face and License Plate Detection and Blurring

This project detects faces and car license plates in videos using a YOLO segmentation model. It segments and blurs these regions for privacy.

## How to Use

1. Add your video to the `video_in` folder.
2. Run the main script
3. Select the video when prompted.

The processed video will play after detection and blurring.

## Model Info
Model: `YOLOv8n-seg`

Face datasets: CHIP, LIP, ATR (https://github.com/Charleshhy/One-shot-Human-Parsing)

License plate dataset: Large License Plate Dataset (https://www.kaggle.com/datasets/fareselmenshawii/large-license-plate-dataset)

## Folders
`video_in/` — input videos (keep sample.mp4)

`video_out/` — processed output

`video_procesing/` — code for processing video