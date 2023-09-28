import unittest

from pkg_queue.algo import Queue, Baglama


class MyTestCase(unittest.TestCase):
    def test_sira_bosdur(self):
        sira = Queue()

        self.assertTrue(sira.bosdur())

    def test_siraya_elave_et(self):
        sira = Queue()

        baglama = Baglama("B1", "Kod1", "Adres1")
        sira.siraya_elave_et(baglama)

        self.assertFalse(sira.bosdur())

    def test_siradan_sil(self):
        sira = Queue()

        baglama1 = Baglama("B1", "Kod1", "Adres1")

        sira.siraya_elave_et(baglama1)

        baglama = sira.siradan_sil()

        self.assertTrue(sira.bosdur())
        self.assertEqual(baglama1, baglama)


if __name__ == '__main__':
    unittest.main()
