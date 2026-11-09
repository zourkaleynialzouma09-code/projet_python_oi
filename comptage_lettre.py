def compter_lettres(texte):
    total_lettres = 0

    for caractere in texte:
        if caractere.isalpha():
            total_lettres += 1

    return total_lettres