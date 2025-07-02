# 🎲 Dice Game

## 🚀 Amaç  
Bu proje, Python komutlarını öğrenmeye çalışanlar için yazılmış basit bir zar atma oyunudur. Kullanıcı tek veya çift zarla atış yapabilir. Komut satırı üzerinden seçim yaparak rastgele sayı üretimi ile etkileşim kurar.

## 🛠️ Kullanılan Teknolojiler  
- Python 2.7  
- `random` kütüphanesi

## 📸 Örnek Çıktı

–dice–
for one dice press 1, for two dice press 2: 2
[3, 6]
try again?(yes or anything else)yes
for one dice press 1, for two dice press 2: 1
[4]
try again?(yes or anything else)no
thanks for playing!

## 📦 Kurulum
```bash
git clone https://github.com/masaldede/dice-game.git
cd dice-game
python dice.py

Not: Python 3 kullanıyorsan print ve raw_input satırlarını güncellemen gerekebilir. (Python 3 uyumlu versiyon yakında eklenebilir.)

💡 Kullanım Örneği
# Terminalde çalıştırmak yeterlidir:
python dice.py

🗺️ Yol Haritası / Öğrendiklerim
	•	random.randint() ile rastgele sayı üretimi
	•	Liste mantığı ile çoklu zar kullanımı
	•	Koşullu döngüler (while, if) ve kullanıcı girdisi alma
	•	Bir sonraki adım: Python 3’e dönüştürmek ve arayüz eklemek
