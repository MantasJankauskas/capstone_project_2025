import os


def convert_bbox_to_segmentation(bbox_line):
    parts = bbox_line.strip().split()

    if len(parts) != 5:
        return None

    class_id = 1
    x_center, y_center, width, height = map(float, parts[1:])

    # Calculate corner points
    x1 = x_center - width / 2
    y1 = y_center - height / 2

    x2 = x_center + width / 2
    y2 = y_center - height / 2

    x3 = x_center + width / 2
    y3 = y_center + height / 2

    x4 = x_center - width / 2
    y4 = y_center + height / 2

    return f"{class_id} {x1:.6f} {y1:.6f} {x2:.6f} {y2:.6f} {x3:.6f} {y3:.6f} {x4:.6f} {y4:.6f}"


def convert_labels_in_folder(folder_path):
    files_names = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    for i, file_name in enumerate(files_names):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r') as f:
            lines = f.readlines()

        new_lines = [convert_bbox_to_segmentation(line) for line in lines]
        new_lines = [line for line in new_lines if line is not None]

        with open(file_path, 'w') as f:
            f.write("\n".join(new_lines))


convert_labels_in_folder("../datasets/car_plates/labels/train")
convert_labels_in_folder("../datasets/car_plates/labels/val")
