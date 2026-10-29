class Musteri:
    def __init__(self, ad, derman):
        self.ad = ad
        self.derman = derman
        self.novbeti = None


class AptekNovbesi:
    def __init__(self):
        self.bas = None      
        self.son = None      
        self.olcu = 0

    def novbeye_elave_et(self, ad, derman):
        yeni = Musteri(ad, derman)
        if self.son is None:          
            self.bas = self.son = yeni
        else:
            self.son.novbeti = yeni
            self.son = yeni
        self.olcu += 1
        print(f"✔ {ad} növbəyə əlavə olundu (dərman: {derman}).")

    def ilk_musteriye_xidmet(self):
        """İlk müştərini xidmət edib növbədən çıxarır. O(1)"""
        if self.bas is None:
            print("Növbə boşdur.")
            return None
        musteri = self.bas
        self.bas = self.bas.novbeti
        if self.bas is None:          # növbə boşaldı
            self.son = None
        self.olcu -= 1
        print(f"✔ {musteri.ad} dərmanını ({musteri.derman}) aldı və növbədən çıxdı.")
        return musteri

    def novbeni_goster(self):
        if self.bas is None:
            print("Növbə boşdur.")
            return
        print(f"\n--- Növbə ({self.olcu} müştəri) ---")
        cari = self.bas
        sira = 1
        while cari is not None:
            print(f"{sira}. {cari.ad} — {cari.derman}")
            cari = cari.novbeti
            sira += 1
        print("-----------------------------\n")

if __name__ == "__main__":
    novbe = AptekNovbesi()

    while True:
        print("1 - Növbəyə müştəri əlavə et")
        print("2 - İlk müştərini xidmət et (çıxar)")
        print("3 - Bütün növbəni göstər")
        print("4 - Nümunə məlumatları yüklə")
        print("0 - Çıxış")
        secim = input("Seçim (yalnız rəqəm): ").strip()

        if secim == "1":
            ad = input("Müştərinin adı: ").strip()
            derman = input("Dərmanın adı: ").strip()
            novbe.novbeye_elave_et(ad, derman)
        elif secim == "2":
            novbe.ilk_musteriye_xidmet()
        elif secim == "3":
            novbe.novbeni_goster()
        elif secim == "4":
            novbe.novbeye_elave_et("Aysel", "Paracetamol")
            novbe.novbeye_elave_et("Elnur", "Ibuprofen")
            novbe.novbeye_elave_et("Leyla", "Vitamin C")
        elif secim == "0":
            break
        else:
            print("Yanlış seçim, yalnız 0, 1, 2, 3 və ya 4 yazın.")
