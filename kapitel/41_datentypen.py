# 41_datentypen.py
# ================
# THEMA: Datentypen in Python
# Python kennt verschiedene Arten von Daten: Texte, Ganzzahlen und Dezimalzahlen
# ================

# ========== ERKLÄRUNG ==========
print("=== Die wichtigsten Datentypen ===")

# 1. Texte (Strings, str)
# - Stehen in Anführungszeichen
# - Können Buchstaben, Zahlen, Symbole enthalten
name = "Alex"             # Text mit doppelten Anführungszeichen
lieblingsspiel = 'Mario'  # Text mit einfachen Anführungszeichen
print("\nText-Beispiele:")
print("Name:", name, "- Typ:", type(name))
print("Spiel:", lieblingsspiel, "- Typ:", type(lieblingsspiel))

# 2. Ganzzahlen (Integer, int)
# - Zahlen ohne Komma
# - Keine Anführungszeichen
alter = 15
punkte = 100
print("\nGanzzahl-Beispiele:")
print("Alter:", alter, "- Typ:", type(alter))
print("Punkte:", punkte, "- Typ:", type(punkte))

# 3. Dezimalzahlen (Float)
# - Zahlen mit Nachkommastellen
# - Punkt statt Komma
# - Keine Anführungszeichen
groesse = 1.75
temperatur = 21.5
print("\nDezimalzahl-Beispiele:")
print("Größe:", groesse, "- Typ:", type(groesse))
print("Temperatur:", temperatur, "- Typ:", type(temperatur))

# ========== BEISPIELE ==========
print("\n=== Praktische Beispiele ===")

# Beispiel 1: Spieler-Statistik
name = "SuperMario"      # Text (str)
level = 5               # Ganzzahl (int)
leben = 100            # Ganzzahl (int)
energie = 75.5         # Dezimalzahl (float)

print("\n=== Spieler-Statistik ===")
print("Name:", name)
print("Level:", level)
print("Leben:", leben)
print("Energie:", energie)

# Beispiel 2: Schulnoten
fach = "Mathematik"     # Text (str)
note = 2                # Ganzzahl (int)
punkte = 87.5           # Dezimalzahl (float)

print("\n=== Notenübersicht ===")
print("Fach:", fach)
print("Note:", note)
print("Punkte:", punkte)

# ========== AUFGABEN ==========
print("\n=== Jetzt bist du dran! ===")

# Aufgabe 1: Datentypen erkennen
print("\n- Aufgabe 1: Erkenne den Typ -")
# TODO: Bestimme den Datentyp (str, int oder float):
# - "15"
# - 15
# - 1.5
# - "Python"
# - 42.0
# - 100

# Aufgabe 2: Spiele-Highscore
print("\n- Aufgabe 2: Highscore-Tabelle -")
# TODO: Erstelle folgende Variablen mit passenden Datentypen:
# - Spielername
# - Punktzahl (ganze Zahl)
# - Spielzeit in Minuten (mit Nachkommastellen)
# - Schwierigkeitsgrad (als Text: "leicht", "mittel", "schwer")

# Aufgabe 3: Sportauswertung
print("\n- Aufgabe 3: Sportwertung -")
# TODO: Erstelle Variablen für:
# - Name des Sportlers
# - Anzahl der Versuche (ganze Zahl)
# - Beste Weite (mit zwei Nachkommastellen)
