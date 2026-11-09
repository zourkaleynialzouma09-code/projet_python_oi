''' import re

# Lecture du fichier
with open("hamlet.txt", encoding="utf-8") as f:
    text = f.read()


# 1) Nombre total de lettres (a-z, sans distinction majuscule/minuscule)
def occurrences_lettres(text: str) -> dict:
    #Renvoie {lettre: nombre d'occurrences} pour les lettres a-z
    occurrences = {}
    for c in text.lower():
        if "a" <= c <= "z":
            occurrences[c] = occurrences.get(c, 0) + 1
    return occurrences


def compter_lettres(text: str) -> int:
    return sum(occurrences_lettres(text).values())


# 3) Nombre de mots
def compter_mots(text: str) -> int:
    """Compte les 'mots' : tout élément séparé par des blancs qui contient au moins une lettre."""
    compteur = 0
    for mot in text.split():
        if any(c.isalpha() for c in mot):
            compteur += 1
    return compteur


# 4) Répliques de chaque acteur
def extraire_repliques(text: str) -> dict:
    """Renvoie {"Ham.": ["réplique 1", "réplique 2", ...], ...}"""
    repliques = {}
    locuteur = None
    # Début de réplique : 2 espaces, un nom se terminant par un point, puis le texte
    debut = re.compile(r"^  (\d?\.? ?[A-Z][A-Za-z]*\.(?:, [A-Z][a-z]*\.)?) ?(.*)$")
    # Début de la 1re scène : avant, ce sont les "Dramatis Personae"
    index_acte = text.find("ACT I. Scene I.")
    corps = text[index_acte:] if index_acte != -1 else text

    for ligne in corps.split("\n"):
        if not ligne.strip():
            continue
        indentation = len(ligne) - len(ligne.lstrip())
        m = debut.match(ligne) if indentation == 2 else None

        if m:
            locuteur = m.group(1)
            repliques.setdefault(locuteur, []).append(m.group(2).strip())
        elif locuteur is not None and indentation == 4:
            # ligne de continuation de la dernière réplique
            repliques[locuteur][-1] += " " + ligne.strip()
        elif indentation > 4 or ligne.lstrip().startswith(("Enter", "Exit", "[", "Scene", "ACT")):
            # didascalie ou titre : la réplique précédente est terminée
            if indentation <= 2 or ligne.lstrip().startswith(("Scene", "ACT")):
                locuteur = None

    # Nettoyage : on retire les didascalies résiduelles en fin de réplique
    for nom, lignes in repliques.items():
        repliques[nom] = [re.sub(r"\s+(Exit|Exeunt|Dies)\b.*$", "", l).strip() for l in lignes]
    return repliques


# 5) Synthèse vocale
def lire(texte: str, moteur=None):
    import pyttsx3  
    moteur = moteur or pyttsx3.init()
    moteur.say(texte)
    moteur.runAndWait()


# Programme principal
if __name__ == "__main__":
    # Q1
    print(f"Nombre total de lettres : {compter_lettres(text)}")

    # Q2 : trié du plus fréquent au moins fréquent
    print("\nOccurrences de chaque lettre :")
    occ = occurrences_lettres(text)
    for lettre, n in sorted(occ.items(), key=lambda couple: couple[1], reverse=True):
        print(f"  {lettre} : {n}")

    # Q3
    print(f"\nNombre de mots (naïf)        : {len(text.split())}")
    print(f"Nombre de mots (avec lettres) : {compter_mots(text)}")

    # Q4
    rep = extraire_repliques(text)
    print("\nNombre de répliques par personnage :")
    for nom, lignes in sorted(rep.items(), key=lambda c: len(c[1]), reverse=True)[:10]:
        print(f"  {nom} {len(lignes)}")
    print("\nPremière réplique de Hamlet :", rep["Ham."][0])

   
    lire(rep["Ham."][0]) '''