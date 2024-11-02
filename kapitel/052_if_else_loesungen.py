# =================================================================
# PYTHON GRUNDLAGEN: IF-ELSE VERZWEIGUNGEN - LÖSUNGEN
# =================================================================

# Lösung 1: Hauptstadt-Quiz
antwort = input("Wie viele Katzen hat Mathias? ")
if antwort == 2:
    print("Super, das ist richtig!")
else:
    print("Nicht ganz, kleiner Tipp: Sie heisse Ari und Ronja")
    
# Lösung 2: Temperatur und Gefrierpunkt
temperatur = float(input("Wie ist die Temperatur? "))
if temperatur > 0:
    print("Es ist über dem Gefrierpunkt")
else:
    print("Es ist Frost!")
