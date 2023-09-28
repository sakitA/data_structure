import unittest

from stack.algo import Baglama, Stack


class MyTestCase(unittest.TestCase):
    def test_qutu_bosdur(self):
        qutu = Stack(3)

        self.assertTrue(qutu.bosdur())

    def test_qutu_doludur(self):
        qutu = Stack(1)

        baglama = Baglama("B1", "Kod1", "Adres1")
        qutu.elave_et(baglama)

        self.assertTrue(qutu.doludur())

    def test_qutu_elave_et(self):
        qutu = Stack(3)

        baglama = Baglama("B1", "Kod1", "Adres1")
        qutu.elave_et(baglama)

        self.assertEqual(1, qutu.baglama_sayi())

    def test_qutu_sil(self):
        qutu = Stack(3)

        baglama1 = Baglama("B1", "Kod1", "Adres1")
        baglama2 = Baglama("B2", "Kod2", "Adres2")
        qutu.elave_et(baglama1)
        qutu.elave_et(baglama2)

        qutu.sil()

        self.assertEqual(1, qutu.baglama_sayi())
        self.assertEqual(baglama1, qutu.baxmaq())

    def test_qutu_sil(self):
        qutu = Stack(3)

        baglama1 = Baglama("B1", "Kod1", "Adres1")
        baglama2 = Baglama("B2", "Kod2", "Adres2")
        qutu.elave_et(baglama1)
        qutu.elave_et(baglama2)

        sonuncu_baglama = qutu.baxmaq()

        self.assertEqual(2, qutu.baglama_sayi())
        self.assertEqual(baglama2, qutu.baxmaq())


if __name__ == '__main__':
    unittest.main()
