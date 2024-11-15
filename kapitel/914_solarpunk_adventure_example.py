# =================================================================
# SOLAR CITY ADVENTURE
# Ein einfaches Textadventure
# =================================================================

# Variablen für Spielzustand
solar_punkte = 0
werkzeug = False

# Begrüßung und Einführung
print("=== Willkommen in Solar City! ===")
print("In unserer grünen Stadt der Zukunft brauchen wir deine Hilfe!")
print("Der zentrale Solarturm muss repariert werden.\n")

# Spielername mit input() abfragen
name = input("Wie heißt du? ")
print(f"\nHallo {name}! Schön, dass du hier bist!")

# Erste Entscheidung mit if/else
print("\nDu stehst vor dem Solarturm. Was möchtest du tun?")
print("1: Nach oben klettern")
print("2: Erst im Werkzeugladen vorbeischauen")

wahl = input("\nDeine Wahl (1 oder 2)? ")

if wahl == "1":
    print("\nOhne Werkzeug kannst du leider nichts reparieren!")
    print("Du kletterst wieder runter.")
    solar_punkte -= 1
elif wahl == "2":
    print("\nGute Idee! Der Werkzeugladen ist gleich um die Ecke.")
    print("Du bekommst einen Solartool-Werkzeugkasten.")
    werkzeug = True
    solar_punkte += 2
else:
    print("\nDas verstehe ich nicht. Bitte wähle 1 oder 2.")

# Zweite Entscheidung, wenn Werkzeug vorhanden
if werkzeug:
    print("\nJetzt bist du optimal ausgerüstet! Was möchtest du reparieren?")
    print("1: Die Solarpanele reinigen")
    print("2: Die Steuerungseinheit überprüfen")
    print("3: Erstmal Mittagspause machen")
    
    wahl = input("\nDeine Wahl (1-3)? ")
    
    if wahl == "1":
        print("\nSuper! Saubere Panele = mehr Solarenergie!")
        solar_punkte += 3
    elif wahl == "2":
        print("\nExzellent! Die Steuerung läuft wieder optimal!")
        solar_punkte += 5
    elif wahl == "3":
        print("\nPause ist wichtig - aber der Turm wartet!")
        solar_punkte -= 1
    else:
        print("\nDas verstehe ich nicht. Bitte wähle 1, 2 oder 3.")

# Auswertung der Punkte mit if/elif/else
print(f"\nDeine Solar-Punkte: {solar_punkte}")

if solar_punkte >= 5:
    print("Fantastische Arbeit! Solar City dankt dir!")
elif solar_punkte > 0:
    print("Guter Anfang! Mit etwas Übung wird es noch besser!")
else:
    print("Das war noch nicht optimal. Probier es gleich nochmal!")

print("\n=== SPIEL ENDE ===")
