# =================================================================
# FATE ACCELERATED NPC GENERATOR
# =================================================================
import random

# Listen von möglichen Elementen für die NPC-Generierung
OCCUPATIONS = [
    "Gelehrte", "Händlerin", "Abenteurerin", "Magierin", "Musikerin",
    "Entdeckerin", "Mechanikerin", "Pilotin", "Ermittlerin", "Künstlerin"
]

PERSONALITIES = [
    "neugierige", "vorsichtige", "mutige", "scharfsinnige", "eigensinnige",
    "kreative", "loyale", "ehrgeizige", "geheimnisvolle", "enthusiastische"
]

GOALS = [
    "sucht nach uraltem Wissen",
    "will ein legendäres Artefakt finden",
    "möchte die eigene Vergangenheit aufdecken",
    "strebt nach wissenschaftlichem Durchbruch",
    "plant eine große Expedition",
    "will eine alte Schuld begleichen",
    "sucht nach verschwundenen Freunden",
    "möchte eine neue Erfindung vollenden",
    "will ein Geheimnis bewahren",
    "strebt nach Gerechtigkeit"
]

TROUBLES = [
    "wird von Rivalen verfolgt",
    "hat eine gefährliche Entdeckung gemacht",
    "trägt ein verfluchtes Armulett",
    "hat mächtige Feinde",
    "wird von der Vergangenheit eingeholt",
    "hat ein gefährliches Versprechen gegeben",
    "besitzt ein gefährliches Artefakt",
    "hat ungewollt eine Prophezeiung ausgelöst",
    "wurde in eine Verschwörung verwickelt",
    "muss ein dunkles Geheimnis hüten"
]

def generate_approaches():
    """Generiert die sechs Approaches mit passenden Werten"""
    approaches = {
        "Sorgfältig": 0, "Clever": 0, "Auffällig": 0,
        "Kraftvoll": 0, "Flink": 0, "Heimlich": 0
    }
    
    # Ein Approach auf +2, zwei auf +1, zwei auf +0, einer auf -1
    values = [2, 1, 1, 0, 0, -1]
    random.shuffle(values)
    
    for i, approach in enumerate(approaches.keys()):
        approaches[approach] = values[i]
    
    return approaches

def generate_npc():
    """Generiert einen kompletten NPC"""
    # Basis-Eigenschaften
    occupation = random.choice(OCCUPATIONS)
    personality = random.choice(PERSONALITIES)
    
    # Aspekte
    high_concept = f"{personality} {occupation}"
    trouble = random.choice(TROUBLES)
    
    # Ziele
    goal = random.choice(GOALS)
    
    # Approaches
    approaches = generate_approaches()
    
    # Formatierte Ausgabe
    npc = f"""
=== FATE NPC ===
Konzept: {high_concept}
Problem: {trouble}
Ziel: {goal}

Approaches:
"""
    
    # Approaches sortiert nach Wert ausgeben
    sorted_approaches = sorted(approaches.items(), key=lambda x: x[1], reverse=True)
    for approach, value in sorted_approaches:
        sign = "+" if value >= 0 else ""
        npc += f"- {approach}: {sign}{value}\n"
    
    return npc

def main():
    """Hauptprogramm"""
    print("=== FATE NPC GENERATOR ===")
    print("Drücke Enter für einen neuen NPC oder 'q' zum Beenden.")
    
    while True:
        eingabe = input("\nNeuer NPC? ")
        if eingabe.lower() == 'q':
            break
        
        print(generate_npc())

if __name__ == "__main__":
    main()
