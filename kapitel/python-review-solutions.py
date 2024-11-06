# =================================================================
# PYTHON GRUNDLAGEN: WIEDERHOLUNG - LÖSUNGEN 
# =================================================================

# Lösung 1: Quiz-Spiel
print("\n=== Quiz-Spiel ===")
name = input("Wie heißt du? ")
print("Hallo", name, "- lass uns ein Quiz spielen!")

antwort = int(input("Wie viele Planeten hat unser Sonnensystem? "))
if antwort == 8:
    print("Super,", name, "- das ist richtig!")
else:
    print("Leider falsch,", name, "- unser Sonnensystem hat 8 Planeten!")

# Lösung 2: Einfacher Taschenrechner
print("\n=== Taschenrechner ===")
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
operation = input("Was soll ich rechnen? (+ oder -): ")

if operation == "+":
    ergebnis = zahl1 + zahl2
    print("Das Ergebnis von", zahl1, "+", zahl2, "ist", ergebnis)
elif operation == "-":
    ergebnis = zahl1 - zahl2
    print("Das Ergebnis von", zahl1, "-", zahl2, "ist", ergebnis)
else:
    print("Diese Operation kenne ich nicht!")

# Lösung 3: Zahlenraten
print("\n=== Zahlenraten ===")
ziel_zahl = 42
versuch = int(input("Rate die Zahl (zwischen 1 und 100): "))

if versuch == ziel_zahl:
    print("Super! Du hast die Zahl erraten!")
elif versuch < ziel_zahl:
    print("Die gesuchte Zahl ist größer!")
else:
    print("Die gesuchte Zahl ist kleiner!")
