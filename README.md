# yolov8

Eğitim labelimg ile yapıldı. 

https://pypi.org/project/labelImg/

Etiketleme yapılırken:

C:\Users\ikra\labelImg\data içerisindeki predefined_classes.txt dosyası class isimlerine göre düzenlenir.

![asdd](https://user-images.githubusercontent.com/62421679/225256359-75e70d0d-f5da-482b-9285-0beb619af8bd.PNG)

Open Dir ile resimlerin bulunduğu klasör açılır.

Change Save Dir ile resimlerin .txt dosyalarının kaydedileceği konum seçilir.

yolo seçeneği seçili olmalı

![fdvs](https://user-images.githubusercontent.com/62421679/225256374-596ad0d9-6138-47be-be9c-c4950a8b5669.PNG)

Dataset içerisinde images ve label klasörü, images ve label klasörü içerisinde train ve val klasörleri olacak. 

Train klasörü içerisinde dogru etiketli resimlerin %80, val klasöründe dogru etiketli resimlerin %20'si olmalı. Aynı şekilde diğer class için de 80/20 şeklinde ayrılmalı.

Bu 80/20 oranı tercihe göre değişebilir.

Model eğitimi yapılırken:

yolov8.ipynb ve custom.yaml dosyaları kullanılacak
