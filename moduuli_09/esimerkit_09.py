""" class Koira:
    pass
   
koira = Koira()
koira.nimi = "Rekku"
koira.syntymävuosi = 2022

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." ) """

""" class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira = Koira("Rekku", 2022)

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." ) """

""" class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu vius")

koira1.hauku(2)
koira2.hauku(5) """

class Koira:

    tehty = 0

    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
print (f"Koiria on nyt {Koira.tehty}.")