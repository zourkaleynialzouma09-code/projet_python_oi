def compter_occurences_lettres(texte):
    occurences = {}
    for caractere in texte:
        if caractere.isalpha():
            lettre = caractere.lower()
            if lettre in occurences:
                occurences[lettre] += 1
            else:
                occurences[lettre] = 1
    return occurences