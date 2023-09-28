class Baglama:
    ad = None
    kod = None
    adres = None

    def __init__(self, ad, kod, adres):
        self.ad = ad
        self.kod = kod
        self.adres = adres


class Element:
    # bağlama haqqında məlumat
    data: Baglama = None

    # sonrakı element haqqında məlumat
    novbeti: 'Element' = None

    def __init__(self, baglama):
        self.data = baglama
        self.novbeti = None


class Queue:
    # sıranın ilk elementi
    ilk: Element = None

    #sıranın son elementi
    son: Element = None

    # yeni elementin sıraya əlavə edilməsi
    def siraya_elave_et(self, baglama):
        # əgər sırada başqa element varsa həmin elementin növbəti elementi olaraq əlavə edirik
        element = Element(baglama)
        if self.son:
            self.son.novbeti = element

        # və yeni elementimiz sıradakı sonuncu element olur
        self.son = element

        # əgər sıramız boşdursa bu elementin sıranın ilk elementi olacaq
        if not self.ilk:
            self.ilk = element

    # sıranın ilk elementin oxuyub sıradan çıxardırıq və növbəti element sıranın ilk elementi olur
    def siradan_sil(self):
        cari_baglama = None
        # sıra doludursa
        if self.ilk:
            # ilk öncə məlumatı oxuyuruq
            cari_baglama = self.ilk.data

            # sıradkı elementi sıranın ilk elementi olaraq təyin edirik
            self.ilk = self.ilk.novbeti

        if not self.ilk:
            # sıra boşdur
            self.son = None

        return cari_baglama

    # baxmaq əməliyyatı silmə əməliyyatından onunla fərqlənir ki, bu əməliyyat zamanı sırada heç bir dəyişiklik baş vermir
    def baxmaq(self):
        if self.ilk:
            print(self.ilk.data)
        else:
            print("Siyahı boşdur")

    # sıranın boş olub olmadığını yoxlayırıq. Əgər son element yoxdursa bu sıranın boş olduğunu göstərir
    def bosdur(self):
        return self.son == None