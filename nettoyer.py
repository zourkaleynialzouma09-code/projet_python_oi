import re
def nettoyer(replique):
    replique = re.sub(r"\[.*?\]", "", replique)
    replique = re.sub(r"\(.*?\)", "", replique)
    return re.sub(r"\s+", " ", replique).strip()