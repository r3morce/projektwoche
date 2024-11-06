# =================================================================
# PYTHON GRUNDLAGEN: WIEDERHOLUNG 
# =================================================================
# In dieser Lektion wiederholen wir die wichtigsten Grundlagen:
# - print(): Ausgabe von Text und Zahlen
# - Variablen: Speichern von Werten
# - Datentypen: Verschiedene Arten von Werten
# - input(): Einlesen von Benutzereingaben
# - Vergleiche: Werte vergleichen
# - if/else: Entscheidungen treffen

# -----------------------------------------------------------------
# 1. PRINT UND VARIABLEN WIEDERHOLEN
# -----------------------------------------------------------------
# Die print()-Funktion gibt Text und Zahlen aus
print("Willkommen zur Wiederholung!")  # Einfache Textausgabe

# TODO: Kommentiere die folgenden Zeilen ein und beobachte die verschiedenen
# Möglichkeiten der Ausgabe
# punkte = 100  # Eine Variable für die Punktzahl
# leben = 3     # Eine Variable für die Anzahl der Leben
# print("Du hast", punkte, "Punkte und", leben, "Leben")

# -----------------------------------------------------------------
# 2. DATENTYPEN WIEDERHOLEN
# -----------------------------------------------------------------
# Es gibt verschiedene Arten von Werten (Datentypen):
# - Text (String, str): In Anführungszeichen
# - Ganze Zahlen (Integer, int): Ohne Komma
# - Kommazahlen (Float): Mit Punkt statt Komma
# - Wahrheitswerte (Boolean): True oder False

# TODO: Kommentiere die folgenden Zeilen ein und beobachte die
# verschiedenen Datentypen
# spieler_name = "Kim"            # String
# alter = 16                      # Integer
# highscore = 99.5               # Float
# spiel_aktiv = True             # Boolean
# print("Datentyp von Name:", type(spieler_name))
# print("Datentyp von Alter:", type(alter))
# print("Datentyp von Highscore:", type(highscore))
# print("Datentyp von Spiel aktiv:", type(spiel_aktiv))

# -----------------------------------------------------------------
# 3. INPUT WIEDERHOLEN
# -----------------------------------------------------------------
# Mit input() können wir Eingaben vom Benutzer einlesen

# TODO: Kommentiere die folgenden Zeilen ein und gib verschiedene
# Werte ein
# name = input("Wie heißt du? ")
# print("Hallo", name)

# Wenn wir Zahlen einlesen wollen, müssen wir sie umwandeln
# TODO: Kommentiere die folgenden Zeilen ein und gib verschiedene
# Zahlen ein
# alter = int(input("Wie alt bist du? "))
# print("Du bist", alter, "Jahre alt")

# -----------------------------------------------------------------
# 4. VERGLEICHE UND IF/ELSE WIEDERHOLEN
# -----------------------------------------------------------------
# Mit Vergleichsoperatoren können wir Werte vergleichen:
# ==    gleich
# !=    ungleich
# >     größer als
# <     kleiner als
# >=    größer oder gleich
# <=    kleiner oder gleich

# Mit if/else können wir verschiedene Dinge tun, je nachdem ob
# eine Bedingung erfüllt ist oder nicht

# TODO: Kommentiere die folgenden Zeilen ein und probiere verschiedene
# Punktzahlen aus
# punkte = int(input("Wie viele Punkte hast du erreicht? "))
# if punkte >= 100:
#     print("Fantastisch! Neuer Highscore!")
# else:
#     print("Weiter üben! Dir fehlen noch", 100 - punkte, "Punkte")

# -----------------------------------------------------------------
# ÜBUNGSAUFGABEN
# -----------------------------------------------------------------
# 1. Erstelle ein kleines Quiz-Spiel:
#    - Frage den Spieler nach seinem Namen
#    - Stelle eine Frage (z.B. "Wie viele Planeten hat unser Sonnensystem?")
#    - Prüfe ob die Antwort richtig ist (8)
#    - Gib eine passende Rückmeldung
#
# 2. Programmiere einen einfachen Taschenrechner:
#    - Lies zwei Zahlen ein
#    - Frage welche Rechenoperation ausgeführt werden soll (+ oder -)
#    - Führe die Berechnung durch und gib das Ergebnis aus
#
# 3. Erstelle ein Spiel "Zahlenraten":
#    - Lege eine Zahl fest (z.B. 42)
#    - Der Spieler soll die Zahl erraten
#    - Gib Hinweise ob die geratene Zahl zu hoch oder zu niedrig ist
