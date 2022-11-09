import unittest
from ..Konto import Konto
from ..KontoFirmowe import Konto_Firmowe

class TestDoTransfer(unittest.TestCase):



    def test_wysylaniePrzelewu(self):
        pesel = "65112179134"
        imie = "Dariusz"
        nazwisko = "Januszewski"
        promo = "PROM_XYZ"

        pesel2 = "65113179135"
        imie2 = "ababa"
        nazwisko2 = "ebebe"

        konto2 = Konto(imie2, nazwisko2, pesel2)
        konto = Konto(imie, nazwisko, pesel, promo)

        self.assertEqual(konto.saldo, 50, "Bledne saldo po kodzie!")
        konto.wyslijPrzelew(20,konto2)
        self.assertEqual(konto.saldo, 30, "Zla suma salda!")
        self.assertEqual(konto2.saldo, 20, "Zla suma salda konto2!")

        handle = konto.wyslijPrzelew(9999,konto2)
        self.assertFalse(handle, "zle dzialanie funkcji")

    def test_odbieraniePrzelewu(self):
        pesel = "65112179134"
        imie = "Dariusz"
        nazwisko = "Januszewski"
        promo = "PROM_XYZ"

        konto = Konto(imie, nazwisko, pesel, promo)

        pesel2 = "65113179135"
        imie2 = "ababa"
        nazwisko2 = "ebebe"

        konto2 = Konto(imie2, nazwisko2, pesel2)

        konto.otrzymajPrzelew(200)
        self.assertEqual(konto.saldo, 250, "Zla suma salda!")

        konto2.otrzymajPrzelew(200)
        self.assertEqual(konto2.saldo, 200, "Zla suma salda!")



    def test_wysylaniePrzelewuExpress(self):
        pesel = "65112179134"
        imie = "Dariusz"
        nazwisko = "Januszewski"
        promo = "PROM_XYZ"

        konto = Konto(imie, nazwisko, pesel, promo)

        pesel2 = "65113179135"
        imie2 = "ababa"
        nazwisko2 = "ebebe"

        konto2 = Konto(imie2, nazwisko2, pesel2)

        konto.wyslijPrzelewEkspres(50,konto2)
        self.assertEqual(konto.saldo, -1, "Zla suma salda!")
        self.assertEqual(konto2.saldo, 50, "Zla suma salda!")
        handle = konto.wyslijPrzelewEkspres(50, konto2)
        self.assertFalse(handle, "Złe dzialanie funkcji!")


    def test_wysylaniePrzelewuExpressFirma(self):
        nip = "1111111111"
        imie = "Buldmar"


        konto = Konto_Firmowe(imie, nip)

        nip2 = "222222222"
        imie2 = "eeeeaaaa"

        konto2 = Konto_Firmowe(imie2, nip2)

        handle = konto.wyslijPrzelewEkspres(50,konto2)
        self.assertFalse(handle, "Nie powinno być przelewu!")
        konto.saldo = 100;
        konto.wyslijPrzelewEkspres(50, konto2)
        self.assertEqual(konto.saldo, 45 , "Zle saldo!")
        self.assertEqual(konto2.saldo, 50, "Zle saldo!")


