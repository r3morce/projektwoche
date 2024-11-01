# =================================================================
# PYTHON GRUNDLAGEN: IF-ELSE VERZWEIGUNGEN - LÖSUNGEN
# =================================================================

# Lösung 1: Hauptstadt-Quiz
antwort = input("Was ist die Hauptstadt von Deutschland? ")
if antwort == "Berlin":
    print("Super, das ist richtig!")
else:
    print("Nicht ganz - die Hauptstadt ist Berlin")
    
# Lösung 2: Temperatur und Gefrierpunkt
temperatur = float(input("Wie ist die Temperatur? "))
if temperatur > 0:
    print("Es ist über dem Gefrierpunkt")
else:
    print("Es ist Frost!")
