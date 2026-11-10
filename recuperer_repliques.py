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
