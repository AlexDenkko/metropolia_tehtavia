# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina 
# saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa 
# tehtävää, jossa alkuluvun testaus tehtiin. 
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan 
# muodossa: http://127.0.0.1:3000/alkuluku/31. 
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    #kokonaisluku intiksi
    luku = int(luku)
    for x in range(2, luku):
        if kokonaisluku % x == 0:
            onko_alkuluku = False
            break
        #vastauksen luonti ja palautus
        vastaus = {
            "Number" : luku,
            "isPrime" : onko_alkuluku
        }

    return vastaus


app.run(use_reloader=True, host='127.0.0.1', port=3000)
