import datetime

# Tarihi al
tarih = datetime.date.today().strftime("%d.%m.%Y")

# Dosyayı aç ve tarihi dosyaya yaz
with open("info.txt", "a", encoding="utf-8") as dosya:
    dosya.write(tarih + "\n")

while True:
    # Kullanıcıdan giriş iste
    girdi = input("Bir girdi girin (Çıkmak için 'q' tuşuna basın): ")

    # Çıkış koşulunu kontrol et
    if girdi.lower() == "q":
        # Ayırıcı çizgiyi dosyaya yaz ve döngüden çık
        with open("info.txt", "a", encoding="utf-8") as dosya:
            dosya.write("---------------\n")
        break

    # Dosyayı aç ve girişi dosyaya yaz
    with open("info.txt", "a", encoding="utf-8") as dosya:
        dosya.write(girdi + "\n")

    print("Girdi kaydedildi.")

print("Program sonlandırıldı.")
