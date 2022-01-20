
# **Yemeksepeti Python Bootcamp Fourth Homework**
- This repo is prepared for **the fourth assignment of Yemeksepeti Python Bootcamp**. You can find the details of the assignment under the "**Homework Description**" heading at the bottom of the Readme page.

## **Overview**

In short, the homework is about **parsing the json** file containing user information in accordance with **Regular Expression** and certain rules, using the **OOP paradigm** effectively and **saving it to the database**.


## **Libraries**

- `sqlite` for database
- `json` for json file operations
- `re` for regular expressions
- `geocoder` for getting location
- `date` for getting current date time

## **Folder Structure**

  
    ├── constants                       # Constant file that includes all strings etc.
    |   └── messages.py                 # Includes all messages
    |                                       
    ├── helpers                         # Helper file includes all main functionality
    │   ├── database_helper.py          # Database functions
    │   ├── file_helper.py              # File operations
    |   ├── location_helper.py          # Location functions
    │   └── regex_helper.py             # Regular expression functions
    |
    ├── models                          # Models file includes data model
    │   └── user.py                     # User data model
    |
    ├── dataregex.db                    # Database file
    ├── dataregex.json                  # Json file includes all informations
    ├── main.py                         # Main 
    ├── README.md                       # Readme


## **UML Class Diagram**
![UML](https://i.hizliresim.com/ctxhqvo.png)

<br/>
<br/>


## **Example Database Table**
![DB](https://i.hizliresim.com/cvh60uy.png)


<br/>


# **Homework Description**

Bu repository patika.dev 153. Yemeksepeti Python Web Development Bootcamp için ödev detaylarını paylaşmak üzere tema olarak hazırlanmıştır. 

Repository içerisinde yer alan `dataregex.json` dosyada yer alan kayıtların incelenerek aşağıdaki kriterlere uygun olarak bir veritabanına kaydedilmesi beklenmektedir. 
1. Veritabanı "dataregex.db" adında bir sqlite veritabanı olacaktır.
2. Veritabanı içerisindeki tablo her seferinde yeniden oluşturulmalı farklılık olarak aktarım zamanı tablo adının yanına eklenmelidir. örn : data_20221208
3. Tablo aşağıdaki sütunları içermelidir.
  - email (eposta adresi)
  - username (kullanıcı adı)
  - isimsoyisim (isim soyisim)
  - emailuserlk (e posta kullanıcı adını ya da bir bölümünü (en az 3 harf) içeriyor mu 1/0)
  - usernamelk (kullanıcı adı ile kullacının isim ya da soyisminin bir bölümünü içeriyor mu 1/0)
  - dogumyil (Doğum Yılı)
  - dogumay  (Doğum Ayı)
  - dogumgun (Doğum Günü)
  - ulke (opsiyonel olarak bir servise gönderdiğiniz lokasyon bilgisi doğrultusunda gelen ülke bilgisinin kaydedilmesi) ya da (adres bilgisi içerisinde yer alan şehir ismi kaydedilebilir)
  - ap (Kullanıcının Aktif ya da Pasif durumda olması 1/0 Default => 1)
4. Program OOP paradigması kullanılarak yazılmalıdır. diğer dosyalardan import edilebilecek bir sınıf olarak kaydedilmelidir.
5. oluşturulacak bir main.py dosyası çalıştırılırken;
   - `--file` parametresi ile json dosyasının erişim adresini alacaktır.
   - `--db` parametresi ile veritabanı erişim adresi belirlenecektir. 

Kriterler
1. Repository olarak paylaşıldı mı?
2. Veritabanı oluşturulmuş mu?
3. Kod çalıştırıldığında aynı formatta ki farklı veriler veritabanına yeni bir tablo olarak kaydediliyor mu?
4. Program OOP paradigmasına uygun yazılmış mı?
5. main.py dosyası parametrelerle sağlıklı çalışıyor mu? parametre girilmediğinde bilgi vererek kullanıcıyı yönlendiriyor mu?
  
