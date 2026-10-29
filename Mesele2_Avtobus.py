class Sernisin:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        self.novbeti = None


class Novbe:
    def __init__(self, ad):
        self.ad = ad
        self.bas = None      
        self.son = None      #
        self.olcu = 0

    def elave_et(self, ad, yas):
        yeni = Sernisin(ad, yas)
        if self.son is None:
            self.bas = self.son = yeni
        else:
            self.son.novbeti = yeni
            self.son = yeni
        self.olcu += 1

    def cixar(self):
        if self.bas is None:
            return None
        sernisin = self.bas
        self.bas = self.bas.novbeti
        if self.bas is None:
            self.son = None
        self.olcu -= 1
        return sernisin

    def bosdur(self):
        return self.bas is None

    def goster(self):
        print(f"\n{self.ad} ({self.olcu} nəfər):")
        if self.bas is None:
            print("   (boşdur)")
            return
        cari = self.bas
        sira = 1
        while cari is not None:
            print(f"   {sira}. {cari.ad} ({cari.yas} yaş)")
            cari = cari.novbeti
            sira += 1


class AvtobusDayanacagi:
    YAS_HEDDI = 65

    def __init__(self):
        self.yaslilar = Novbe("Yaşlılar növbəsi (prioritet, 65+)")
        self.diger = Novbe("Digər sərnişinlər növbəsi")

    def sernisin_elave_et(self, ad, yas):
        if yas >= self.YAS_HEDDI:
            self.yaslilar.elave_et(ad, yas)
            print(f"✔ {ad} ({yas} yaş) yaşlılar növbəsinə əlavə olundu.")
        else:
            self.diger.elave_et(ad, yas)
            print(f"✔ {ad} ({yas} yaş) digər növbəyə əlavə olundu.")

    def avtobusa_min(self):
        if not self.yaslilar.bosdur():
            s = self.yaslilar.cixar()
            print(f"🚌 {s.ad} ({s.yas} yaş) prioritetlə avtobusa mindi.")
        elif not self.diger.bosdur():
            s = self.diger.cixar()
            print(f"🚌 {s.ad} ({s.yas} yaş) avtobusa mindi.")
        else:
            print("Hər iki növbə boşdur.")

    def novbeleri_goster(self):
        print("\n========== Dayanacaq ==========")
        self.yaslilar.goster()
        self.diger.goster()
        print("===============================\n")

if __name__ == "__main__":
    dayanacaq = AvtobusDayanacagi()

    while True:
        print("1 - Sərnişin əlavə et")
        print("2 - Avtobusa mindir (prioritetlə)")
        print("3 - Növbələri göstər")
        print("4 - Nümunə məlumatları yüklə")
        print("0 - Çıxış")
        secim = input("Seçim (yalnız rəqəm): ").strip()

        if secim == "1":
            ad = input("Sərnişinin adı: ").strip()
            try:
                yas = int(input("Yaşı: ").strip())
                if yas <= 0:
                    print("Yaş müsbət olmalıdır.")
                else:
                    dayanacaq.sernisin_elave_et(ad, yas)
            except ValueError:
                print("Yaşı rəqəmlə yazın.")
        elif secim == "2":
            dayanacaq.avtobusa_min()
        elif secim == "3":
            dayanacaq.novbeleri_goster()
        elif secim == "4":
            dayanacaq.sernisin_elave_et("Aysel", 25)
            dayanacaq.sernisin_elave_et("Həsən", 70)
            dayanacaq.sernisin_elave_et("Leyla", 30)
            dayanacaq.sernisin_elave_et("Fatma", 68)
            dayanacaq.sernisin_elave_et("Elnur", 19)
        elif secim == "0":
            break
        else:
            print("Yanlış seçim, yalnız 0, 1, 2, 3 və ya 4 yazın.")
