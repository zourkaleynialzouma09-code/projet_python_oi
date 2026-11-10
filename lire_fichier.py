def lire_piece(chemin):
    with open(chemin, "r", encoding="utf-8", errors="replace") as f:
        return f.read()