# yolov8

1. ETİKETLEME İŞLEMİ

--> Etiketleme labelimg ile yapıldı.

https://pypi.org/project/labelImg/

--> Class isimlerini ayarlama

C:\Users\ikra\labelImg\data içerisindeki predefined_classes.txt dosyası class isimlerine göre düzenlenir.

![gfds](https://github.com/gulerikra/yolov8/assets/62421679/0edcad9d-ffa9-438d-b68e-1565d5949db0)

--> Uygulamayı açma

![vcx](https://github.com/gulerikra/yolov8/assets/62421679/9c2f757c-d771-42ee-b292-ec89c74bc881)

--> Open Dir ile resimlerin bulunduğu klasör açılır.
 
--> Change Save Dir ile resimlerin .txt dosyalarının kaydedileceği konum seçilir.

--> YOLO seçeneği seçili olmalı

--> Create RectBox ile ilgili alan ve class ismi seçilir. 

--> Ardından save yapılır.

![aaaaaaaaaa](https://github.com/gulerikra/yolov8/assets/62421679/69c5f26a-82e1-4e5c-a3d1-0022d892a5f1)

-----------------------------------------------------------------

2. DATASET İÇİ KLASÖR OLUŞTURMA

--> Dataset içerisinde images ve label klasörü, images ve label klasörü içerisinde train ve val klasörleri olacak.

--> Train klasörü içerisinde 'dogru' etiketli resimlerin %80, val klasöründe 'dogru' etiketli resimlerin %20'si olmalı. Aynı 

şekilde diğer class için de 80/20 şeklinde ayrılmalı.

--> Sonuç olarak tüm resimlerin %80’i train klasöründe, %20’si val klasöründe olmalı.

--> Bu 80/20 oranı tercihe göre değişebilir.

----------------------------------------------------------------------

3. MODEL EĞİTİMİ

--> yolov8.ipynb ve custom.yaml dosyaları kullanılacak.

--> Eğitim tamamlandıktan sonra best.pt ve last.pt isimli ağırlık dosyaları oluşur.

------------------------------------------------------------------------

4. MODELİ TEST ETME

--> yolov8_deneme.py koduna ağırlık dosyası ve örnek klasördeki resimleri vererek model test edilir.
