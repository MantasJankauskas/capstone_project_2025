import os

def clean_dataset(split):
    image_folder = os.path.join(images_dir, split)
    label_folder = os.path.join(labels_dir, split)

    image_files = os.listdir(image_folder)

    for image_file in image_files:
        image_name, _ = os.path.splitext(image_file)
        label_path = os.path.join(label_folder, f"{image_name}.txt")

        # Check if label exists
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                contents = file.read()
                if not contents:
                    os.remove(label_path)
                    os.remove(os.path.join(image_folder, image_file))
        else:
            os.remove(os.path.join(image_folder, image_file))

base_path = '../datasets/main'
images_dir = os.path.join(base_path, 'images')
labels_dir = os.path.join(base_path, 'labels')

for split in ['train', 'val']:
    clean_dataset(split)

print("Dataset cleaned")
