class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# Pääohjelma
auto = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus}")
print(f"Nopeus: {auto.nopeus}")
print(f"Kuljettu matka: {auto.kuljettu_matka}")
print()

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")

auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
print()

auto.nopeus = 60
auto.kuljettu_matka = 2000
auto.kulje(1.5)
print(f"Kuljettu matka: {auto.kuljettu_matka} km")
