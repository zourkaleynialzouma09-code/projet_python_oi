import pyttsx3
import personnage
import re
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def lire_repliques(phrase):
    #lire_repliques(acteur, liste, voix_par_acteur):
    #engine.setProperty("voice", voix_par_acteur[acteur])
    #for replique in liste:
    #print(f"\n[{personnage.PERSONNAGES.get(acteur, acteur)}] {replique}")
    engine.say(phrase)
    engine.runAndWait()
