# =================================================================
# PYTHON GRUNDLAGEN: VARIABLEN - ZUSAMMENFASSUNG
# =================================================================

# 1. VARIABLE ERSTELLEN
name = "Alex"        # Text in Anführungszeichen
level = 5           # Zahlen ohne Anführungszeichen
print(name, level)  # Variablen ausgeben

# 2. GRUNDREGELN
# - Variablennamen: Buchstaben, Zahlen, Unterstriche
# - Variablen müssen mit Buchstabe oder Unterstrich beginnen
# - Groß- und Kleinschreibung beachten (name ≠ Name)
# - Keine Leerzeichen im Namen erlaubt
# - Aussagekräftige Namen wählen

# 3. VARIABLEN ÄNDERN
punkte = 0          # Erste Zuweisung
print(punkte)       # Gibt 0 aus
punkte = 100        # Neue Zuweisung
print(punkte)       # Gibt 100 aus

# 4. VARIABLEN VERWENDEN
spieler = "Tom"
print("Hallo", spieler)           # In print verwenden
neuer_spieler = spieler           # Kopieren
print("Kopie:", neuer_spieler)    # Gibt "Tom" aus

# 5. HÄUFIGE FEHLER VERMEIDEN
# name = Max      # Fehler: Text braucht Anführungszeichen
# 123_player     # Fehler: Beginnt mit Zahl
# mein name      # Fehler: Enthält Leerzeichen
# Name = "Tom"   # Vorsicht: Anderer Name als name

# 6. TIPPS
# - Variablen sind wie beschriftete Boxen
# - Inhalt kann jederzeit geändert werden
# - Gleiche Variable = Neuer Wert überschreibt alten
# - Verschiedene Variablen = Verschiedene Boxen