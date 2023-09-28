class Baglama:
    ad = None
    kod = None
    adres = None

    def __init__(self, ad, kod, adres):
        self.ad = ad
        self.kod = kod
        self.adres = adres


class Stack:

    # bağlamaları yerləşdirəcəyimiz qutu
    qutu = None

    # qutunun sonuncu elementini göstərir
    # əgər -1 dirsə bu zaman qutunu boş hesab edəcəyik
    index = -1

    # yeni stack(dəstə)`nin/qutunun yaradılması.
    # say - dəyişənin qutumuza neçə bağlama əlavə edə biləcəyimizi göstərir
    def __init__(self, say):
        self.qutu = [None] * say
        self.index = -1

    # yeni bağlamanın qutuya əlavə olunması.(push)
    # Bağlamanı qutuya əlavə etməzdən öncə qutumuzda kifayət qədər yer
    # olub olmadığını yoxlayırıq
    def elave_et(self, baglama):
        # niyə index + 1? xatırlayan varmı? :)
        if (self.index + 1) == len(self.qutu):
            print("Qutu doludur. Yeni bağlama əlavə edilə bilməz.")
        else:
            self.index = self.index + 1
            self.qutu[self.index] = baglama

    # ən sonuncu əlavə olunmuş elementin silinməsi(pop)
    # silmə əməliyyatından öncə qutunun boş olub olmaması yoxlanılmalıdır
    # daha sonra ən üstəki bağlamanı götürürük.
    def sil(self):
        if self.index == -1:
            print('Qutu boşdur')
            return None
        else:
            # əvvəlcə qutuda ən üstəki bağlamanı götürürük, daha sonra isə
            # indexi 1 azaldırıq
            baglama = self.qutu[self.index]
            self.index = self.index - 1
            print('Sonuncu element siyahıdan silindi')
            return baglama

    # qutunun boş olub olmadığını yoxlayırıq(isEmpty)
    def bosdur(self):
        return self.index == -1

    # qutunun dolub olub olmaması yoxlanılır(isFull)
    def doludur(self):
        return self.index + 1 == len(self.qutu)

    # bu əməliyyat(peek) silmə əməliyyatına oxşayır. Tək fərq isə
    # silmədən fərqli olaraq bu zaman qutunun ən üstündəki bağlamanı silmirik
    # qutudan götürüb sonra yerinə qoyuruq
    def baxmaq(self):
        if self.index == -1:
            print('Qutu boşdur')
            return None

        return self.qutu[self.index]

    # qutumuzda neçə bağlama olduğu məlumatını verir.(size)
    def baglama_sayi(self):
        return self.index + 1