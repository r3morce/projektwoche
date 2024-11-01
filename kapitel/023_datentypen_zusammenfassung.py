# =================================================================
# PYTHON GRUNDLAGEN: DATENTYPEN - ZUSAMMENFASSUNG
# =================================================================

# 1. DATENTYPEN ÜBERSICHT
# -----------------------
# Integer (int)    - Ganze Zahlen (positiv/negativ)
# Float (float)    - Kommazahlen (mit Dezimalpunkt)
# String (str)     - Text (in Anführungszeichen)
# Boolean (bool)   - Wahrheitswerte (True/False)

# 2. BEISPIELE FÜR JEDEN DATENTYP
# ------------------------------
punkte = 100              # Integer
prozent = 75.5           # Float
name = "Sam"             # String
aktiv = True             # Boolean

# 3. WICHTIGE REGELN
# -----------------
# - Kommazahlen werden mit Punkt geschrieben (nicht Komma)
# - Text kann einfache oder doppelte Anführungszeichen nutzen
# - True und False werden großgeschrieben
# - Mit type() kann man den Datentyp einer Variable prüfen

# 4. ANWENDUNGEN
# -------------
# Integer: Punktzahlen, Level, Anzahl von Gegenständen
# Float:   Spielzeit, Geschwindigkeit, Prozentangaben
# String:  Namen, Beschreibungen, Status-Meldungen
# Boolean: Spielzustände, Errungenschaften, Verfügbarkeit

# 5. DATENTYP PRÜFEN
# -----------------
print("=== DATENTYP BEISPIELE ===")
print("Integer:", type(punkte))    # <class 'int'>
print("Float:", type(prozent))     # <class 'float'>
print("String:", type(name))       # <class 'str'>
print("Boolean:", type(aktiv))     # <class 'bool'>