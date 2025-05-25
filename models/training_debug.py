from ultralytics import YOLO

def train_yolo():
    model = YOLO("yolov8s-seg.pt")

    model.train(
        data="../datasets/debug/data.yaml",
        epochs=45,
        imgsz=640,
        batch=8,
        workers=8,
        save=True,
        device=0,
        name='yolov8s_ch_15_lr0_0_003_weight_decay_0_001',
        project='debug_faces_and_car_pates_v1',
        lr0=0.003,
        weight_decay=0.001,
    )

if __name__ == "__main__":
    train_yolo()