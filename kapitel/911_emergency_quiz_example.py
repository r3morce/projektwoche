for _ in range(10):
    points = 0
    
    print("Hallo! Herzlich willkommen beim FEUMED V1!")
    
    player = input("Gib deinen Benutzernamen ein: ")
    
    print("Hallo", player)
    print("Ich beschreibe dir kurz die Regeln: Unser Ziel ist ein Spiel, das Leute auf ihr Wissen über Feuerwehr und medizinische Grundlagen testet.")
    print("Jetzt wähle 1 für das Feuerwehr-Thema oder 2 für Medizin!")
    
    choice = int(input("1 oder 2: "))
    if choice == 1:
        print(player, "du hast die Feuerwehr gewählt.")
        print("1. Frage: Wie lautet die EU-Notrufnummer?")
        print("Antwort (1): 110")
        print("Antwort (2): 112")
        print("Antwort (3): 999")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 2:
            points += 1 
            
        print("2. Frage: Wann wird die Feuerwehr gerufen?")
        print("Antwort (1): Bei Bränden, Unfällen etc.")
        print("Antwort (2): Nur bei Unfällen")
        print("Antwort (3): Nur bei Katzen auf Bäumen")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 1:
            points += 1 
            
        print("3. Frage: Was ist FF?")
        print("Antwort (1): Free Friends")
        print("Antwort (2): Freiwillige Feuerwehr")
        print("Antwort (3): Friends Forever")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 2:
            points += 1 
            
        print("4. Frage: Du fährst mit dem Auto und siehst ein Haus mit Rauchentwicklung. Was machst du?")
        print("Antwort (1): Fahre weiter, das geht mich nichts an.")
        print("Antwort (2): Halte an und schreie um Hilfe.")
        print("Antwort (3): Ich setze einen Notruf unter 112 ab, beantworte alle Fragen und begebe mich nicht in Gefahr.")
        answer = int(input("Wähle eine Antwort aus: "))   
        if answer == 3:
            points += 1   
            
        print("5. Frage: Bei dir zuhause brennt eine Pfanne mit Schnitzel und Öl. Wie löschst du diesen Brand?")
        print("Antwort (1): Mit einem Fettbrand-Feuerlöscher/Löschdecke")
        print("Antwort (2): Mit Wasser")
        print("Antwort (3): Gar nicht, ich renne weg!")
        answer = int(input("Wähle eine Antwort aus: "))     
        if answer == 1:
            points += 1     
            
        print("6. Frage: Welche Feuerlöscher-Klassen gibt es?")
        print("Antwort (1): A/B/C/D/F")
        print("Antwort (2): A/B/C")
        print("Antwort (3): Feuerlöscher ist Feuerlöscher")
        answer = int(input("Wähle eine Antwort aus: "))     
        if answer == 1:
            points += 1         
            
        print("Du hast", points, "von 6 Punkten.")
        
    else:
        print(player, "du hast Medizin gewählt.")
        print("1. Frage: Wie lange soll man die Atemfrequenz (AF) kontrollieren?")
        print("Antwort (1): 10 Sekunden")
        print("Antwort (2): 30 Sekunden")
        print("Antwort (3): 1 Minute")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 1:
            points += 1 
            
        print("2. Frage: Wie lautet die EU-Notrufnummer?")
        print("Antwort (1): 110")
        print("Antwort (2): 999")
        print("Antwort (3): 112")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 3:
            points += 1 
            
        print("3. Frage: Wie macht man eine HLW (Herz-Lungen-Wiederbelebung)?")
        print("Antwort (1): 30-50 mal in der Thoraxmitte drücken/pro min")
        print("Antwort (2): 100-120 mal in der Thoraxmitte drücken/pro min")
        print("Antwort (3): 112-130 mal in der Thoraxmitte drücken/pro min")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 2:
            points += 1 
            
        print("4. Frage: Was ist RTW?")
        print("Antwort (1): Rettungswagen")
        print("Antwort (2): Krankenwagen")
        print("Antwort (3): Rettungshubschrauber")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 1:
            points += 1 
            
        print("5. Frage: Wo landet ein Notruf unter 112?")
        print("Antwort (1): In einer Rettungsleitstelle")
        print("Antwort (2): Bei der Polizei")
        print("Antwort (3): Bei der örtlichen Feuerwehr")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 1:
            points += 1 
            
        print("6. Frage: Was sind die 5W-Fragen?")
        print("Antwort (1): Grundlegende Fragen")
        print("Antwort (2): Orientierungsfragen")
        print("Antwort (3): Wichtige Fragen, die der Disponent für eine erfolgreiche Alarmierung der Einsatzkräfte benötigt")
        answer = int(input("Wähle eine Antwort aus: "))
        if answer == 3:
            points += 1 
        
        print("Du hast", points, "von 6 Punkten.")
    
    if points >= 3: 
        print("Du hast bestanden und bist bereit, Leben zu retten!")
    else:
        print("Du hast leider nicht bestanden, aber gib nicht auf!")
        
    print("Wenn du ein Lebensretter sein willst, frag bei deiner örtlichen Feuerwehr/DRK-Bereitschaft nach!")  
    print("Vielen Dank für dein Spiel!")
