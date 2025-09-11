# test_hra.py
import unittest
from HadiZebriky.hra import zpracuj_kolizi
from .utils import hod_kostkou

class MockHrac:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice

class MockDeska:
    def aplikuj_specialni_pole(self, pozice, jmeno, vypis):
        return pozice  # žádná speciální pravidla

def mock_vypis(msg):
    pass  # ignorujeme výpisy

class TestKolizeNaJednicce(unittest.TestCase):
    def test_hraci_na_poli_1_nejsou_posunuti_niz(self):
        hrac1 = MockHrac("A", 1)
        hrac2 = MockHrac("B", 1)
        hrac3 = MockHrac("C", 1)
        hrac4 = MockHrac("D", 1)
        deska = MockDeska()
        zpracuj_kolizi(hrac1, [hrac2], deska)
        self.assertEqual(hrac2.pozice, 1)

if __name__ == "__main__":
    unittest.main()
