from .CoreAccountFeatures import Core

class Konto_Firmowe(Core):
    def __init__(self, nazwa, nip):
            super().__init__()
            self.nazwa = nazwa
            self.nip = nip

            if(len(nip) != 10):
                self.nip = 'Niepoprawny NIP!'


    def wyslijPrzelewEkspres(self, kwota, odbiorca):
        handle = self.wyslijPrzelew(kwota,odbiorca)
        if(handle):
            self.saldo -=5
            return True
        else:
            return False




