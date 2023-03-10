from ultralytics import YOLO
import os
from PIL import Image
model = YOLO("last1.pt") #last3

# Klasördeki dosya isimlerini al
folder_path = "C:\\Users\\ikra\\Pictures\\yolov8\\foto\\"
file_names = os.listdir(folder_path)

# Dosya isimleri üzerinden for döngüsü ile resimleri aç
for file_name in file_names:
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        file_path = os.path.join(folder_path, file_name)
        image = Image.open(file_path)

        de_out=model.predict(source=image, conf=0.4, show=False, device='cpu')

        if len(de_out) != 0:
            isCompress = 0
            for i in range(len(de_out[0])):
                boxes = de_out[0].boxes
                box = boxes[i]
                clsID =boxes.cls.numpy()[0]
                conf = box.conf.numpy()[0]
                bb = box.xyxy.numpy()[0]
                print(clsID)
