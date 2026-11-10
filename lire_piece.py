from pathlib import Path
import re
import lire_repliques
from personnage import PERSONNAGES
import recuperer_repliques


def lire_piece(chemin):
    with open(chemin, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


texte = lire_piece("hamlet.txt")

total_lettres = 0
for caractere in texte:
    if caractere.isalpha():
        total_lettres += 1

print("Nombre total de lettres dans la pièce :", total_lettres)



texte = lire_piece("hamlet.txt")
repliques = recuperer_repliques(texte)

for acteur, liste in sorted(repliques.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{acteur} : {len(liste)} répliques")

def preparer_voix(acteurs):
    voices = engine.getProperty("voices")
    anglaises = [v for v in voices if any("en" in str(l).lower() for l in v.languages)]
    if not anglaises:
        anglaises = voices
    return {a: anglaises[i % len(anglaises)].id for i, a in enumerate(acteurs)}




acteurs = sorted(repliques, key=lambda a: len(repliques[a]), reverse=True)
voix_par_acteur = preparer_voix(acteurs)

while True:
    print("\n--- Acteurs disponibles ---")
    for a in acteurs:
        print(f"{a:8} {PERSONNAGES.get(a, a):28} {len(repliques[a])} répliques")

    saisie = input("\nQuel acteur ? (ex: Ham, ou 'q' pour quitter) : ").strip()
    if saisie.lower() == "q":
        break

    choix = next((a for a in repliques if a.lower() == saisie.lower()), None)
    if choix is None:
        print("Acteur inconnu, choisis une abréviation de la liste.")
        continue

    nb = input("Combien de répliques ? (un nombre, ou 'tout') : ").strip().lower()
    if nb == "tout":
        liste = repliques[choix]
    elif nb.isdigit():
        liste = repliques[choix][: int(nb)]
    else:
        print("Réponse non comprise.")
        continue

    lire_repliques(choix, liste, voix_par_acteur)
