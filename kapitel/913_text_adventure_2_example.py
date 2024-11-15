# Get player name and introduction
name = input("Please enter your character name: ")
print("Welcome", name)
print("You're a Dark Elf who teamed up with three other adventurers (a Forest Walker, a Blood Mage, and a Dragon Knight) "
      "to find a cure for a mysterious illness that's slowly consuming your mind. "
      "Your quest led you to Forest Haven where a powerful druid was supposed to help, but they've been missing for a month. "
      "Now there's a horde of raiders with their Dark Elf leader at Forest Haven's gates. "
      "The leader is trying to convince you to open the gate and let everyone in, "
      "while threatening to kill the guardian of Forest Haven.")
print("(Dark Elves are ancient beings who once ruled vast underground kingdoms)")

# First major choice: Loyalty decision
choice_a = "Listen to the raiders"
choice_b = "Stay loyal to the people of Forest Haven"

print("A:", choice_a)
print("B:", choice_b)

# Get player's first decision
decision = input("Choose your next action (A/B): ").lower()

if decision == "a":
    # Path: Side with raiders
    print("You decided to listen to the raiders")
    choice_c = "Attack the leader before they attack you"
    choice_d = "Quickly open the gate before the defenders can stop you"
    print("C:", choice_c)
    print("D:", choice_d)
    
    next_action = input("What do you want to do (C/D)? ").lower()
    
    if next_action == "c":
        # Combat outcome
        print("You were forced back and fell from the battlements")
    elif next_action == "d":
        # Betrayal path
        print("You opened the gate and the raiders pour into the settlement, attacking everyone. "
              "Their leader wants to speak with you.")
        choice_e = "Talk to them (your party disapproves)"
        choice_f = "Attack them (they're much stronger than you)"
        print("E:", choice_e)
        print("F:", choice_f)
        
        final_choice = input("What will it be (E/F)? ").lower()
        
        if final_choice == "e":
            print("Your party abandoned you, disgusted by your betrayal")
        elif final_choice == "f":
            print("They proved too powerful and defeated you")

elif decision == "b":
    # Path: Stay loyal
    print("A battle erupts. Choose your weapon:")
    choice_g = "Blade"
    choice_h = "Staff"
    print("G:", choice_g)
    print("H:", choice_h)
    
    weapon = input("Which one (G/H)? ").lower()
    
    if weapon == "g":
        # Combat outcome - blade
        print("You stand atop the wall. The raiders attack with arrows and magic, "
              "while you have no way to strike back.")
        print("You fall in battle")
    elif weapon == "h":
        # Combat outcome - staff
        print("You and your companions successfully repel the raiders with powerful magic! "
              "The guardian of Forest Haven requests your presence.")
        choice_i = "Speak with them"
        choice_j = "Leave Forest Haven and travel to the Great City"
        print("I:", choice_i)
        print("J:", choice_j)
        
        next_decision = input("Choose wisely (I/J): ").lower()
        
        if next_decision == "j":
            print("You lived in the Great City briefly before succumbing to your illness")
        elif next_decision == "i":
            # Continue story with rescue quest
            print("They tell you that the Elder Druid went missing while investigating "
                  "the raiders' stronghold. They warn you of the dangers - hundreds of raiders "
                  "and several dark mystics guard the place. They provide you with supplies.")
            choice_k = "Leave for the Great City"
            choice_l = "Rescue the Elder Druid"
            print("K:", choice_k)
            print("L:", choice_l)
            
            quest_choice = input("What will you do? (Finding the Elder Druid might save your life) (K/L): ").lower()
            
            if quest_choice == "k":
                print("You lived briefly in the Great City before your illness claimed you")
            elif quest_choice == "l":
                # Infiltration mission
                print("You reach the raiders' stronghold. Your party must decide how to enter.")
                choice_m = "Search for a hidden entrance"
                choice_n = "Launch a direct assault"
                print("M:", choice_m)
                print("N:", choice_n)
                
                infiltration = input("How will you enter the stronghold? (M/N): ").lower()
                
                if infiltration == "m":
                    # Stealth path
                    print("While scouting the perimeter, you spot guards at the main gate.")
                    choice_o = "Try to fight through the main entrance"
                    choice_p = "Look for a way to the upper levels"
                    print("O:", choice_o)
                    print("P:", choice_p)
                    
                    stealth_choice = input("Choose wisely (O/P): ").lower()
                    
                    if stealth_choice == "o":
                        print("The guards raise the alarm. You're quickly overwhelmed by raiders.")
                        print("Your journey ends here")
                    elif stealth_choice == "p":
                        # Continue stealth mission
                        print("You sneak past some sleeping guards and discover a secret passage.")
                        print("Q: Carefully make your way to the dungeons")
                        print("R: Try to question a sleeping guard")
                        
                        next_move = input("What do you want to do? (Q/R): ").lower()
                        
                        if next_move == "q":
                            # Prison break attempt
                            print("You find the dungeon but the Elder Druid's cell is locked. "
                                  "You need to find the key.")
                            print("S: Try to steal keys from the guards")
                            print("T: Search the storage rooms")
                            
                            key_choice = input("Where will you search? (S/T): ").lower()
                            
                            if key_choice == "s":
                                print("You manage to steal the keys without being detected")
                                print("A: Free the Elder Druid immediately")
                                print("B: Search the vault first")
                                
                                final_decision = input("What will you do with the keys? (A/B): ").lower()
                                
                                if final_decision == "a":
                                    print("The Elder Druid helps cure your illness. "
                                          "Together you escape to the Great City.")
                                    print("To be continued...")
                                elif final_decision == "b":
                                    print("You find great wealth but lose precious time. "
                                          "The illness claims you within half a year.")
                            elif key_choice == "t":
                                print("Guards discover you searching the storage rooms")
                                print("Your quest ends here")
                        elif next_move == "r":
                            print("The guard wakes and raises the alarm")
                            print("You're quickly captured")
                elif infiltration == "n":
                    print("The raiders' numbers are too great. "
                          "Your small party cannot hope to defeat them all!")
                    print("Your attack fails and you are overwhelmed")
                    print("Your story ends here")
