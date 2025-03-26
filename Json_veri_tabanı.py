import json
import re
import random
import time

class Site:
    def __init__(self):
        self.dongu = True
        self.veriler = self.verial()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1 ile 3 arası bir değer giriniz")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ile 3 arası bir değer giriniz")
        while True:
            try:
                secim = input("\nMerhaba. Beydan Sitesine Hoşgeldiniz.\n\nLütfen yapmak istediğiniz işlemi seçiniz...\n\n[1]- Giriş\n[2]- Kayıt\n[3]- Çıkış\n\n")
                kontrol(secim)
            except Exception as Hata:
                print("{}".format(Hata))
                time.sleep(3)
            else:
                break
        return secim

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("\nGiriş menüsüne yönlendiriliyorsunuz")
            for i in range(5):
                print(".",end="",flush=True)
                time.sleep(.5)
            time.sleep(.7)
            self.giris()

        if secim == "2":
            print("\nKayıt menüsüne yönlendiriliyorsunuz")
            for i in range(5):
                print(".",end="",flush=True)
                time.sleep(.5)
            time.sleep(.7)
            self.kayitol()

        if secim == "3":
            print("\nÇıkış gerçekleştiriliyor")
            for i in range(5):
                print(".",end="",flush=True)
                time.sleep(.5)
            time.sleep(.7)            
            self.cikis()

