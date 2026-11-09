def compter_lettres(texte):
    total_lettres = 0
    occurences = {}

    for caractere in texte:
        if caractere.isalpha():
            total_lettres += 1
            lettre = caractere.lower()
            if lettre in occurences:
                occurences[lettre] += 1
            else:
                occurences[lettre] = 1

    return total_lettres, occurences