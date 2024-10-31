# 63_vergleiche_zusammenfassung.py
# ==============================
# THEMA: Zusammenfassung der Vergleichsoperatoren
# ==============================

# === Die Vergleichsoperatoren ===

# 1. Gleichheit und Ungleichheit
print("=== Gleichheit/Ungleichheit ===")
print("Gleich (==):", 5 == 5)       # True
print("Ungleich (!=):", 5 != 3)     # True
print()

# 2. Größer und Kleiner
print("=== Größer/Kleiner ===")
print("Größer (>):", 5 > 3)         # True
print("Kleiner (<):", 3 < 5)        # True
print()

# 3. Größer/Kleiner oder Gleich
print("=== Größer/Kleiner oder Gleich ===")
print("Größer/Gleich (>=):", 5 >= 5)  # True
print("Kleiner/Gleich (<=):", 5 <= 5)  # True
print()

# === Wichtige Regeln ===

# 1. Vergleiche ergeben immer True oder False
ergebnis = 5 > 3    # True
print("5 > 3:", ergebnis)

# 2. == für Vergleich, = für Zuweisung
x = 5       # Zuweisung
print("5 == 5:", 5 == 5)  # Vergleich

# 3. Mehrere Vergleiche möglich
print("3 < 5 < 7:", 3 < 5 < 7)  # True

# === Häufige Fehler vermeiden ===

# 1. = statt == verwenden
# if x = 5:    # Falsch! (Zuweisung)
# if x == 5:   # Richtig! (Vergleich)

# 2. Vergleich von verschiedenen Typen
# "5" == 5     # False, Text ≠ Zahl

# 3. Gleitkomma-Vergleiche
# 0.1 + 0.2 == 0.3  # Vorsicht bei Dezimalzahlen!

# === Merkhilfen ===
# - == ist wie "ist gleich?"
# - != ist wie "ist nicht gleich?"
# - > ist wie "ist größer als?"
# - < ist wie "ist kleiner als?"
# - >= ist wie "ist größer oder gleich?"
# - <= ist wie "ist kleiner oder gleich?"

# === Typische Anwendungen ===
# - Punktevergleiche in Spielen
# - Altersüberprüfungen
# - Temperaturvergleiche
# - Level-Anforderungen
# - Passwort-Überprüfungen

# === Checkliste ===
# ✓ == für "ist gleich"
# ✓ != für "ist ungleich"
# ✓ > für "größer als"
# ✓ < für "kleiner als"
# ✓ >= für "größer oder gleich"
# ✓ <= für "kleiner oder gleich"
