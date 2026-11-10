PERSONNAGES = {
    "Ham": "Hamlet", "Hor": "Horatio", "King": "Le Roi (Claudius)",
    "Queen": "La Reine (Gertrude)", "Pol": "Polonius", "Laer": "Laertes",
    "Oph": "Ophélie", "Ros": "Rosencrantz", "Guil": "Guildenstern",
    "Clown": "Un fossoyeur", "Mar": "Marcellus", "Ber": "Bernardo",
    "Fran": "Francisco", "Ghost": "Le Fantôme", "Rey": "Reynaldo",
    "Osr": "Osric", "Capt": "Le capitaine norvégien", "Fort": "Fortinbras",
    "Volt": "Voltemand", "Cor": "Cornelius", "Priest": "Le prêtre",
    "Player": "Un comédien", "Gent": "Un gentilhomme", "Sailor": "Un marin",
    "Mess": "Un messager", "Luc": "Lucianus", "Lord": "Un seigneur",
    "Servant": "Un serviteur",
}

def nom_complet(cle):
    return PERSONNAGES.get(cle, cle)
#Retourne le nom complet du personnage correspondant à la clé donnée. Si la clé n'est pas trouvée, elle retourne la clé elle-même.

def trouver_cle(nom):
    for cle, nom_complet in PERSONNAGES.items():
        if nom_complet == nom:
            return cle
    return None
#Retourne la clé correspondant au nom complet du personnage donné. Si le nom n'est pas trouvé, elle retourne None.