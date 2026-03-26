class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjoittaja {self.kirjoittaja}")
        print(f"Kirjan sivumäärä {self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja {self.päätoimittaja}")

aku = Lehti(nimi="Aku Ankka", päätoimittaja="Aki Hyyppä")
hytti6 = Kirja(nimi="Hytti n:6", kirjoittaja="Rosa Liksom", sivumäärä="2008")

#aku.tulosta_tiedot()
hytti6.tulosta_tiedot()


