print("<==================================================================================>")
name = input("Who are you? ")
print()
print("Welcome", name, ". Choose your class")
print()
# Present class choices with their stats
print("1. Elf    |Intelligence: 4|Survival: 6")
print("2. Warlock |Intelligence: 3|Survival: 7") 
print("3. Bard    |Intelligence: 4|Survival: 6")
print("4. Paladin |Intelligence: 5|Survival: 5")

chosen_class = input("Choose your class (1-4): ")

# Assign character stats based on class choice
if chosen_class == "1":
    intelligence = 4
    survival = 6
    class_name = "Elf"
elif chosen_class == "2":
    intelligence = 3
    survival = 7
    class_name = "Warlock"
elif chosen_class == "3":
    intelligence = 4
    survival = 6
    class_name = "Bard"
elif chosen_class == "4":
    intelligence = 5
    survival = 5
    class_name = "Paladin"
else:
    # Default class if invalid choice is made
    intelligence = 1
    survival = 6
    class_name = "Jester"

print()
print(f"Alright, you are now a {class_name}")
print()

# First major story decision point
print(f"After a long journey, {name}, you find yourself at a crossroads.")
print("The left path leads into a deep and dark part of the forest.")
print("The right path follows a river into a valley.")
print("The path ahead continues through open countryside.")
print("1: Take the left path")
print("2: Take the right path")
print("3: Continue forward")

choice = input("What is your choice (1-3)? ")
print()

# Branch storyline based on path choice
if choice == "1":
    # Forest path storyline
    print("You venture into the dark forest.")
    print("While walking, you notice ancient intertwined trees, hear a loud waterfall,")
    print("and spot a small forest clearing, but you keep going.")
    print("Soon you find an abandoned pouch on the ground.")
    print("1: Pick up the pouch")
    print("2: Leave it alone")
    
    # Decision about the pouch
    pouch_choice = input("What do you do (1-2)? ")
    
    if pouch_choice == "1":
        # Consequence of taking the pouch
        print("As you reach for the pouch, you hear something rushing toward you from behind.")
        print("Something grabs and pulls at you!")
        # Present options based on character stats
        print(f"1: Try to fight back (Required Survival: 6, You have: {survival})")
        print(f"2: Try to reason with it (Required Intelligence: 5, You have: {intelligence})")
        print("3: Try to break free")
        
        combat_choice = input("What do you do (1-3)? ")
        # Future expansion: Add combat system and stat checks
        
    else:
        # Alternative path if pouch is ignored
        print("You decide to leave the area. Where do you go next?")
        print("1: Deeper into the dark forest")
        print("2: Return to the tavern where you started")
        print("3: Toward the sound of the waterfall")
        print("4: To the forest clearing")
        
        direction = input("Which way (1-4)? ")
        # Future expansion: Add more locations and events

elif choice == "2":
    # River valley path storyline
    print("You follow the river path into the valley...")
    # Future expansion: Add river valley adventures

else:
    # Countryside path storyline
    print("You continue along the countryside path...")
    # Future expansion: Add countryside adventures
