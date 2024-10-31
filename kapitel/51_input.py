# 51_input.py
# ===========
# THEMA: Benutzereingaben mit input()
# Mit input() können wir den Benutzer nach Eingaben fragen
# ===========

# ========== ERKLÄRUNG ==========
print("=== Eingaben verstehen ===")

# 1. Texteingaben
# Die Eingabe wird als Text gespeichert
name = input("Wie heißt du? ")
print("Hallo", name)

spiel = input("Was ist dein Lieblingsspiel? ")
print("Cool,", spiel, "ist wirklich toll!")

# 2. Zahleneingaben
# Eingaben sind immer Text und müssen umgewandelt werden!
# int() für Ganzzahlen
alter = int(input("Wie alt bist du? "))
print("Nächstes Jahr bist du", alter + 1)

# float() für Dezimalzahlen
groesse = float(input("Wie groß bist du (in Metern)? "))
print("Du bist", groesse, "Meter groß")

# ========== BEISPIELE ==========
print("\n=== Praktische Beispiele ===")

# Beispiel 1: Spieler-Registrierung
print("\n=== Neuer Spieler ===")
spielername = input("Wähle deinen Spielernamen: ")
charakter = input("Wähle deinen Charakter (Magier/Krieger/Bogenschütze): ")
level = int(input("Mit welchem Level möchtest du starten? (1-10): "))

print("\nSpielerprofil erstellt:")
print("Name:", spielername)
print("Charakter:", charakter)
print("Level:", level)

# Beispiel 2: Taschenrechner
print("\n=== Mini-Taschenrechner ===")
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

print("\nErgebnisse:")
print("Addition:", zahl1 + zahl2)
print("Subtraktion:", zahl1 - zahl2)
print("Multiplikation:", zahl1 * zahl2)
print("Division:", zahl1 / zahl2)

# ========== AUFGABEN ==========
print("\n=== Jetzt bist du dran! ===")

# Aufgabe 1: Steckbrief-Generator
print("\n- Aufgabe 1: Erstelle einen Steckbrief -")
# TODO:
# 1. Frage nach: Name, Alter, Hobby, Lieblingsfarbe
# 2. Erstelle einen schönen Steckbrief daraus


# Aufgabe 2: Punkterechner
print("\n- Aufgabe 2: Punkte berechnen -")
# TODO:
# 1. Frage nach Punkten in Level 1 (Ganzzahl)
# 2. Frage nach Punkten in Level 2 (Ganzzahl)
# 3. Berechne und zeige die Gesamtpunktzahl
# 4. Berechne und zeige den Durchschnitt (Dezimalzahl)


# Aufgabe 3: Temperaturumrechner
print("\n- Aufgabe 3: Temperatur umrechnen -")
# TODO:
# 1. Frage nach einer Temperatur in Celsius (Dezimalzahl)
# 2. Rechne sie in Fahrenheit um (°F = °C * 9/5 + 32)
# 3. Gib beide Temperaturen aus
