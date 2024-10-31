# 53_input_zusammenfassung.py
# =========================
# THEMA: Zusammenfassung zu Eingaben
# =========================

# === Grundlagen von input() ===

# 1. Texteingaben
# - input() liefert immer Text
# - Anführungszeichen nicht nötig bei Eingabe
name = input("Dein Name: ")
print("Text-Eingabe:", name)

# 2. Zahleneingaben
# - int() für Ganzzahlen
# - float() für Dezimalzahlen
alter = int(input("Dein Alter: "))
groesse = float(input("Deine Größe in Metern: "))
print("Ganzzahl:", alter)
print("Dezimalzahl:", groesse)

# === Wichtige Regeln ===

# 1. input() gibt IMMER einen Text zurück
# - Auch bei Zahlen-Eingaben kommt Text zurück
# - Umwandlung nötig für Berechnungen

# 2. Umwandlung von Eingaben
# - int(input()) für Ganzzahlen
# - float(input()) für Dezimalzahlen

# === Häufige Fehler vermeiden ===

# 1. Fehlende Umwandlung
# alter = input("Alter: ")       # Ergibt Text!
# alter = int(input("Alter: "))  # Richtig für Zahlen

# 2. Falsche Umwandlung
# Benutzer gibt "Hallo" ein:
# zahl = int(input("Zahl: "))    # Fehler!

# 3. Punkt statt Komma
# Bei Dezimalzahlen Punkt verwenden:
# 3.14 richtig
# 3,14 falsch

# === Praxistipps ===

# 1. Klare Eingabeaufforderungen
name = input("Wie heißt du? ")  # Besser als nur "Name: "

# 2. Fehlerbehandlung
# Später lernen wir, wie man Eingabefehler abfängt

# 3. Eingaben testen
# - Mit normalen Werten
# - Mit Sonderfällen
# - Mit falschen Eingaben

# === Typische Anwendungen ===

# 1. Textverarbeitung
# - Namen
# - Auswahlmöglichkeiten
# - Spielereingaben

# 2. Zahlenverarbeitung
# - Alter
# - Punktzahlen
# - Messwerte
# - Berechnungen
