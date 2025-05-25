import os
import shutil

def process_split(split):
    image_dir = os.path.join(base_input_dir, 'images', split)
    label_dir = os.path.join(base_input_dir, 'labels', split)
    output_image_dir = os.path.join(base_output_dir, 'images', split)
    output_label_dir = os.path.join(base_output_dir, 'labels',split)

    for label_file in os.listdir(label_dir):
        if not label_file.endswith('.txt'):
            continue

        label_path = os.path.join(label_dir, label_file)
        with open(label_path, 'r') as f:
            lines = f.readlines()

        filtered_lines = []
        for line in lines:
            if not line.startswith(f"{class_id_to_remove} "):
                filtered_lines.append(line + '\n')

        if filtered_lines:
            new_label_path = os.path.join(output_label_dir, label_file)
            with open(new_label_path, 'w') as f:
                f.writelines(filtered_lines)

            image_name = os.path.splitext(label_file)[0] + '.jpg'
            image_path = os.path.join(image_dir, os.path.splitext(label_file)[0] + '.jpg')
            
            if os.path.exists(image_path):
                shutil.copy(image_path, os.path.join(output_image_dir, os.path.basename(image_path)))
                break


base_input_dir = r"C:\Users\mjank\OneDrive\Documents\FilteringData\datasets\debug"
base_output_dir = r"C:\Users\mjank\OneDrive\Documents\FilteringData\datasets\debug_only_faces"
splits = ['train', 'val']
class_id_to_remove = 1

for split in splits:
    os.makedirs(os.path.join(base_output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(base_output_dir, 'labels', split), exist_ok=True)

for split in splits:
    process_split(split)
    print("Cleanup done")
