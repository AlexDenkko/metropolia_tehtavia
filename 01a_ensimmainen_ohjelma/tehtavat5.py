# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numbers = []

while True:
    user_input = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    
    if user_input == "":
        break
    
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")

numbers.sort(reverse=True)
top_five = numbers[:5]

print("Viisi suurinta lukua:")
for num in top_five:
    print(num)