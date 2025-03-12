from ultralytics import YOLO
import cv2

model = YOLO('../YOLO-weights/yolov8l.pt')
results = model("Images/Bunch of cars.png", show=True)
cv2.waitKey(0)
