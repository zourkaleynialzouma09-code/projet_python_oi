import sys
import comptage_mot
import comptage_lettre
import extraire_replique
import lire_fichier
# from lire_fichier import lire_piece
from paramètre import CHEMIN_DEFAUT
import recuperer_repliques
import serveur
import test_json
import test_replique
from trouver_cle import trouver_cle
import tts 
from personnage import PERSONNAGES
from collections import Counter, defaultdict
from flask import Flask, jsonify, request

HOST, PORT = "127.0.0.1", 5000
app = Flask(__name__)


@app.get("/api/compter_lettres")
def compter_lettres():
    chemin_fichier = CHEMIN_DEFAUT
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        texte = fichier.read()
# contenu =str(lire_fichier("hamlet.txt"))
# print(contenu)
    print("Nombre total de lettres dans la pièce :", comptage_lettre.compter_lettres(texte))
    return jsonify({"resultat" : comptage_lettre.compter_lettres(texte)})

@app.get("/api/compter_mots")
def compter_mots():
    chemin_fichier = CHEMIN_DEFAUT
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        texte = fichier.read()
# contenu =str(lire_fichier("hamlet.txt"))
# print(contenu)
    print("Nombre total de mots dans la pièce :", comptage_mot.compter_mots(texte))
    return jsonify({"resultat" : comptage_mot.compter_mots(texte)})






citations = []




def main():
    
    print("********* DEMARRAGE DU PROGRAMME ****************")
    chemin_fichier = CHEMIN_DEFAUT
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        texte = fichier.read()

    nb_lettres = comptage_lettre.compter_lettres(texte)
    print(nb_lettres)

    nb_mots = comptage_mot.compter_mots(texte)
    print(nb_mots)

    content = texte
        # def test_replique(content):
    for ligne in content.splitlines():
        pos = ligne[:10].find(".")
        if pos > 1:
            cle = ligne[:pos].strip()
            print(cle, "a dit :")
            print("  ",ligne[pos:])
            personnage = str(cle)
            citations.append((personnage, ligne[pos:]))
        else:
            print(ligne)

    # print(citations)
    # print(json)

    




if __name__ == "__main__":
    main()
    app.run(host=HOST, port=PORT)


# tts.lire_repliques("test de voix")
