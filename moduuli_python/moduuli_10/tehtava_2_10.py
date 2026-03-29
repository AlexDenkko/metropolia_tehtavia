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
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros)
                       for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei kelpaa")


if __name__ == "__main__":
    # Testaa Hissi-luokkaa
    print("=== Hissin testaus ===")
    h = Hissi(1, 10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)

    # Testaa Talo-luokkaa
    print("\n=== Talon testaus ===")
    talo = Talo(1, 10, 3)
    talo.aja_hissia(0, 7)
    print()
    talo.aja_hissia(1, 3)
    print()
    talo.aja_hissia(2, 1)
