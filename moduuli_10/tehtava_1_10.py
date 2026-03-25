class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
        return self.nykyinen_kerros

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
        return self.nykyinen_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print("Virhe: kerrosta ei ole olemassa")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


h = Hissi(1, 10)
print(f"Hissi aloittaa kerroksessa {h.nykyinen_kerros}")

h.siirry_kerrokseen(5)
print(f"Saavuttu kerrokseen {h.nykyinen_kerros}\n")

h.siirry_kerrokseen(1)
print(f"Paluu kerrokseen {h.nykyinen_kerros}")
