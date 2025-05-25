import os
import shutil
import glob

def merge_datasets(plate_img_dir, plate_label_dir, main_img_dir, main_label_dir):
    os.makedirs(main_img_dir, exist_ok=True)
    os.makedirs(main_label_dir, exist_ok=True)

    for img_file in glob.glob(os.path.join(plate_img_dir, "*.jpg")):
        shutil.copy(img_file, os.path.join(main_img_dir, os.path.basename(img_file)))

    for label_file in glob.glob(os.path.join(plate_label_dir, "*.txt")):
        shutil.copy(label_file, os.path.join(main_label_dir, os.path.basename(label_file)))


for split in ['train', 'val']:
    merge_datasets(
        plate_img_dir = f"../datasets/car_plates/images/{split}",
        plate_label_dir = f"../datasets/car_plates/labels/{split}",
        main_img_dir = f"../datasets/main/images/{split}",
        main_label_dir = f"../datasets/main/labels/{split}"
    )