#-***-
#---Fonksiyonlar arası değer göndermeye örnek---

    def giris(self):
        while True:
            Kullanıcı_Adı = input("\nLütfen bir kullanıcı adı giriniz")
            Şifre = input("Lütfen şifrenizi giriniz")

            Sonuç = self.giriskontrol(Kullanıcı_Adı,Şifre)
            
            if Sonuç == True:
                self.girisbasarili()
                break

            else:
                self.girisbasarisiz()
                break

    def giriskontrol(self, Kullanıcı_Adı, Şifre):
        #-- herhangi bir return sonucuna ulaşıldığında döngü biter 
        try:
            self.veriler = self.verial()
            kullanıcılar = self.veriler["Kullanıcılar"]  # Burada KeyError yakalanabilir
            
            for kullanıcı in kullanıcılar:
                if kullanıcı["Kullanıcı_Adı"] == Kullanıcı_Adı and kullanıcı["Şifre"] == Şifre:
                    return True

                #elif kullanıcı["Kullanıcı_Adı"] == Kullanıcı_Adı and kullanıcı["Şifre"] != Şifre:
                #    print("\nŞifreniz bu Kullanıcı Adıyla uyuşmuyor. Lütfen tekrar deneyiniz.")
                #    return False  #-Kullanıcıya tekrar deneme hakki verir... 
        
        except KeyError: # Eğer "Kullanıcılar" anahtarı yoksa veya veri yapısı beklendiği gibi değilse
            
            print("Kullanıcı veritabanında kayıtlı kullanıcı bulunamadı.")
          
        return False


    def girisbasarili(self):
        print("\ngiriş kontol ediliyor")
        for i in range(5):
            print(".",end="",flush=True)
            time.sleep(.5)
            print("\nJson Veri Tabanına hoşgeldiniz ")
        time.sleep(.7)
        self.Sonuç = False
        self.dongu = False


    def girisbasarisiz(self):
        print("\ngiriş kontol ediliyor")
        for i in range(5):
            print(".",end="",flush=True)
            time.sleep(.5)
        time.sleep(.7)
        print("\nGiriş Başarısız")
        time.sleep(2)

        while True:
            kayıt_olma_seçimi = input("\nGirdiğiniz bilgilere ait bir hesap bulamadık. Kaydınız yok mu?\nKayıt olmak için -[1]\nAna menüye gitmek için -[2]\n")
            if kayıt_olma_seçimi == "1":
                print("\nKayıt menüsüne yönlendiriliyorsunuz...")
                for i in range(5):
                    print(".",end="",flush=True)
                    time.sleep(.5)
                time.sleep(.7)
                self.kayitol()
                return # Doğrudan ana döngüye dön
            elif kayıt_olma_seçimi == "2":
                print("\nAna menüye yönlendiriliyorsunuz...")
                for i in range(5):
                    print(".",end="",flush=True)
                    time.sleep(.5)
                time.sleep(.7)
                return # Doğrudan ana döngüye dön
            else:
                print("Lütfen geçerli bir seçim yapın.")



    def kayitol(self):
        def kayit_ka(Kullanıcı_Adı):
            if len(Kullanıcı_Adı) < 8:
                raise Exception("\nKullanıcı Adınız 8 karakterden fazla olmalı")
            if Kullanıcı_Adı.isalpha == False:
                raise Exception("\nKullanıcı Adınız sadece harflerden oluşabilir")
        while True:
            try:
                Kullanıcı_Adı = input("\n Lütfen bir Kullanıcı Adı giriniz")
                kayit_ka(Kullanıcı_Adı)
            except Exception as Hata:
                print(Hata)
            else:
                break

        def kayit_si(Şifre):
            Dogumtarihi = "2005"
            Karakterler = ["\@,\€,\+,\*,\?,\!"]
            if len(Şifre) < 8:
                raise Exception("\nŞifreniz 8 karakterden fazla olmalı")
            elif not re.search("[a-z]",Şifre):
                raise Exception(" en az 1 tane küçük harf olmalı")
            elif not re.search("[0-9]", Şifre):
                raise Exception(" en az 1 tane rakam girmelisin")
            elif not re.search(str(Karakterler), Şifre):
                raise Exception(" en az bir özel (\@,\€,\+,\*,\?,\!) karakter girmelisin")
            elif not re.search("[A-Z]", Şifre):
                raise Exception("en az 1 büyük harf girmelisin.")
            elif re.search(Dogumtarihi, Şifre):
                raise Exception("şifrene doğum tarihini ekleyemezsin")
            
        while True:
            try:
                Şifre = input("\n Lütfen bir Şifre giriniz")
                kayit_si(Şifre)
            except Exception as Hata:
                print(Hata)
            else:
                break
        
        def kayit_mail(Mail):
            if not re.search("@gmail.com" or "@hotmail.com", Mail):
                raise Exception("\n mailinizde '@gmail.com' ya da '@hotmail.com' ibaresi bulunmalıdır. ")
            
        while True:
            try:
                Mail = input("\n Mailinizi giriniz. ")
                kayit_mail(Mail)
            except Exception as Mail_hata:
                print(Mail_hata)
            else:
                break

        Mail_sonuc = self.mailvarmi(Mail)
        if Mail_sonuc == False:

            KullanıcıAdı_sonuc =self.kullaniciadivarmi(Kullanıcı_Adı)
            if KullanıcıAdı_sonuc == False:

                aktivasyon_kodu = self.aktivasyongonder()
                durum = self.aktivasyonkontrol(aktivasyon_kodu)
                while True:
                    if durum == True:
                        self.verikaydet(Kullanıcı_Adı,Şifre,Mail)
                        print("\n-- Kaydınız oluşturulmuştur --")
                        time.sleep(3)
                        return # Doğrudan ana döngüye dön
            
                    else:
                        print("Aktivasyon Kodunuz Yanlış")
                        time.sleep(5)
                        return # Doğrudan ana döngüye dön
            else:
                print("\nBu Kullanıcı Adı sistemde var...")
        else:
            print("\nBu Mail sistemde var...")

    def mailvarmi(self,Mail):
        self.veriler = self.verial()

        try:
            for mail in self.veriler["Kullanıcı"]:
                if mail["Mail"] == Mail:
                    return True
        except KeyError:
            return False
        return False
            
    def kullaniciadivarmi(self,Kullanıcı_Adı):
        self.veriler = self.verial()

        try:
            for kullanıcı_adı in self.veriler["Kullanıcı"]:
                if kullanıcı_adı["Kullanıcı_Adı"] == Kullanıcı_Adı:
                    return True
        except KeyError:
            return False
        return False
        
    def aktivasyongonder(self):
        with open("C:/Users/user/Desktop/Aktivasyon.txt","w",encoding="utf8") as Dosya:
            aktivasyon = str( random.randint(10000,99999))
            Dosya.write("Aktivasyon kodunuz:" + aktivasyon)

        return aktivasyon
    
    def aktivasyonkontrol(self,aktivasyon):
        aktivasyon_girilen = input("\nLütfen mailinize gelen aktivasyon kodunu giriniz.")
        if aktivasyon == aktivasyon_girilen:
            return True
        
        else:
            return False

    def verial(self):
        try:
            with open("C:/Users/user/Desktop/Kullanıcılar.json","r",encoding="utf8") as Dosya:
                veriler = json.load(Dosya)
        except FileNotFoundError:
            with open("C:/Users/user/Desktop/Kullanıcılar.json","w",encoding="utf8") as Dosya:
                Dosya.write("{}")
            with open("C:/Users/user/Desktop/Kullanıcılar.json","r",encoding="utf8") as Dosya:
                veriler = json.load(Dosya)
        return veriler
                
    def verikaydet(self,Kullanıcı_Adı,Şifre,Mail):
        self.veriler = self.verial()
        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcı_Adı":Kullanıcı_Adı,"Şifre":Şifre,"Mail":Mail})
        except KeyError:
            self.veriler["Kullanıcılar"] = list()
            self.veriler["Kullanıcılar"].append({"Kullanıcı_Adı":Kullanıcı_Adı,"Şifre":Şifre,"Mail":Mail})

        with open("C:/Users/user/Desktop/Kullanıcılar.json","w",encoding="utf8") as Dosya:
            json.dump(self.veriler,Dosya,ensure_ascii=False,indent=4)#-Türkçe karakter için

    def cikis(self):
        print("Siteden çıkılıyor...")
        time.sleep(3)
        self.dongu= False
        exit()




Sistem = Site()
while Sistem.dongu:
    Sistem.program()