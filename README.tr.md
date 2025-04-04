# EmotionStoryBot  
Yüz ifadelerinize göre **duyguya uyumlu, dinamik hikâyeler** anlatan yaratıcı bir robot uygulaması!

Gerçek zamanlı duygu algılama için bir web kamerası ve isteğe bağlı robotik bir bileşen (örneğin bir kol veya LED’ler) kullanarak, bu proje hikâye anlatımını eşsiz ve etkileşimli bir deneyime dönüştürüyor.

---

## Özellikler

- **Duygu Algılama:** Web kamerası ile yüz ifadelerinizi (mutlu, üzgün, şaşkın vb.) analiz eder.  
- **Dinamik Hikâye Anlatımı:** Duygularınıza göre hikâyenin tonu, olayları veya temposu ayarlanır.  
- **Robotik Etkileşim:** İsteğe bağlı olarak küçük bir robot kolu veya LED’lerle hikâye anlarını "canlandırır".  
- **Sesli Anlatım:** Metinleri sesli şekilde anlatmak için metinden-konuşmaya motoru kullanır.  
- **Kişiselleştirilebilir:** Basit JSON veya metin formatında kendi hikaye şablonlarınızı ekleyebilirsiniz.

---

## Nasıl Çalışır?

1. Program başlatıldığında web kameranız açılır ve duygularınızı algılar.  
2. Bot bir hikâye anlatmaya başlar (örnek: *"Bir zamanlar cesur bir kaşif varmış..."*).  
3. Yüz ifadeleriniz hikâyeye yön verir:  
   - Kaşlar çatık mı? Hikâye teselli veren bir dönüş alır.  
   - Gülümsüyor musunuz? Hikâyede heyecan artar!  
4. Robot kolu sallanır veya LED’ler yanar (isteğe bağlı olarak).  
5. Hikâye, sizin son duygunuza göre son bulur.

---

## Gereksinimler

- **Python 3.8+**  
- Web kamerası (duygu algılama için)  
- İsteğe bağlı: Servo motorlar veya LED’lerle donatılmış Arduino / Raspberry Pi

---

## Kurulum

1. **Repoyu klonlayın**  
```bash
git clone https://github.com/sosyalrobot/EmotionStoryBot.git
cd EmotionStoryBot
```

2. **Bağımlılıkları yükleyin**  
```bash
pip install -r requirements.txt
```

Gerekli kütüphaneler: `opencv-python`, `deepface`, `pyttsx3`, `pyserial` (donanım için isteğe bağlı)

3. **Donanım Kurulumu (isteğe bağlı)**  
- Arduino veya Raspberry Pi’ye servo motor veya LED bağlayın.  
- Arduino kullanıyorsanız, `robot_control.ino` dosyasını cihaza yükleyin.

4. **Programı çalıştırın**  
```bash
python main.py
```

---

## Kullanım

- Script’i başlatın ve kameraya bakın.  
- Hikâyeyi dinleyin; mimiklerinize göre şekillenecektir.  
- `stories/` klasöründeki dosyaları düzenleyerek kendi hikayelerinizi yazabilirsiniz (aşağıya bkz).

---

## Proje Yapısı

```
EmotionStoryBot/
├── main.py                # Uygulamayı başlatan ana script
├── emotion_detector.py    # Duygu tespiti modülü
├── story_engine.py        # Hikâye üretim ve uyarlama mantığı
├── robot_control.py       # Robotik donanım kontrolü (isteğe bağlı)
├── stories/               # Örnek hikâye şablonları
│   ├── happy_story.json
│   └── adventure_story.json
├── requirements.txt       # Gereksinimler
└── README.md              # Bu dosya
```

---

## Hikâye Şablonları

Hikayeler `stories/` klasöründe JSON formatında saklanır. Örnek:

```json
{
  "title": "Cesur Kaşif",
  "base_story": "Bir zamanlar Alex adında cesur bir kaşif varmış.",
  "happy": "Alex, altın dolu bir hazine sandığı bulmuş!",
  "sad": "Alex, kaybolmuş bir yavru köpek bulmuş ve evine götürmeye karar vermiş.",
  "surprised": "Aniden gökyüzünde bir ejderha belirmiş!"
}
```

Kendinize özel hikayelerle deneyimi kişiselleştirin!

---

## Örnek Çıktı

```
EmotionStoryBot başlatılıyor...
Web kamerası aktif. Merhaba deyin!
[Duygu Algılandı: Mutlu]
"Alex, altın dolu bir hazine sandığı bulmuş!"
[Robot Kolu Sallanıyor]
"Yaşasın!"
```

---

## Katkıda Bulunma

Fork'layabilir, issue açabilir ya da pull request gönderebilirsiniz.  
Yeni özellik önerilerine açığız (örneğin çok dilli destek, grafik arayüz vs).

---

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

## Teşekkürler

- ❤️ ile geliştirildi: [sosyalrobot](https://github.com/sosyalrobot)  
- Gücünü OpenCV, DeepFace ve pyttsx3’den alır

---

## Yol Haritası

- [ ] Çok dilli hikaye desteği (örneğin Türkçe)  
- [ ] Hikâye oluşturmak için basit bir GUI  
- [ ] Hikaye oturumlarını video olarak dışa aktarma
