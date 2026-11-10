import sys

import comptage_mot
import comptage_lettre
from paramètre import CHEMIN_DEFAUT
import recuperer_repliques
import serveur
import tts 
import personnage
from collections import Counter, defaultdict

def main():
    chemin_fichier = lire_chemin()
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        texte = fichier.read()

    repliques = recuperer_repliques.recuperer_repliques(texte)
    occurences_lettres = comptage_lettre.compter_occurences_lettres(texte)
    occurences_mots = comptage_mot.compter_occurences_mots(texte)

    print("Occurrences de lettres :")
    for lettre, occurence in sorted(occurences_lettres.items()):
        print(f"{lettre}: {occurence}")

    print("\nOccurrences de mots :")
    for mot, occurence in sorted(occurences_mots.items()):
        print(f"{mot}: {occurence}")

    serveur.demarrer_serveur(repliques)

def lire_chemin(argv=None):
    """Retourne le chemin du fichier fourni en argument, ou le chemin par défaut."""
    argv = sys.argv if argv is None else argv
    return argv[1] if len(argv) > 1 else CHEMIN_DEFAUT

if __name__ == "__main__":
    main()


tts.lire_repliques("test de voix")
