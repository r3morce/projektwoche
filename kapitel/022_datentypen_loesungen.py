# =================================================================
# PYTHON GRUNDLAGEN: DATENTYPEN - LÖSUNGEN
# =================================================================

# Lösung 1: Münzen (Integer)
muenzen = 42
print("Gesammelte Münzen:", muenzen)
print("Datentyp:", type(muenzen))

# Lösung 2: Treffergenauigkeit (Float)
treffergenauigkeit = 88.5
print("Treffergenauigkeit:", treffergenauigkeit, "%")
print("Datentyp:", type(treffergenauigkeit))

# Lösung 3: Charaktername (String)
charakter_name = "Morgan"
print("Charaktername:", charakter_name)
print("Datentyp:", type(charakter_name))

# Lösung 4: Level Status (Boolean)
level_geschafft = True
print("Level abgeschlossen:", level_geschafft)
print("Datentyp:", type(level_geschafft))

# Lösung 5: Inventarsystem
anzahl_heiltraenke = 3          # Integer für Mengenzählung
gewicht_rucksack = 12.8         # Float für genaues Gewicht
gegenstand_name = "Zauberring"  # String für Beschreibung
ist_ueberladen = True          # Boolean für Status
print("\n=== INVENTAR STATUS ===")
print("Heiltränke:", anzahl_heiltraenke, type(anzahl_heiltraenke))
print("Rucksackgewicht:", gewicht_rucksack, type(gewicht_rucksack))
print("Gegenstand:", gegenstand_name, type(gegenstand_name))
print("Ausrüstbar:", ist_ueberladen, type(ist_ueberladen))