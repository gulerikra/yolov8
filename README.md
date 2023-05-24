# yolov8

1. ETİKETLEME İŞLEMİ

--> Etiketleme labelimg ile yapıldı.

https://pypi.org/project/labelImg/

--> Class isimlerini ayarlama

C:\Users\ikra\labelImg\data içerisindeki predefined_classes.txt dosyası class isimlerine göre düzenlenir.

![cdxs](https://github.com/gulerikra/yolov8/assets/62421679/63d308c2-2069-47ed-adcf-3a4ba18c9dc6)

--> Uygulamayı açma

![vcx](https://github.com/gulerikra/yolov8/assets/62421679/fe88538b-33f1-4b91-ab9d-668d036c527a)

--> Open Dir ile resimlerin bulunduğu klasör açılır.
 
--> Change Save Dir ile resimlerin .txt dosyalarının kaydedileceği konum seçilir.

--> YOLO seçeneği seçili olmalı

--> Create RectBox ile ilgili alan ve class ismi seçilir. 

--> Ardından save yapılır.

![aaaaaaaaaa](https://github.com/gulerikra/yolov8/assets/62421679/c7d8b9e5-c990-44b4-9da0-575fd03fa6c8)

-----------------------------------------------------------------

2. DATASET İÇİ KLASÖR OLUŞTURMA

![ii](https://github.com/gulerikra/yolov8/assets/62421679/754fd5c6-3709-4ca7-808d-12c48920ad2e)

--> Dataset içerisinde images ve label klasörü, images ve label klasörü içerisinde train ve val klasörleri olacak.

--> Train klasörü içerisinde dogru etiketli resimlerin %80, val klasöründe dogru etiketli resimlerin %20'si olmalı. Aynı 

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
