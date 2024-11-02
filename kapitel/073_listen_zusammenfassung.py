# =================================================================
# PYTHON GRUNDLAGEN: LISTEN - ZUSAMMENFASSUNG
# =================================================================

# 1. LISTE ERSTELLEN
# -----------------
farben = ["rot", "grün", "blau"]      # Liste mit Texten
zahlen = [1, 2, 3, 4, 5]              # Liste mit Zahlen
gemischt = ["text", 42, True, 3.14]   # Gemischte Liste

# 2. AUF ELEMENTE ZUGREIFEN
# ------------------------
# Index beginnt bei 0!
print("\n=== ZUGRIFF AUF LISTEN ===")
print("Erstes Element:", farben[0])    # Erstes Element
print("Zweites Element:", farben[1])   # Zweites Element
print("Letztes Element:", farben[2])   # Letztes Element

# 3. LISTEN VERÄNDERN
# -----------------
team = ["Sam", "Alex"]
team.append("Robin")     # Element hinzufügen
team[1] = "Kim"         # Element ändern
print("\n=== LISTE VERÄNDERN ===")
print("Team nach Änderungen:", team)

# 4. WICHTIGE LISTENFUNKTIONEN
# --------------------------
scores = [85, 92, 78, 90]
print("\n=== LISTENFUNKTIONEN ===")
print("Anzahl Elemente:", len(scores))     # Länge der Liste
scores.sort()                              # Liste sortieren
print("Sortierte Liste:", scores)
scores.reverse()                           # Liste umdrehen
print("Umgedrehte Liste:", scores)

# 5. LISTE DURCHLAUFEN
# ------------------
print("\n=== LISTE DURCHLAUFEN ===")
for score in scores:
    print("Punktzahl:", score)

# 6. WICHTIGE REGELN
# ----------------
# - Listen können beliebig viele Elemente enthalten
# - Elemente können verschiedene Datentypen haben
# - Index beginnt bei 0
# - Listen sind veränderbar (mutable)
# - Auf nicht vorhandene Indizes kann nicht zugegriffen werden

# 7. HÄUFIGE ANWENDUNGEN
# --------------------
# - Sammlung von zusammengehörigen Werten
# - Speichern von Highscores
# - Verwaltung von Spielernamen
# - Inventarsysteme
# - Level-Informationen