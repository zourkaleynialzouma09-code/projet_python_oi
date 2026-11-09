import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
import pyttsx3

engine = pyttsx3.init()


PERSONNAGES = {
    "Ham": "Hamlet", "Hor": "Horatio", "King": "Le Roi (Claudius)",
    "Queen": "La Reine (Gertrude)", "Pol": "Polonius", "Laer": "Laertes",
    "Oph": "Ophélie", "Ros": "Rosencrantz", "Guil": "Guildenstern",
    "Clown": "Un fossoyeur", "Mar": "Marcellus", "Ber": "Bernardo",
    "Fran": "Francisco", "Ghost": "Le Fantôme", "Rey": "Reynaldo",
    "Osr": "Osric", "Capt": "Le capitaine norvégien", "Fort": "Fortinbras",
    "Volt": "Voltemand", "Cor": "Cornelius", "Priest": "Le prêtre",
    "Player": "Un comédien", "Gent": "Un gentilhomme", "Sailor": "Un marin",
    "Mess": "Un messager", "Luc": "Lucianus", "Lord": "Un seigneur",
    "Servant": "Un serviteur",
}


def lire_piece(chemin):
    return Path(chemin).read_text(encoding="utf-8", errors="replace")

def compter(texte: str):
    letters = {}
    word = 0
    letterBefore = False
    for c in texte:
        if c.lower() >= 'a' and c.lower() <= 'z':
            letters[c.lower()] = letters.get(c.lower(), 0) + 1
            letterBefore = True
        elif (c == ' ' or c == '\n') and letterBefore:
            word += 1
            letterBefore = False
        else:
            letterBefore = False
    return letters, word



def extraire_repliques(texte):
    repliques = defaultdict(list)
    personnage = None
    for ligne in texte.splitlines():
        correspondance = re.match(r"^\s*([A-Z][a-z]{1,8})\.\s*(.*)$", ligne)
        if correspondance and correspondance.group(1) in PERSONNAGES:
            personnage = correspondance.group(1)
            contenu = correspondance.group(2).strip()
            if contenu:
                repliques[personnage].append(contenu)
        elif personnage and ligne.strip():
            # Ignore les indications de scène entre parenthèses.
            contenu = ligne.strip()
            if not re.match(r"^(Enter|Exit|Exeunt|[A-Z][a-z]+ Ghost\.)", contenu):
                repliques[personnage].append(contenu)
    return repliques


def lire_a_haute_voix(nom, texte):
    engine.say(f"{nom}. {texte}")
    engine.runAndWait()


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else "hamlet.txt"
    try:
        texte = lire_piece(chemin)
    except OSError:
        print(f"Fichier introuvable : {chemin}")
        print("Utilisation : python3 analyse_hamlet.py chemin/vers/hamlet.txt")
        return

    lettres, mots = compter(texte)
    repliques = extraire_repliques(texte)
    print(f"Nombre total de lettres : {sum(lettres.values())}")
    print("Nombre d'occurrences de chaque lettre :")
    for lettre, nombre in sorted(lettres.items()):
        print(f"  {lettre} : {nombre}")
    print(f"\nNombre de mots : {mots}")
    print("\nRépliques par personnage :")
    for cle, lignes in repliques.items():
        print(f"  {PERSONNAGES[cle]} : {len(lignes)} lignes")

    while True:
        choix = input("\nPersonnage à faire lire (nom ou Entrée pour arrêter) : ").strip()
        if not choix:
            break
        cle = next((k for k, nom in PERSONNAGES.items()
                    if choix.casefold() in (k.casefold(), nom.casefold())), None)
        if cle not in repliques:
            print("Personnage introuvable. Essaie Hamlet, Horatio, Ophélie, etc.")
        else:
            lire_a_haute_voix(PERSONNAGES[cle], " ".join(repliques[cle]))


if __name__ == "__main__":
    main()
