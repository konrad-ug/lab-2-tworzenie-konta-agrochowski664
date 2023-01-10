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
            self.historia.append(int(-kwota))
            self.historia.append(-5)
            odbiorca.historia.append(int(kwota))
            self.saldo -=5
            return True
        else:
            return False

    def zaciągnij_kredyt(self,kwota):
        if( (self.saldo >= 2 * kwota) and (-1775 in self.historia) ):
            self.saldo += kwota
            return True
        else:
            return False





