import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, promo=None):
            self.imie = imie
            self.nazwisko = nazwisko
            self.pesel = pesel
            self.saldo = 0
            self.promo = promo
            if(self.promo and re.match("^PROM_([A-Z]{3})$", self.promo) and (int(self.pesel[2:4]) > 12 and int(self.pesel[2:4]) < 81)
                        or (int(self.pesel[0:2]) > 60 and int(self.pesel[2:4]) < 13
                            and int(self.pesel[2:4]) > 0)):
                    self.saldo = 50
            pass
