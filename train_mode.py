from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")  # or yolov8s.pt or any custom model

    model.train(
        data="roboflow/data.yaml",
        epochs=100 ,
        imgsz=1280, 
        
        batch=8,
        name="yolov8-highres",
        project="sign-language"
    )

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
