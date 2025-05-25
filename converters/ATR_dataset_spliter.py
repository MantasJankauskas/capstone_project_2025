import os
import shutil
import random
from sklearn.model_selection import train_test_split


def split_dataset(image_dir, mask_dir, output_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    os.makedirs(os.path.join(output_dir, 'train', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'train', 'masks'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'val', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'val', 'masks'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'test', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'test', 'masks'), exist_ok=True)

    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f)) and f.lower().endswith('.jpg')]

    base_names = [os.path.splitext(f)[0] for f in image_files]

    # check if masks exist
    valid_pairs = []
    for base in base_names:
        mask_file = base + '.png'
        if os.path.exists(os.path.join(mask_dir, mask_file)):
            valid_pairs.append(base)

    train_names, temp_names = train_test_split(valid_pairs, test_size=(val_ratio + test_ratio), random_state=1)
    val_names, test_names = train_test_split(temp_names, test_size=test_ratio / (val_ratio + test_ratio), random_state=1)

    def copy_files(names, split):
        for base in names:
            # copy image
            img_file = base + '.jpg'
            src_img = os.path.join(image_dir, img_file)
            dst_img = os.path.join(output_dir, split, 'images', img_file)
            shutil.copy(src_img, dst_img)

            # copy mask
            mask_file = base + '.png'
            src_mask = os.path.join(mask_dir, mask_file)
            dst_mask = os.path.join(output_dir, split, 'masks', mask_file)
            shutil.copy(src_mask, dst_mask)

    copy_files(train_names, 'train')
    copy_files(val_names, 'val')
    copy_files(test_names, 'test')

    print("\nDataset split done")



image_directory = "../datasets/HumanParsingDataset/ATR/JPEGImages"
mask_directory = "../datasets/HumanParsingDataset/ATR/SegmentationClassAug"
output_directory = "../datasets/HumanParsingDataset/ATR/"

split_dataset(image_directory, mask_directory, output_directory)