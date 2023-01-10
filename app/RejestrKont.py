class Rejestr:
    lista = []

    @classmethod
    def dodaj(cls, konto):
        if cls.znajdz(konto.pesel):
            return False
        else:
            cls.lista.append(konto)
            return True


    @classmethod
    def znajdz(cls, pesel): # pesel imo bezpieczniejszy niz konto
        for konto in cls.lista:
            if(konto.pesel == pesel):
                return konto

        return False


    @classmethod
    def liczba_kont(cls):
        return len(cls.lista)
