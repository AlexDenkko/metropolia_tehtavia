class ihminen:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def TulostaIka(self):
        print(f"{self.ika}")


class Suomalainen(ihminen):
    def __init__(self, nimi, ika, sisu):
        self.sisu = sisu
        super().__init__(nimi, ika) #alustaa samat parametrit
    def Tervehdi(self):
        print(f"Morjens mä oon {self.nimi}")


Pena = ihminen(nimi="pekka", ika=53)

Kake = Suomalainen(nimi="kalle", ika=27, sisu=100)
Kake.TulostaIka()
Kake.Tervehdi()
