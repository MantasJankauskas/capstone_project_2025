import os
import random
import shutil
import glob

def copy_subset(input_root, output_root, percent=0.3):
    subsets = ['train', 'val']

    for subset in subsets:
        img_input_dir = os.path.join(input_root, 'images', subset)
        lbl_input_dir = os.path.join(input_root, 'labels', subset)

        img_output_dir = os.path.join(output_root, 'images', subset)
        lbl_output_dir = os.path.join(output_root, 'labels', subset)

        os.makedirs(img_output_dir, exist_ok=True)
        os.makedirs(lbl_output_dir, exist_ok=True)

        image_files = glob.glob(os.path.join(img_input_dir, "*.*"))

        valid_image_files = []
        for img_path in image_files:
            img_name = os.path.basename(img_path)
            name_no_ext, _ = os.path.splitext(img_name)
            lbl_path = os.path.join(lbl_input_dir, name_no_ext + ".txt")
            if os.path.exists(lbl_path):
                valid_image_files.append(img_path)

        sample_size = int(len(valid_image_files) * percent)
        selected_images = random.sample(valid_image_files, sample_size)

        for img_path in selected_images:
            img_name = os.path.basename(img_path)
            name_no_ext, _ = os.path.splitext(img_name)
            lbl_path = os.path.join(lbl_input_dir, name_no_ext + ".txt")

            shutil.copy(img_path, os.path.join(img_output_dir, img_name))
            shutil.copy(lbl_path, os.path.join(lbl_output_dir, name_no_ext + ".txt"))

    print(f"Copied {percent*100}% of images only with labels")

copy_subset(
    input_root="../datasets/car_plates",
    output_root="../datasets/debug_car_plates",
)
