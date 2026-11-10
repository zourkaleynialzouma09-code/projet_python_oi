from collections import defaultdict
import re
import trouver_cle as trouver
from personnage import PERSONNAGES

def extraire_repliques(texte):
    # repliques = defaultdict(list)
    # personnage = None
    print(PERSONNAGES)
    for ligne in texte.splitlines():
        print(trouver.trouver_cle(ligne[:5]))
        if trouver.trouver_cle(ligne[:5]) == True:
            personnage = ligne[:6]
            contenu = ligne[6:]
            print(f"{personnage} a dit : {contenu}")

        
        
        
        
        
        # print(ligne[:6])
        # correspondance = ""
        # if correspondance and correspondance.group(1) in personnage:
        #     personnage = correspondance.group(1)
        #     contenu = correspondance.group(2).strip()
        #     if contenu:
        #         repliques[personnage].append(contenu)
        # elif personnage and ligne.strip():
        #     # Ignore les indications de scène entre parenthèses.
        #     contenu = ligne.strip()
        #     if not re.match(r"^(Enter|Exit|Exeunt|[A-Z][a-z]+ Ghost\.)", contenu):
        #         repliques[personnage].append(contenu)
    return ""