import unittest

from parameterized import parameterized

from ..Konto import Konto
from ..KontoFirmowe import Konto_Firmowe


class loanTest(unittest.TestCase):
    imie = "Adam"
    nazwisko = "Januszewski"
    nip = "8461627563"
    pesel = "65112179134"


    def setUp(self):
        self.kontofirmowe = Konto_Firmowe(self.imie, self.nip)
        self.konto = Konto(self.imie, self.nazwisko,  self.pesel)


    @parameterized.expand([
        (500, True, [100, 200, 201]),
        (500, True, [100, 200, 200,200,200,200,200]),
        (1, False,  []),
        (1000, False, [400,400]),
        (100, False, [-100, -100,200]),
        (400, False, [300, 300]),
        (400, True, [1,1,401]),
        (400, False, [400]),
        (400, False, [100,100,50,50,100,100])

    ])
    def test_pozyczka_prywanta(self, kwota_kredytu, expectedValue, historia):
        self.konto.historia = historia

        udana_pozyczka = self.konto.zaciagnij_kredyt(kwota_kredytu)

        self.assertEqual(udana_pozyczka, expectedValue)
        self.assertEqual(self.konto.saldo, (kwota_kredytu if udana_pozyczka else 0)) # Z racji, że zawsze mamy zerowe saldo to przewidujemy, że zawssze będzie takie jak kwota pożyczki




    @parameterized.expand([
        (500, True, [100, 200, -1775], 1000),
        (500, False, [100, 200, 200,200,200,200,200], 9099),
        (1, False,  [], 10000),
        (1000, False, [400,400, -1775], 500),
        (100, False, [-100, -100,200, 1775], 201),
        (400, True, [-1775, 1775, 300], 20000),
        (400, True, [1,1,401, -1775], 800),


    ])
    def test_pozyczka_firmowa(self, kwota_kredytu, expectedValue, historia, saldo):
        self.kontofirmowe.historia = historia
        self.kontofirmowe.saldo = saldo



        udana_pozyczka = self.kontofirmowe.zaciągnij_kredyt(kwota_kredytu)

        self.assertEqual(udana_pozyczka, expectedValue)
        self.assertEqual(self.kontofirmowe.saldo, (kwota_kredytu+saldo if udana_pozyczka else saldo)) # Z racji, że zawsze mamy zerowe saldo to przewidujemy, że zawssze będzie takie jak kwota pożyczki
