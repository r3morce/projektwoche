# =================================================================
# PYTHON GRUNDLAGEN: INPUT (BENUTZEREINGABEN)
# =================================================================
# In dieser Lektion lernen wir, wie wir Eingaben von Benutzern
# in unser Programm einlesen können.
#
# Die input()-Funktion ist wie ein Formular: Das Programm hält an und
# wartet, bis der Benutzer etwas eingetippt und Enter gedrückt hat.
# Dann wird die Eingabe in einer Variable gespeichert - genau wie
# wenn wir einen Wert direkt zuweisen würden.

# -----------------------------------------------------------------
# 1. ERSTE EINGABE
# -----------------------------------------------------------------
# Ein Input besteht aus zwei Teilen:
# 1. Dem Text, der dem Benutzer angezeigt wird (in den Klammern)
# 2. Der Variable, in der die Antwort gespeichert wird

name = input("Wie ist dein Name? ")    # Programm stoppt und wartet hier
print("Hallo", name)                   # Verwendet die Eingabe

# TODO: Kommentiere die folgenden Zeilen ein und probiere verschiedene
# Eingaben aus. Beobachte, wie das Programm auf deine Eingabe wartet.
# lieblingsspiel = input("Was ist dein Lieblingsspiel? ")
# print("Cool,", lieblingsspiel, "ist ein tolles Spiel!")

# -----------------------------------------------------------------
# 2. EINGABEN WEITERVERARBEITEN
# -----------------------------------------------------------------
# Eingaben können wie normale Variablen verwendet werden
# TODO: Kommentiere die folgenden Zeilen ein und probiere aus, wie
# die Eingabe mehrfach verwendet wird
# nickname = input("Wähle einen Nickname: ")
# print("Willkommen,", nickname)
# print("Dein Nickname hat", len(nickname), "Buchstaben")
# print("In Großbuchstaben:", nickname.upper())

# -----------------------------------------------------------------
# 3. EINGABEN MIT HINWEISTEXT
# -----------------------------------------------------------------
# Der Text in input() sollte dem Benutzer helfen zu verstehen,
# was eingegeben werden soll
# TODO: Kommentiere die folgenden Zeilen ein und beachte den
# hilfreichen Hinweistext
# farbe = input("Was ist deine Lieblingsfarbe (z.B. rot, blau, grün)? ")
# print("Die Farbe", farbe, "ist eine tolle Wahl!")

# -----------------------------------------------------------------
# 4. MEHRERE EINGABEN NACHEINANDER
# -----------------------------------------------------------------
# Wir können beliebig viele Eingaben nacheinander abfragen
# TODO: Kommentiere die folgenden Zeilen ein und gib verschiedene
# Antworten ein
# hobby = input("Was ist dein Hobby? ")
# erfahrung = input("Wie lange machst du das schon? ")
# print("Wow! Du übst", hobby, "also schon", erfahrung, "aus!")

# -----------------------------------------------------------------
# ÜBUNGSAUFGABEN
# -----------------------------------------------------------------
# 1. Erstelle ein Programm, das nach dem Namen und dem Alter fragt
#    und beides zusammen ausgibt
#
# 2. Schreibe ein Programm für einen Steckbrief, das nach drei
#    verschiedenen Informationen fragt (z.B. Hobby, Lieblingsessen,
#    Lieblingsfarbe) und diese übersichtlich ausgibt
#
# 3. Entwickle ein Programm, das nach einem Lieblingstier fragt und
#    dann einen lustigen Satz damit bildet
