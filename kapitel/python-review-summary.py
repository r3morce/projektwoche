# =================================================================
# PYTHON GRUNDLAGEN: WIEDERHOLUNG - ZUSAMMENFASSUNG
# =================================================================

# 1. PRINT
# --------
print("Text ausgeben")              # Text ausgeben
print("Text", "verbinden")          # Mehrere Werte ausgeben
print("Zahl:", 42)                  # Text und Zahlen mischen

# 2. VARIABLEN
# ------------
name = "Kim"                       # Text speichern
alter = 16                         # Zahlen speichern
aktiv = True                      # Wahrheitswerte speichern
print(name, "ist", alter)         # Variablen ausgeben

# 3. DATENTYPEN
# -------------
text = "Hallo"                    # String (str)
ganze_zahl = 42                   # Integer (int)
komma_zahl = 3.14                 # Float
wahrheit = True                   # Boolean (bool)

# 4. INPUT
# --------
name = input("Name: ")            # Text einlesen
alter = int(input("Alter: "))     # Zahl einlesen
print("Hallo", name)              # Eingabe verwenden

# 5. VERGLEICHE
# -------------
print(42 == 42)                   # Gleichheit (True)
print(10 != 5)                    # Ungleichheit (True)
print(7 > 3)                      # Größer als (True)
print(2 < 1)                      # Kleiner als (False)
print(5 >= 5)                     # Größer/gleich (True)
print(6 <= 3)                     # Kleiner/gleich (False)

# 6. IF/ELSE
# ----------
alter = 16
if alter >= 16:
    print("Du darfst Zéfix spielen")
else:
    print("Du bist noch zu jung")

# 7. WICHTIGE REGELN
# -----------------
# - Text immer in Anführungszeichen
# - Zahlen ohne Anführungszeichen
# - Bei input() immer überlegen ob die Eingabe umgewandelt werden muss
# - Nach if/else immer Doppelpunkt
# - Code nach if/else muss eingerückt sein

# 8. HÄUFIGE FEHLER VERMEIDEN
# --------------------------
# name = Max           # Fehler: Text braucht Anführungszeichen
# alter = "16"         # Vorsicht: Text statt Zahl
# if alter == 16:      # Fehler: Kann Text nicht mit Zahl vergleichen
# if alter = 16:       # Fehler: Einzelnes = ist Zuweisung
# if alter >= 16       # Fehler: Doppelpunkt fehlt
