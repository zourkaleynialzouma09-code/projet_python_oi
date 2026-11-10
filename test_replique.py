
from tts import parler



def test_replique(content):
    for ligne in content.splitlines():
        pos = ligne[:10].find(".")
        if pos > 1:
            cle = ligne[:pos].strip()
            print(cle, "a dit :")
            print("  ",ligne[pos:])
            personnage = str(cle)
            parler(personnage)
            parler(ligne[pos:])
        else:
            print(ligne)
            parler(ligne)

    return ""