import torch
import ultralytics
from ultralytics import YOLO

# print(torch.cuda.is_available())
# print(ultralytics.checks())


if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.train(data='C:\\Users\\user\\PycharmProjects\\lecture\\roboflow\\Models-1\\data.yaml',
                imgsz=640, epochs=30, batch=4)  # batch=4 # device=0 gpu
