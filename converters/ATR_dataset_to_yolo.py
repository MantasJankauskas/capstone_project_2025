import os
from glob import glob

import cv2
import numpy as np


def process_mask_with_unified_classes(mask_path, output_dir, visualization_dir, class_mapping):
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    if mask is None:
        return

    height, width = mask.shape
    filename = os.path.splitext(os.path.basename(mask_path))[0]
    output_path = os.path.join(output_dir, filename + ".txt")

    visualization_image = np.zeros((height, width, 3), dtype=np.uint8)

    with open(output_path, 'w') as f:
        for gray_value, class_id in class_mapping.items():
            class_mask = (mask == gray_value).astype(np.uint8) * 255
            num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(class_mask, connectivity=8)

            for label in range(1, num_labels):
                instance_mask = (labels == label).astype(np.uint8) * 255

                contours, _ = cv2.findContours(instance_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    contour = cv2.approxPolyDP(contour, 1, closed=True)

                    if len(contour) < 3:
                        continue

                    normalized_coords = []
                    for point in contour:
                        x = point[0][0] / width
                        y = point[0][1] / height
                        normalized_coords.extend([x, y])

                    line = f"{class_id} " + " ".join(f"{coord:.6f}" for coord in normalized_coords)
                    f.write(line + "\n")

                    contour_points = contour.squeeze()

                    cv2.fillPoly(visualization_image, [contour_points], (0, 200, 200))
                    cv2.polylines(visualization_image, [contour_points], isClosed=True, color=(255, 255, 255),
                                  thickness=5)

    visualization_path = os.path.join(visualization_dir, filename + "_test.jpg")
    cv2.imwrite(visualization_path, visualization_image)


# original class mapping grayscale value to class id
class_mapping = {
    11: 0,
}

mask_dir = "../datasets/HumanParsingDataset/ATR/val/masks"
output_dir = "../datasets/HumanParsingDataset/ATR/val/labels"
visualization_dir = "../datasets/HumanParsingDataset/ATR/val/visualizations"

os.makedirs(output_dir, exist_ok=True)
os.makedirs(visualization_dir, exist_ok=True)

mask_paths = glob(os.path.join(mask_dir, "*.png"))
for mask_path in mask_paths:
    process_mask_with_unified_classes(
        mask_path,
        output_dir,
        visualization_dir,
        class_mapping
    )
