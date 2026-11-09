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