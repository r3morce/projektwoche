# 42_datentypen_loesungen.py
# ======================
# THEMA: Lösungen zu den Datentypen-Aufgaben
# ======================

# Lösung 1: Datentypen erkennen
print("=== Datentypen erkennen ===")
print(type("15"))        # str (Text)
print(type(15))         # int (Ganzzahl)
print(type(1.5))        # float (Dezimalzahl)
print(type("Python"))    # str (Text)
print(type(42.0))       # float (Dezimalzahl)
print(type(100))        # int (Ganzzahl)
print()

# Lösung 2: Spiele-Highscore
spielername = "MasterChief"
punktzahl = 2500
spielzeit = 45.5
schwierigkeit = "mittel"

print("=== Highscore ===")
print("Spieler:", spielername)
print("Punkte:", punktzahl)
print("Zeit:", spielzeit, "Minuten")
print("Schwierigkeit:", schwierigkeit)
print()

# Lösung 3: Sportauswertung
sportler = "Max Meyer"
versuche = 3
beste_weite = 7.85

print("=== Sportwertung ===")
print("Athlet:", sportler)
print("Versuche:", versuche)
print("Beste Weite:", beste_weite, "Meter")
