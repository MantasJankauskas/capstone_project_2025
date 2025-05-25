import os
import shutil

def copy_files(src_dirs, dst_dir):
    for src_dir in src_dirs:
        if os.path.exists(src_dir):
            for root, _, files in os.walk(src_dir):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        src_file = os.path.join(root, file)
                        dst_file = os.path.join(dst_dir, file)
                        shutil.copy(src_file, dst_file)

image_sources = {
    'train': [
        '../datasets/HumanParsingDataset/ATR/test/images',
        '../datasets/HumanParsingDataset/CIHP/Training/Images',
        '../datasets/HumanParsingDataset/LIP/TrainVal_images/train_images'
    ],
    'val': [
        '../datasets/HumanParsingDataset/ATR/val/images',
        '../datasets/HumanParsingDataset/CIHP/Validation/Images',
        '../datasets/HumanParsingDataset/LIP/TrainVal_images/val_images'
    ]
}

label_sources = {
    'train': [
        '../datasets/HumanParsingDataset/ATR/train/labels',
        '../datasets/HumanParsingDataset/CIHP/Training/labels',
        '../datasets/HumanParsingDataset/LIP/TrainVal_parsing_annotations/train/labels'
    ],
    'val': [
        '../datasets/HumanParsingDataset/ATR/val/labels',
        '../datasets/HumanParsingDataset/CIHP/Validation/labels',
        '../datasets/HumanParsingDataset/LIP/TrainVal_parsing_annotations/val/labels'
    ]
}

base_dest = '../datasets/main'
image_dest = os.path.join(base_dest, 'images')
label_dest = os.path.join(base_dest, 'labels')

for split in ['train', 'val']:
    os.makedirs(os.path.join(image_dest, split), exist_ok=True)
    os.makedirs(os.path.join(label_dest, split), exist_ok=True)

# copy images
for split, src_dirs in image_sources.items():
    dst_dir = os.path.join(image_dest, split)
    copy_files(src_dirs, dst_dir)

# copy labels
for split, src_dirs in label_sources.items():
    dst_dir = os.path.join(label_dest, split)
    copy_files(src_dirs, dst_dir)

print("Images and labels copied")
