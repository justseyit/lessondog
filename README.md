# [EN]
# KUZEM Auto-Login and Lesson Date Check Bot with Python and Selenium (aka LessonDog)

LessonDog is designed for Kırıkkale University Online Education Portal (KUZEM).

## What can LessonDog do?

-LessonDog logs into the system for you, checks the upcoming lesson dates and prints them on the console screen for you.

## How to use LessonDog?

To use LessonDog, you must have the following installed on your computer:

-Google Chrome
-Chrome Web Driver compatible with your Google Chrome version
-Python
-Selenium

If you don't tick all the boxes, continue reading with the topic below. If you tick all the boxes, you can start using it. Open the `lessondog.py` file, edit the `usernameStr` and `passwordStr` variables according to your own credentials. You can now start the bot. After running it will ask you for how many lessons you have. Be sure not to enter this information incorrectly. Otherwise, the bot will malfunction or not work.

## How to check the requirements?

The version of Google Chrome you are using must be the same as the version of the `chromedriver.exe` file in the main folder where the `lessondog.py` file is located. Otherwise, you may get an error. In the specified folder, by default, there is a version of `89.0.4389.23` of the `chromedriver.exe` file. You can download the required version from [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### How to check Google Chrome Version?

1. Go to Chrome Options > Help > About Google Chrome

![Help](https://i.ibb.co/8cW5ZwK/image.png "Help")
![About Google Chrome](https://i.ibb.co/yWz5Wbf/image.png "About Google Chrome")
![Chrome Version](https://i.ibb.co/PxmgY8d/image.png "Chrome Version")

2. Make sure you have the appropriate `chromedriver.exe` file for your version of Google Chrome.

### How to Install Python and Selenium?

1. Download and install Python from [python.org](python.org). Complete setup successfully.
2. Open the terminal on your computer and enter the command `pip install selenium` and hit `enter`.
3. Wait for the installation to complete. After the installation is complete, you can close the terminal window.

You can now start using the bot.



# [TR]
# Python ve Selenium ile KUZEM Otomatik-Giriş ve Ders Zamanı Kontrol Botu (Diğer adıyla LessonDog)

LessonDog, Kırıkkale Üniversitesi Online Eğitim Portalı (KUZEM) için tasarlandı.

## LessonDog neler yapabilir?

-LessonDog, sizin yerinize sisteme giriş yaparak yaklaşan ders randevularını kontrol eder ve sizin için konsol ekranına yazdırır.

## LessonDog nasıl kullanılır?

LessonDog'u kullanabilmek için bilgisayarınızda şunlar yüklü olmalıdır:

-Google Chrome
-Google Chrome versiyonunuz ile uyumlu olan Chrome Web Driver
-Python
-Selenium

Gereksinimleri karşılamıyorsanız okumaya, aşağıdaki başlıkla devam edin. Eğer gereksinimleri karşılıyorsanız kullanmaya başlayabilirsiniz. `lessondog.py` dosyasını açın, `usernameStr` ve `passwordStr` değişkenlerini kendi bilgilerinize göre düzenleyin. Artık botu çalıştırabilirsiniz. Çalıştırdıktan sonra size, aldığınız ders sayısını soracaktır. Bu bilgiyi hatalı girmediğinizden emin olun. Aksi takdirde bot, hatalı çalışacaktır veya çalışmayacaktır.

## Gereksinimler nasıl kontrol edilir?

Kullandığınız Google Chrome versiyonu ile, `lessondog.py` dosyasının bulunduğu ana klasördeki `chromedriver.exe` dosyasının versiyonu aynı olmalıdır. Aksi takdirde hata alabilirsiniz. Belirtilen klasörde, varsayılan olarak `chromedriver.exe` dosyasının `89.0.4389.23` versiyonu bulunmaktadır. [Bu bağlantıdan](https://sites.google.com/a/chromium.org/chromedriver/downloads) size uygun olan versiyonu indirebilirsiniz.

### Google Chrome Versiyonunu Kontrol Etme:

1. Chrome Seçenekleri > Yardım > Google Chrome Hakkında yolunu izleyin.

![Yardım](https://i.ibb.co/8cW5ZwK/image.png "Yardım")
![Google Chrome Hakkında](https://i.ibb.co/yWz5Wbf/image.png "Google Chrome Hakkında")
![Chrome Versiyonu](https://i.ibb.co/PxmgY8d/image.png "Chrome Versiyonu")

2. Google Chrome versiyonunuza uygun `chromedriver.exe` dosyasına sahip olduğunuzdan emin olun.

### Python ve Selenium Kurulumu

1. [python.org](python.org) adresinden Python'u indirin ve kurun. Kurulumu başarılı bir şekilde tamamlayın.
2. Bilgisayarınızdan terminali açın ve `pip install selenium` komutunu girip `enter`'a basın.
3. Yüklemenin tamamlanmasını bekleyin. Yükleme bittikten sonra terminal penceresini kapatabilirsiniz.

Artık botu kullanmaya başlayabilirsiniz.