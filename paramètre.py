import sys

CHEMIN_DEFAUT = "hamlet.txt"
ENCODAGE = "utf-8"


def lire_chemin(argv=None):
    """Retourne le chemin du fichier fourni en argument, ou le chemin par défaut."""
    argv = sys.argv if argv is None else argv
    return argv[1] if len(argv) > 1 else CHEMIN_DEFAUT