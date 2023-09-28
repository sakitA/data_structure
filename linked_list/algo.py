class Baglama:
    def __init__(self, vetendas, adres):
        self.vetendas = vetendas
        self.adres = adres
        self.novbeti_baglama = None

    def __str__(self) -> str:
        return f'Vətəndaş: {self.vetendas}, Adres: {self.adres}'


ilk_baglama = None


def ElaveEt(melumat):
    global ilk_baglama

    vetendas = melumat['vetendas']
    adres = melumat['adres']
    yeni_baglama = Baglama(vetendas, adres)

    bir_evvelki_baglama = None
    cari_baglama = ilk_baglama

    if ilk_baglama:
        while cari_baglama:
            if cari_baglama.adres > adres:
                break
            elif cari_baglama.novbeti_baglama:
                bir_evvelki_baglama = cari_baglama
                cari_baglama = cari_baglama.novbeti_baglama
            else:
                cari_baglama.novbeti_baglama = yeni_baglama
                return

        if cari_baglama == ilk_baglama:
            yeni_baglama.novbeti_baglama = ilk_baglama
            ilk_baglama = yeni_baglama
        else:
            yeni_baglama.novbeti_baglama = cari_baglama
            bir_evvelki_baglama.novbeti_baglama = yeni_baglama
    else:
        ilk_baglama = yeni_baglama


def Silme(melumat):
    global ilk_baglama

    if ilk_baglama:
        vetendas = melumat['vetendas']
        adres = melumat['adres']

        bir_evvelki_baglama = None
        cari_baglama = ilk_baglama

        while cari_baglama:
            if cari_baglama.vetendas == vetendas and cari_baglama.adres == adres:
                break
            elif cari_baglama.novbeti_baglama:
                bir_evvelki_baglama = cari_baglama
                cari_baglama = cari_baglama.novbeti_baglama
            else:
                return

        if cari_baglama == ilk_baglama:
            ilk_baglama = cari_baglama.novbeti_baglama
        else:
            bir_evvelki_baglama.novbeti_baglama = cari_baglama.novbeti_baglama

        cari_baglama = None

def CapEt():
    baglama = ilk_baglama
    while baglama:
        print(baglama)
        baglama = baglama.novbeti_baglama


if __name__ == "__main__":
    ElaveEt({'vetendas': "Nizami Gəncəvi", 'adres': 3})
    ElaveEt({'vetendas': "Məhəmməd Fizuli", 'adres': 9})
    ElaveEt({'vetendas': 'Qara Qarayev', 'adres': 4})
    ElaveEt({'vetendas': 'Xurşudbanu Natəvan', 'adres': 2})
    ElaveEt({'vetendas': 'Nigar Rəfibəyli', 'adres': 10})

    CapEt()
    print()
    #Silme({'vetendas': 'Xurşudbanu Natəvan', 'adres': 2})
    #Silme({'vetendas': 'Qara Qarayev', 'adres': 4})
    #Silme({'vetendas': 'Nigar Rəfibəyli', 'adres': 10})

    CapEt()


def mektubu_oxu(mektub:str):
    for herf in mektub:
        print(herf)
