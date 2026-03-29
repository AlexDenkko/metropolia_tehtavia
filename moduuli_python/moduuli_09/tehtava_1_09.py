class Auto:

    def __init__(self, rekisteriTunnus, huippunopeus, nopeusNyt="0", kuljettumatka="0"):
        self.rekisteriTunnus = rekisteriTunnus
        self.huippunopeus = huippunopeus
        self.nopeusNyt = nopeusNyt
        self.kuljettumatka = kuljettumatka


auto1 = Auto("ABC-123", 142)
print({auto1})
auto2 = Auto("ABC-123", 142, 50, 100)

print(f"Rekisteritunnus: {auto1.rekisteriTunnus}")
print(f"Huippunopeus: {auto1.huippunopeus}km/h")
print(f"Nopeus nyt: {auto1.nopeusNyt}")
print(f"Kuljettu matka: {auto1.kuljettumatka}\n")

print(f"Rekisteritunnus: {auto2.rekisteriTunnus}")
print(f"Huippunopeus: {auto2.huippunopeus}km/h")
print(f"Nopeus nyt: {auto2.nopeusNyt}")
print(f"Kuljettu matka: {auto2.kuljettumatka}")
