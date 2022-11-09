import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    pesel = "55112179134"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    promo = "PROM_XYZ"
    pierwsze_konto = Konto(imie, nazwisko , pesel, promo)

    pesel2 = "02241808199"
    imie2 = "Dariusz2"
    nazwisko2 = "Januszewski2"
    promo2 = "PROM_XYZ"
    konto2 = Konto(imie2, nazwisko2 , pesel2, promo2)


    def test_tworzenie_konta(self):

        self.assertEqual(self.pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(self.pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(self.konto2.saldo, 50, "Saldo nie dodane!")


    def test_pesel(self):
        self.assertEqual(len(self.pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_create_promo(self):

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

