# Xətti axtarış alqoritması
def linear_search(mektublar, kod):
    # çoxluqda/massivdə neçə element olduğunu müəyyən edirik.
    say = len(mektublar)

    # Addım 1: proqramlaşdırmada indeks 0 dan başladığı üçün 1ə yox 0la eyniləşdiririk.
    indeks = 0

    # Addım 2: indeks saydan kiçikdirsə axtarışa davam edirik
    while indeks < say:
        # Addım 3: cari indeksdəki elementin axtardığımız kod olub olmadığını yoxlayırıq
        if mektublar[indeks] == kod:
            # Addım 5: saymağa sıfırdan başladığımız üçün məktubun doğru nömrəsin tapmaq üçün üzərinə 1 gəlirik
            return indeks + 1
        # Addım
        indeks += 1

    # Addım 6: massivdə verilmiş kod üzrə heç bir məlumat tapılmadığı üçün proqramı sonlandırııq
    return "Məktub yoxdur"
