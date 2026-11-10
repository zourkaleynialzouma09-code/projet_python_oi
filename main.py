import sys

import comptage_mot
import comptage_lettre
from paramètre import CHEMIN_DEFAUT
import recuperer_repliques
import serveur
import tts 
import personnage
from collections import Counter, defaultdict

def lire_chemin(argv=None):
    """Retourne le chemin du fichier fourni en argument, ou le chemin par défaut."""
    argv = sys.argv if argv is None else argv
    return argv[1] if len(argv) > 1 else CHEMIN_DEFAUT


tts.lire_repliques("test de voix")
