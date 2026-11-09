from pathlib import Path


engine = pyttsx3.init()
engine.setProperty('rate', 150)

def lire_piece(chemin):
    with open(chemin, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def nettoyer(replique):
    replique = re.sub(r"\[.*?\]", "", replique)
    replique = re.sub(r"\(.*?\)", "", replique)
    return re.sub(r"\s+", " ", replique).strip()

texte = lire_piece("hamlet.txt")

total_lettres = 0
for caractere in texte:
    if caractere.isalpha():
        total_lettres += 1

print("Nombre total de lettres dans la pièce :", total_lettres)

occurences = {}

for caractere in texte:
    if caractere.isalpha():
        lettre = caractere.lower()
        if lettre in occurences:
            occurences[lettre] += 1
        else:
            occurences[lettre] = 1

for lettre in sorted(occurences.keys()):
    print(f"Lettre '{lettre}' : {occurences[lettre]} occurrences")

mots = texte.split()
print("Nombre de mots dans la pièce :", len(mots))

mots_propres = []
for mot in texte.split():
    mot = mot.strip(".,!?;:\"'()[]{}<>")
    if mot:
        mots_propres.append(mot.lower())

print("Nombre de mots distincts dans la pièce :", len(set(mots_propres)))

def recuperer_repliques(texte):
    repliques = {}
    acteur = None
    piece_comencee = False

    for ligne in texte.splitlines():
        if ligne.startswith("ACT I."):
            piece_comencee = True
        if not piece_comencee:
            continue

        debut = re.match(r"^ {2}([A-Z][a-z]{1,8})\.\s*(.*)$", ligne)
        if debut:
            acteur = debut.group(1)
            repliques.setdefault(acteur, []).append(debut.group(2).strip())
        elif re.match(r"^ {4}\S", ligne) and acteur:
            repliques[acteur][-1] += " " + ligne.strip()
    for acteur in repliques:
        repliques[acteur] = [nettoyer(r) for r in repliques[acteur]]

    return repliques

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


def lire_repliques(acteur, liste, voix_par_acteur):
    engine.setProperty("voice", voix_par_acteur[acteur])
    for replique in liste:
        print(f"\n[{PERSONNAGES.get(acteur, acteur)}] {replique}")
        engine.say(replique)
    engine.runAndWait()


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

