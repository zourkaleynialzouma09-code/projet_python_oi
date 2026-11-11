from personnage import PERSONNAGES


# def nom_complet(cle):
    # return PERSONNAGES.get(cle, cle)
#Retourne le nom complet du personnage correspondant à la clé donnée. Si la clé n'est pas trouvée, elle retourne la clé elle-même.

trouve = False

def trouver_cle(nom):
    # print(nom)
    for cle, valeur in PERSONNAGES.items():
        print(cle)
        if cle == nom:
            trouve = True
        else:
            trouve = False   

    return trouve