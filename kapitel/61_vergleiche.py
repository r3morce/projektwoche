# 61_vergleiche.py
# ===============
# THEMA: Vergleichsoperatoren in Python
# Mit Vergleichen können wir prüfen, ob etwas gleich, größer oder kleiner ist
# ===============

# ========== ERKLÄRUNG ==========
print("=== Vergleichsoperatoren ===\n")

# 1. Gleich: ==
print("Gleich (==):")
print("5 == 5:", 5 == 5)       # True
print("5 == 3:", 5 == 3)       # False
print()

# 2. Ungleich: !=
print("Ungleich (!=):")
print("5 != 3:", 5 != 3)       # True
print("5 != 5:", 5 != 5)       # False
print()

# 3. Größer als: >
print("Größer als (>):")
print("5 > 3:", 5 > 3)         # True
print("3 > 5:", 3 > 5)         # False
print()

# 4. Kleiner als: <
print("Kleiner als (<):")
print("3 < 5:", 3 < 5)         # True
print("5 < 3:", 5 < 3)         # False
print()

# 5. Größer oder gleich: >=
print("Größer oder gleich (>=):")
print("5 >= 5:", 5 >= 5)       # True
print("5 >= 3:", 5 >= 3)       # True
print("3 >= 5:", 3 >= 5)       # False
print()

# 6. Kleiner oder gleich: <=
print("Kleiner oder gleich (<=):")
print("5 <= 5:", 5 <= 5)       # True
print("3 <= 5:", 3 <= 5)       # True
print("5 <= 3:", 5 <= 3)       # False
print()

# ========== BEISPIELE ==========
print("=== Praktische Beispiele ===\n")

# Beispiel 1: Spiele-Highscore
punktzahl = 85
print("Highscore-Check:")
print("Punktzahl:", punktzahl)
print("Über 50 Punkte?", punktzahl > 50)
print("Perfekte 100?", punktzahl == 100)
print("Unter 70?", punktzahl < 70)
print()

# Beispiel 2: Temperaturcheck
temperatur = 22
print("Temperatur-Check:")
print("Temperatur:", temperatur)
print("Über 25 Grad?", temperatur > 25)
print("Angenehm (18-24)?", temperatur >= 18 and temperatur <= 24)
print("Zu kalt (unter 15)?", temperatur < 15)
print()

# Beispiel 3: Level-Freischaltung
level = 5
min_level = 3
print("Level-Check:")
print("Aktuelles Level:", level)
print("Level ausreichend?", level >= min_level)
print()

# ========== AUFGABEN ==========
print("=== Jetzt bist du dran! ===\n")

# Aufgabe 1: Zahlenvergleiche
print("- Aufgabe 1: Vergleiche die Zahlen -")
# TODO: Vergleiche 10 und 7
# 1. Ist 10 größer als 7?
# 2. Ist 10 kleiner als 7?
# 3. Ist 10 gleich 7?
# 4. Ist 10 ungleich 7?


# Aufgabe 2: Spielerbewertung
print("\n- Aufgabe 2: Spielerbewertung -")
# TODO: Erstelle Vergleiche für:
# - punkte = 75
# 1. Ist die Punktzahl größer oder gleich 50?
# 2. Ist die Punktzahl kleiner als 100?
# 3. Ist die Punktzahl genau 75?


# Aufgabe 3: Quizfragen
print("\n- Aufgabe 3: Quiz-Vergleiche -")
# TODO: Beantworte mit True oder False:
# 1. Ist 15 größer als 20?
# 2. Ist 30 größer oder gleich 30?
# 3. Ist 42 ungleich 42?
# 4. Ist 100 kleiner oder gleich 99?
