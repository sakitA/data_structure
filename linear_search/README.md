Fərz edin ki, əyalətlərin birində poçt offisində işləyirsiniz. Əlinizdə çoxlu sayda məktub var. Vətəndaşlar poçt
ofisinə yaxınlaşıb adlarına məktub olub olmadığını soruşurlar. Bu vətəndaşın adına məktub olub olmadığını 
necə yoxlayarsınız? Təbii mövcüd bütün məktublara baxar və əgər sizə müraciət edən vətəndaşın adına uyğun bir
məktub tapsanız onu vətəndaşa təqdim edər, tapmasanız bu zaman vətəndaşa onun adına heç bir məktub olmadığını
vurğulayaraq yola salarsınız. İndi fərz edin ki, siz hər dəfə vətəndaşlar sizə müraciət etdikdə yenidən təkrar 
təkrar məktubları bir axtarmaq kimi bu yorucu işi görmək istəmir və bunu komputerin köməyi ilə daha sürətli etmək 
istəyirsiniz. Bunun üçün nə etməlisiniz? İlk öncə poçt ofisində olan məktublara hər bir vətəndaş üçün unikal
kod verərək bütün məktublrdan ibarət bir çoxluq/massiv yaratmalısınız. Daha sonra vətəndaşlar sizə müraciət etdikdə
daha öncədən vətəndaşa verdiyiniz unikal kod proqrama daxil edərək həmin vətəndaşın adına məktub olub olmadığını
proqram sizə çox qısa zaman deyəcək. Proqram sizin daxil etdiyiniz unikal kodu daha öncədən yaratmış olduğunuz 
məktublar çoxluğunu/massivini axtaracaq. Əgər məktub tapılarsa sizə məktubun nömrəsini, tapılmazsa isə məktub 
yoxdur mesajını verəcək. Proqramın məktubu tapmaq üçün istifadə etdiyi bu əməliyyatlar ardıcılığı "Xətti Axtarış" 
alqoritması adlanır. 

`Qeyd 1: ofisdə hər bir vətəndaşın adına sadəcə və sadəcə bir məktub olduğunu fərz edirik.`

`Qeyd 2: massivin indeksi məktubun rəfdəki sıra nömrəsini göstərir`

````
Alqoritm: XəttiAxtarış(məktublar[], kod)

Addım 1: indeksi massivin ilk elementinə - yəni 1`ə - eyniləşdiririk
Addım 2: əgər indeks massivin sonuna çatdısa `Addım 6`ya gedirik
Addım 3: məktublar[indeks] = kod şərti ödənsə `Addım 5`ə gedirik
Addım 4: indeksi bir artırıb `Addım 2` yə gedirik
Addım 5: məktub tapıldığı üçün indeksi, yəni məktubun rəfdəki sıra nömrəsini ekranda çapa veririk
Addım 6: məktub tapılmadığı üçün `Məktub yoxdur` mesajını çapa veririk
````


**Psevode kod**

```
procedure xetti_axtaris (list, kod)
   for each item in the list
      if match item == value
         return the item's location
      end if
   end for
   return "Məktub yoxdur"
end procedure
```

**Kod**

```python
# Xətti axtarış alqoritması
def linear_search(mektublar, kod):
    # Addım 1: proqramlaşdırmada indeks 0 dan başladığı üçün 1ə yox 0la eyniləşdiririk.
    indeks = 0

    # çoxluqda/massivdə neçə element olduğunu müəyyən edirik.
    say = len(mektublar)

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
```

```python
import unittest

from linear_search import algo


class MyTestCase(unittest.TestCase):
    massiv = [3, 5, 2, 1, 20, 12, 10]

    def test_mektub_var(self):
        # gözlənilən nəticə
        expected = 1

        # real nəticə
        actual = algo.linear_search(mektublar=self.massiv, kod=3)

        self.assertEqual(expected, actual)

    def test_mektub_yoxdur(self):
        # gözlənilən nəticə
        expected = "Məktub yoxdur"

        # real nəticə
        actual = algo.linear_search(mektublar=self.massiv, kod=33)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
```

Xətti axtarış alqoritması kiçik və orta həcmli dağınıq massivlər üçün əlverişlidir.
Alqoritmadan anladığınız kimi bu alqoritm böyük çoxluqlar üçün əlverişli deyil belə ki,
axtardığınız element massivin ən sonuncu elementi olsa bu zaman bütün elementləri bir
bir yoxlamalı olacaqsınız. 