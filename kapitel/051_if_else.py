# =================================================================
# PYTHON GRUNDLAGEN: IF-ELSE VERZWEIGUNGEN
# =================================================================
# In dieser Lektion lernen wir Verzweigungen kennen. Mit if und else
# kann unser Programm verschiedene Dinge tun, je nachdem ob eine
# Bedingung erfüllt ist oder nicht.

# -----------------------------------------------------------------
# 1. EINFACHE IF-VERZWEIGUNG
# -----------------------------------------------------------------
temperatur = 25  # Variablen kennst du schon
if temperatur > 20:  # Vergleiche auch, nur das if und der Doppelpunkt sind neu
    print("Das Wetter ist prima!")  # Wird nur ausgeführt, wenn Bedingung stimmt

# TODO: Kommentiere die folgenden Zeilen ein und probiere verschiedene
# Temperaturen aus, Zum Beispiel 10 und 20

# temperatur_heute = 15
# if temperatur_heute < 18:
#     print("Heute ist es kühl!")
#     print("Denk an eine Jacke!")

# -----------------------------------------------------------------
# 2. IF-ELSE VERZWEIGUNG
# -----------------------------------------------------------------
# Es kann nicht nur etwas ausgeführt werden wenn eine Bedingung zutrifft,
# sondern auch wenn sie eben nicht zutrifft.
# TODO: Kommentiere die folgenden Zeilen ein und ändere den
# regen Wert zwischen True und False
# regen = True
# if regen:
#     print("Die Katzen wollen nicht raus.")
# else:
#     print("Die Katzen gehen raus und haben Spaß!")

# -----------------------------------------------------------------
# 3. VERGLEICHSOPERATOREN IN BEDINGUNGEN
# -----------------------------------------------------------------
# TODO: Kommentiere die folgenden Zeilen ein und probiere
# verschiedene Werte für uhrzeit aus
# uhrzeit = 11
# if uhrzeit == 13:
#     print("Zeit für Mittagessen!")
# else:
#     print("Keine Essenszeit")

# Häufig verwendete Vergleichsoperatoren:
# ==    gleich
# !=    ungleich
# >     größer als
# <     kleiner als
# >=    größer oder gleich
# <=    kleiner oder gleich

# -----------------------------------------------------------------
# 4. TEXTE VERGLEICHEN
# -----------------------------------------------------------------
# TODO: Kommentiere die folgenden Zeilen ein und probiere
# verschiedene Eingaben aus
# lieblingsfarbe = input("Was ist deine Lieblingsfarbe? ")
# if lieblingsfarbe == "blau":
#     print("Wie das Meer!")
# else:
#     print("Eine schöne Farbe!")

# -----------------------------------------------------------------
# 5. ZAHLEN EINGEBEN UND VERGLEICHEN
# -----------------------------------------------------------------
# TODO: Kommentiere die folgenden Zeilen ein und gib verschiedene
# Zahlen ein. Beachte, dass wir int() brauchen, um aus der Eingabe
# eine Zahl zu machen
# entfernung = int(input("Wie weit möchtest du heute joggen (km)? "))
# if entfernung >= 5:
#     print("Das wird ein gutes Training!")
# else:
#     print("Eine lockere Runde also!")

# -----------------------------------------------------------------
# ÜBUNGSAUFGABEN
# -----------------------------------------------------------------
#
# 1. Entwickle ein kleines Quiz: Frage nach wie viele Katzen Mathias hat.
#    Bei richtiger Antwort Lob, bei falscher ein Tipp
#
# 2. Erstelle ein Programm das prüft, ob die eingegebene Temperatur
#    über oder unter dem Gefrierpunkt liegt