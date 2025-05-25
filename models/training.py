from ultralytics import YOLO

def train_yolo():
    model = YOLO("yolov8n-seg.pt")

    model.train(
        data="../datasets/main/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        workers=8,
        save=True,
        device=0,
        name='yolov8n_ch_20_full_power',
        project='debug_faces_and_car_pates_v1',
        lr0=0.003,
        weight_decay=0.001,
    )


if __name__ == "__main__":
    train_yolo()