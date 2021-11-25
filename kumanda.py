import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TV8"],kanal="TV8"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Zaten Acık")
        else:
            time.sleep(1)
            print("Tv Açılıyor")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Zaten Kapalı")
            self.tv_durum = "Kapalı"
        else:
            time.sleep(1)
            print("Tv Kapanıyor")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır:'>'\nÇıkış: 'q' basınız")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses :", self.tv_ses)

            elif (cevap == ">"):
                if (self.tv_ses != 40):
                    self.tv_ses += 1
                    print("Ses :", self.tv_ses)

            else:
                print("Ses Güncellendi: ", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(3)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi...")
    def random_kanal(self):
        random_kanal = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[random_kanal]
        print(f"Seçilen kanal : {self.kanal}")

    def kanal_sayisi(self):
        print(len(self.kanal_listesi))

    def __str__(self):
        return "Tv Durum: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n.".format(self.tv_durum, self.tv_ses,
                                                                                          self.kanal_listesi,
                                                                                          self.kanal)


kumanda = Kumanda()

banner = """
    Televizyon Uygulaması

    1.Tv Aç
    2.Tv Kapat
    3.Tv Ses Ayarları
    4.Kanal Ekle
    5.Kanal Sayısı Öğrenme
    6.Rastgele Kanal Geçme
    7.Tv Bilgileri
    Çıkmak için 'q' basınız...
"""
print(banner)

while True:
    islem2=input("İşlem Seçiniz :")
    if (islem2=="q"):
        time.sleep(2)
        print("cikis yapiliyor.")
        break
    elif(islem2=="1"):
        kumanda.tv_ac()
    elif(islem2=="2"):
        kumanda.tv_kapat()
    elif(islem2=="3"):
        kumanda.ses_ayarları()
    elif(islem2=="4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak yazınız...")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem2=="5"):
        kumanda.kanal_sayisi()
    elif(islem2=="6"):
        kumanda.random_kanal()
    elif(islem2=="7"):
        print(kumanda)
    else:
        print("gecersiz islem")

