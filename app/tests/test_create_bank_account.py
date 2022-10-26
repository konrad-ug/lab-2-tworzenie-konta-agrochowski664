import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    pesel = "55112179134"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    promo = "PROM_XYZ"
    pierwsze_konto = Konto(imie, nazwisko , pesel, promo)

    def test_tworzenie_konta(self):

        self.assertEqual(self.pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        if self.pierwsze_konto.promo:
           return
        self.assertEqual(self.pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


    def test_pesel(self):
        self.assertEqual(len(self.pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_create_promo(self):
        if not self.pierwsze_konto.promo:
           return
        self.assertTrue(self.pierwsze_konto.promo[0:4].isupper(), "PREFIX kodu nie jest duzymi!")
        self.assertEqual(self.pierwsze_konto.promo[0:4], "PROM", "Prefix to nie PROM!")
        self.assertEqual(self.pierwsze_konto.promo[4], "_", "Po prefiksie nie ma podłogi!")
        self.assertTrue(self.pierwsze_konto.promo[5:8].isalpha(), "Suffiks kodu to nie litery!")
        self.assertTrue(self.pierwsze_konto.promo[5:8].isupper(), "Suffiks kodu nie jest duzymi!")
        self.assertEqual(len(self.pierwsze_konto.promo), 8, "Niepoprawna długość kodu!")

        self.assertTrue(((int(self.pierwsze_konto.pesel[2:4]) > 12 and int(self.pierwsze_konto.pesel[2:4]) < 81)
                        or (int(self.pierwsze_konto.pesel[0:2]) > 60 and int(self.pierwsze_konto.pesel[2:4]) < 13
                            and int(self.pierwsze_konto.pesel[2:4]) > 0)) and (self.pierwsze_konto.saldo == 50) or not ((int(self.pierwsze_konto.pesel[2:4]) > 12 and int(self.pierwsze_konto.pesel[2:4]) < 81)
                        or (int(self.pierwsze_konto.pesel[0:2]) > 60 and int(self.pierwsze_konto.pesel[2:4]) < 13
                            and int(self.pierwsze_konto.pesel[2:4]) > 0)) and (self.pierwsze_konto.saldo == 0) , "Człowiek powinien być urodzony po 1960 aby skorzystać z kodu!")

        # Jeśli urodzony po 1960 to saldo powinno byc 50, jesli nie to powinno byc 0 bo moze byc staruszek z poprawnym kodem i saldo nie będzie dodawane więc nie powinno wywalić błędu
