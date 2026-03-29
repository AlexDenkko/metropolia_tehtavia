class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            self.nopeus = self.huippunopeus

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


# Pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aseta_nopeus(160)
polttoauto.aseta_nopeus(140)

sahkoauto.aja(3)
polttoauto.aja(3)

print(
    f"Sähköauto {sahkoauto.rekisteritunnus} matkamittari: {sahkoauto.matkamittari} km")
print(
    f"Polttomoottoriauto {polttoauto.rekisteritunnus} matkamittari: {polttoauto.matkamittari} km")
