def compter_mots(texte: str) -> int:
    """Compte les mots : une suite de lettres terminée par un espace ou un retour à la ligne."""
    mots = 0
    lettre_avant = False
    for c in texte:
        c = c.lower()
        if "a" <= c <= "z":
            lettre_avant = True
        elif (c == " " or c == "\n") and lettre_avant:
            mots += 1
            lettre_avant = False
        else:
            lettre_avant = False
    return mots