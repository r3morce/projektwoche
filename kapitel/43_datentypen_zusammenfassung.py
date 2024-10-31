# 43_datentypen_zusammenfassung.py
# ===========================
# THEMA: Zusammenfassung der Datentypen
# ===========================

# === Die drei wichtigsten Datentypen ===

# 1. Text (str - String)
print("=== Texte (str) ===")
name = "Python"
print("Text mit doppelten Anführungszeichen:", name)
sprache = 'Python'
print("Text mit einfachen Anführungszeichen:", sprache)
print("Typ von Text:", type(name))
print()

# 2. Ganzzahlen (int - Integer)
print("=== Ganzzahlen (int) ===")
alter = 15
punkte = 100
print("Positive Zahl:", alter)
print("Größere Zahl:", punkte)
print("Typ von Ganzzahlen:", type(alter))
print()

# 3. Dezimalzahlen (float)
print("=== Dezimalzahlen (float) ===")
groesse = 1.75
gewicht = 60.5
print("Größe in Metern:", groesse)
print("Gewicht in kg:", gewicht)
print("Typ von Dezimalzahlen:", type(groesse))
print()

# === Wichtige Regeln ===

# 1. Text:
# - Braucht immer Anführungszeichen (" oder ')
# - Auch Zahlen in Anführungszeichen sind Text
# - Kann beliebige Zeichen enthalten

# 2. Ganzzahlen:
# - Keine Anführungszeichen
# - Keine Nachkommastellen
# - Für Zähler und ganze Werte

# 3. Dezimalzahlen:
# - Keine Anführungszeichen
# - Punkt als Dezimaltrennzeichen
# - Für Messwerte und Berechnungen

# === Häufige Fehler vermeiden ===
# 1. Verwechslung von Text und Zahl
zahl = 42        # Zahl zum Rechnen
text = "42"      # Text, nicht zum Rechnen

# 2. Komma statt Punkt
# preis = 9,99   # Falsch!
preis = 9.99     # Richtig!

# 3. Fehlende Anführungszeichen
# name = Max     # Falsch!
name = "Max"     # Richtig!

# === Typische Anwendungen ===
# Text (str):
# - Namen
# - Beschreibungen
# - Texteingaben

# Ganzzahlen (int):
# - Alter
# - Punktzahlen
# - Anzahl von Dingen

# Dezimalzahlen (float):
# - Größe/Gewicht
# - Preise
# - Messwerte
