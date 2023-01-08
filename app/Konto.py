import re
from .CoreAccountFeatures import Core

class Konto(Core):
    def __init__(self, imie, nazwisko, pesel, promo=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.promo = promo

        if(self.promo !=None  and re.match("^PROM_([A-Z]{3})$", self.promo) and ((int(self.pesel[2:4]) > 12 and int(self.pesel[2:4]) < 81)
                or (int(self.pesel[0:2]) > 60 and int(self.pesel[2:4]) < 13
                                   and int(self.pesel[2:4]) > 0))):
            self.saldo = 50


    def wyslijPrzelewEkspres(self, kwota, odbiorca):
        handle = self.wyslijPrzelew(kwota,odbiorca)
        if(handle):
            self.historia.append(int(-kwota))
            self.historia.append(-1)
            odbiorca.historia.append(int(kwota))
            self.saldo -=1
            return True
        else:
            return False

    def zaciagnij_kredyt(self, kwota):
        if(len(self.historia) > 2 ):
            if(self.historia[-1] > 0 and self.historia[-2] >0 and self.historia[-3] > 0 and sum(self.historia[-5:]) > kwota):
                self.saldo +=kwota
                return True
            else:
                return  False

        else:
            return False





