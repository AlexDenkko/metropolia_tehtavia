""" class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return


class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + " kirjattu sisään")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + " kirjattu ulos")
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)

# Pääohjelma


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()
 """


""" class Auto:
    def __init__(self, rekisteritunnus, väri):
        self.rekisteritunnus = rekisteritunnus
        self.väri = väri


class Maalaamo:
    def maalaa(self, auto, väri):
        auto.väri = väri


maalaamo = Maalaamo()
auto = Auto("ABC-123", "sininen")
print("Auto on " + auto.väri)
maalaamo.maalaa(auto, "punainen")
print("Auto on nyt " + auto.väri) """
