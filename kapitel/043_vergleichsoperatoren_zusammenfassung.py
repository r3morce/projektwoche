# =================================================================
# PYTHON GRUNDLAGEN: VERGLEICHSOPERATOREN - ZUSAMMENFASSUNG
# =================================================================

# 1. ÜBERSICHT ALLER VERGLEICHSOPERATOREN
# --------------------------------------
# ==    Ist gleich
# !=    Ist ungleich
# >     Größer als
# <     Kleiner als
# >=    Größer oder gleich
# <=    Kleiner oder gleich

# 2. BEISPIELE
# -----------
level = 5
print("\n=== BEISPIELE FÜR VERGLEICHE ===")
print("level == 5:", level == 5)    # True (Gleichheit)
print("level != 5:", level != 5)    # False (Ungleichheit)
print("level > 3:", level > 3)      # True (Größer als)
print("level < 10:", level < 10)    # True (Kleiner als)
print("level >= 5:", level >= 5)    # True (Größer/gleich)
print("level <= 4:", level <= 4)    # False (Kleiner/gleich)

# 3. WICHTIGE REGELN
# -----------------
# - Vergleiche ergeben immer True oder False
# - Gleiche Werte werden mit == verglichen (nicht mit =)
# - Texte unterscheiden Groß- und Kleinschreibung
# - Zahlen verschiedener Typen (int/float) können verglichen werden

# 4. ANWENDUNGEN
# -------------
# - Punktestände vergleichen
# - Level-Anforderungen prüfen
# - Highscores vergleichen
# - Namen auf Gleichheit prüfen