# =================================================================
# PYTHON GRUNDLAGEN: IF-ELSE VERZWEIGUNGEN - ZUSAMMENFASSUNG
# =================================================================

bedingung = True

# 1. STRUKTUR EINER IF-VERZWEIGUNG
# -------------------------------
if bedingung:
    # Code der ausgeführt wird, wenn die Bedingung True ist
    print("Bedingung ist True")

# 2. STRUKTUR EINER IF-ELSE-VERZWEIGUNG
# -----------------------------------
if bedingung:
    # Code für True
    print("Bedingung ist True")
else:
    # Code für False
    print("Bedingung ist False")

# 3. VERGLEICHSOPERATOREN
# ----------------------
# ==    Ist gleich
# !=    Ist ungleich
# >     Größer als
# <     Kleiner als
# >=    Größer oder gleich
# <=    Kleiner oder gleich

# 4. BEISPIELE FÜR BEDINGUNGEN
# --------------------------
alter = 18
if alter >= 18:
    print("Volljährig")

name = "Alex"
if name == "Alex":
    print("Hallo Alex")

temperatur = 25
if temperatur > 20:
    print("Warm")
else:
    print("Kühl")

# 5. WICHTIGE REGELN
# ----------------
# - Nach if und else kommt ein Doppelpunkt
# - Der Code im if/else Block muss eingerückt sein
# - Einrückung immer gleich tief (meist 4 Leerzeichen)
# - Bedingungen werden von oben nach unten geprüft
# - Bei Textvergleichen auf Groß-/Kleinschreibung achten

# 6. HÄUFIGE ANWENDUNGEN
# --------------------
# - Werte vergleichen (größer, kleiner, gleich)
# - Benutzereingaben prüfen
# - Entscheidungen im Programm treffen
# - Fehler vermeiden (z.B. Division durch 0)
