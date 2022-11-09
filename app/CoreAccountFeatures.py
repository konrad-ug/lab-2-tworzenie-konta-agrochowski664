class Core:
    def __init__(self):
        self.saldo = 0


    def otrzymajPrzelew(self, kwota):
        self.saldo += kwota

    def wyslijPrzelew(self, kwota, odbiorca):
            if self.saldo >= kwota:
                    self.saldo -= kwota
                    odbiorca.saldo += kwota
                    return True
            else:
                return False

