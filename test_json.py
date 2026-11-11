citations = []
def test_replique(content):
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
            

    return ""