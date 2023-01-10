import unittest

from ..Konto import Konto
from ..RejestrKont import Rejestr

from parameterized import parameterized


class accountRegistryTest(unittest.TestCase):
    pesel1 = "77102252233"
    pesel2 = "55101879374"
    pesel3 = "94072924175"
    konto1 = Konto("Janusz", "Testowy", pesel1)
    konto2 = Konto("Barbara", "Testowa", pesel2)
    konto3 = Konto("aaaaa", "bbbowy", pesel3)

    def setUp(self):
        self.rejestr = Rejestr()

    @parameterized.expand([
        (konto1, True, [konto1]),
        (konto1, False, [konto1]),
    ])
    def test_dodawanie(self, konto, wynik, lista):
        res = self.rejestr.dodaj(konto)
        self.assertEqual(res, wynik)
        self.assertEqual(self.rejestr.lista, lista)

    @parameterized.expand([
        (konto1.pesel, konto1),
        (konto3.pesel, False),
    ])
    def test_znajdz(self, pesel, wynik):
        self.assertEqual(self.rejestr.znajdz(pesel), wynik)

    def test_liczba(self):
        self.assertEqual(self.rejestr.liczba_kont(), 1)
        self.rejestr.dodaj(self.konto2)
        self.assertEqual(self.rejestr.liczba_kont(), 2)


