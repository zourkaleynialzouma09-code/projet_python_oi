from collections import defaultdict
import re

from personnage import PERSONNAGES

def extraire_repliques(texte):
    repliques = defaultdict(list)
    personnage = None
    for ligne in texte.splitlines():
        correspondance = re.match(r"^\s*([A-Z][a-z]{1,8})\.\s*(.*)$", ligne)
        if correspondance and correspondance.group(1) in personnage:
            personnage = correspondance.group(1)
            contenu = correspondance.group(2).strip()
            if contenu:
                repliques[personnage].append(contenu)
        elif personnage and ligne.strip():
            # Ignore les indications de scène entre parenthèses.
            contenu = ligne.strip()
            if not re.match(r"^(Enter|Exit|Exeunt|[A-Z][a-z]+ Ghost\.)", contenu):
                repliques[personnage].append(contenu)
    return repliques