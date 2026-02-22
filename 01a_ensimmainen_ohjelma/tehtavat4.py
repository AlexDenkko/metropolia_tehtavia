import random
#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

""" number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1 """

#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa

""" while True:
    inches = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} tuumaa = {centimeters} cm") """

#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, 
# kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, 
# että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Arvaa luku väliltä 1-10: "))
    if guess > secret_number:
        print("Liian suuri arvaus")
    elif guess < secret_number:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break
