# 🎲 Dice Game

## 🚀 Amaç  
Bu proje, Python öğrenmeye yeni başlayanlar için yazılmış basit bir zar atma oyunudur. Kullanıcı tek veya çift zarla atış yapabilir. Komut satırında rastgelelik ve kullanıcı etkileşimini anlamak için idealdir.

## 🛠️ Kullanılan Teknolojiler  
- Python 3.x  
- `random` kütüphanesi (yerleşik)

## 📸 Örnek Çıktı
You rolled a 5!
You rolled a 3 and 6! Total: 9

## 📦 Kurulum
```bash
git clone https://github.com/masaldede/dice-game.git
cd dice-game
python dice.py

from dice import roll_dice
roll_dice(two_dice=True)

🗺️ Yol Haritası / Öğrendiklerim
	•	random.randint() ile rastgele sayı üretme
	•	Tek/çift zar mantığı ve fonksiyon yapısı
	•	Bir sonraki adım: Basit arayüz (Tkinter/Streamlit) eklemek
