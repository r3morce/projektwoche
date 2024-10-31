# 33_variablen_zusammenfassung.py
# ========================
# THEMA: Zusammenfassung zu Variablen
# ========================

# === Was ist eine Variable? ===
# Eine Variable ist wie eine beschriftete Box:
# 1. Die Box hat einen Namen (Beschriftung)
# 2. In der Box ist ein Wert
# 3. Der Wert kann sich ändern
# 4. Wir können den Wert jederzeit ansehen

# === Beispiele für Variablennamen ===
# ERLAUBT:
name = "Max"              # Einfacher Name
spieler_name = "Max"      # Mit Unterstrich
spielerName = "Max"       # CamelCase
name2 = "Max"            # Mit Zahlen (nicht am Anfang)
_name = "Max"            # Unterstrich am Anfang

# NICHT ERLAUBT:
# 2name = "Max"          # Keine Zahl am Anfang
# mein-name = "Max"      # Keine Bindestriche
# mein name = "Max"      # Keine Leerzeichen
# name! = "Max"          # Keine Sonderzeichen

# === Checkliste für Variablen ===
# ✓ Name beschreibt den Inhalt
# ✓ Keine Leerzeichen im Namen
# ✓ Beginnt mit Buchstabe oder _
# ✓ Enthält nur Buchstaben, Zahlen, _
# ✓ Ist kein Python-Schlüsselwort

# === Häufige Fehler vermeiden ===
# 1. Groß-/Kleinschreibung beachten:
name = "Max"
# Name ist nicht das gleiche wie name!

# 2. Anführungszeichen bei Text:
name = "Max"      # Richtig
# name = Max      # Falsch! Text braucht ""

# 3. Variable muss existieren:
# print(alter)    # Fehler! alter existiert nicht

# === Praxistipps ===
# 1. Verwende eindeutige Namen
# 2. Nutze englische oder deutsche Namen
# 3. Bleib bei einem Namens-Stil
# 4. Kommentiere komplexe Variablen
