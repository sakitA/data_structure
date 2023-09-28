# İkili axtarış alqoritması
import math


def binary_search(mektublar, kod):
    # Addım 1: çoxluqda/massivdə neçə element olduğunu müəyyən edirik.
    say = len(mektublar)

    # Addım 2:
    sol_indeks = 0 # proqramlaşdırmada indeks 0 dan başladığı üçün 1ə yox 0la eyniləşdiririk.
    sag_indeks = say - 1 # saymağa 0dan başladığımız üçün sayı bir azaldırıq

    # Addım 3: sol_indeks sağ_indeksdən kiçikdirsə axtarışa davam edirik
    while sol_indeks <= sag_indeks:
        # Addım 4: orta indeksin hesablanması
        orta_indeks = math.floor((sol_indeks+sag_indeks) / 2)

        # Addım 5: cari indeksdəki elementin axtardığımız kod olub olmadığını yoxlayırıq
        if mektublar[orta_indeks] == kod:
            # saymağa sıfırdan başladığımız üçün məktubun doğru nömrəsin tapmaq üçün üzərinə 1 gəlirik
            return orta_indeks + 1
        elif mektublar[orta_indeks] < kod:
            sol_indeks = orta_indeks + 1
        else:
            sag_indeks = orta_indeks - 1

    # Addım 6: massivdə verilmiş kod üzrə heç bir məlumat tapılmadığı üçün proqramı sonlandırııq
    return "Məktub yoxdur"
