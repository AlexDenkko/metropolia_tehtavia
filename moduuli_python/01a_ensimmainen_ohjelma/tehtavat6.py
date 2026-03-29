""" viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.") """

""" pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p) """

numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Viivi"] = "050-1011012"
numerot["Ahmed"] = int(1000*0.90)
numerot["Seppo"] = int(99999)

print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")