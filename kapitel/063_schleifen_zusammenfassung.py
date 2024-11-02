# =================================================================
# PYTHON GRUNDLAGEN: SCHLEIFEN - ZUSAMMENFASSUNG
# =================================================================

# 1. GRUNDFORM DER FOR-SCHLEIFE
# ----------------------------
# for variable in range(anzahl):
#     anweisungen...
#
# Beispiel:
# for i in range(3):
#     print(i)        # Gibt 0, 1, 2 aus

# 2. RANGE VARIANTEN
# -----------------
# range(5)      -> 0 bis 4
# range(1, 4)   -> 1 bis 3
# range(5, 0, -1) -> 5 bis 1 rückwärts

# 3. ÜBER TEXT ITERIEREN
# --------------------
# for buchstabe in text:
#     anweisungen...
#
# Beispiel:
# for b in "Hallo":
#     print(b)    # Gibt H, a, l, l, o aus

# 4. WICHTIGE REGELN
# ----------------
# - Einrückung beachten (4 Leerzeichen oder Tab)
# - range(n) beginnt bei 0 und geht bis n-1
# - Schleifenvariable (i, n, etc.) frei wählbar
# - Unterstrich (_) wenn Variable nicht genutzt wird

# 5. HÄUFIGE ANWENDUNGEN
# --------------------
# - Countdown/Hochzählen
# - Text buchstabieren
# - Mehrfache Eingaben
# - Wiederholte Ausgaben