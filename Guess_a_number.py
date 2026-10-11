import time
import data_dictionaries as data

# tracks game state across levels 
game_state = {
    "elephant_number": None,
    "elephant_type": "Normal",
    "elephant_diet": None,
    "dwarven_level": "none",
    "hunger": 25,
    "bloodlust": 0,
    "ending" : None,
    "death_count": 0,
    "has_phrasebook" : False,
    "dwarven_reputation": 0 
}

# Resets game states after run
# Dwarven level and totals deaths persist 
def reset_game():
        game_state["elephant_number"] = None
        game_state["elephant_type"] = "Normal"
        game_state["elephant_diet"] = None
        game_state["hunger"] = 25
        game_state["bloodlust"] = 0
        game_state["ending"] = None
        game_state["has_phrasebook"] = False
        game_state["dwarven_reputation"]= 0 

   
# Choice validation. 
# checks if input is A B or C
# Player gets 3 warinings or the game restarts.
#stretch goal - make them play guess the letter ?
# failure counts as a death 
def A_B_or_C():
    A_B_C_count = 0

    while True:

        choice = input("\nEnter choice: ").upper()

        if choice in ("A", "B", "C"):
            return choice, None
         
        A_B_C_count += 1

        if A_B_C_count == 1:
          print_lines(data.dialogue["multiple_choice_warnings"]["warning_1"])

        elif A_B_C_count == 2:
            print_lines(data.dialogue["multiple_choice_warnings"]["warning_2"]) 

        elif A_B_C_count == 3:
            print_lines(data.dialogue["multiple_choice_warnings"]["warning_3"])

        else:
           return None, "no_letters" 
   

# Prints text one character at a time at a chosen speed,
# then pauses before allowing the next line to print. 
def type_text(text, speed="normal", pause=0.3):
    delay = data.TEXT_SPEED.get(speed, 0.04)

    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)

    print()
    time.sleep(pause)

# Retrieves dialogue text and its speed/pause settings.
# Formats dynamic values and sends each line to type_text().
# Use print_lines(dialogue_chunks) instead of print() for narration. - !!!I should make a word doc for dialogue paths 
def print_lines(chunks):
     # Wrap single dialogue entries in a list.
    if isinstance(chunks, dict):
        chunks = [chunks]

    for chunk in chunks:
        text = chunk["text"].format(**game_state)
        speed = chunk.get("speed", "normal")
        pause = chunk.get("pause", "normal")

        type_text(text, speed, data.TEXT_PAUSE.get(pause, 0.3))

# displays Hunger or Bloodlust bar 
def display_bar(name,percentage):
    bar_length = 20
    filled = int(percentage/100 * bar_length)
    empty = bar_length - filled 

    bar = "█" * filled + " " * empty

    print(f"\n{name}: [{bar}] {percentage}%")

# Checks if the number of elephants is a float or negative. 
# Used in choose_num_of_elephants.
def is_float_or_negative(number_of_elephants):
    try:
        number_of_elephants = float(number_of_elephants)

        if not number_of_elephants.is_integer() or number_of_elephants < 0:
            return None, "float"

        return int(number_of_elephants), None

    except ValueError:
        return None, "string" 
    
# checks if ending has been achieved and prints it. 
def show_ending():
        if game_state["ending"] is not None:
            print_lines(data.dialogue["endings"][game_state["ending"]])
            game_state["death_count"] += 1
            print_lines(data.dialogue["death_reboot"])
            return True
        
        return False

# Level 1 
# Player chooses how many elephants they want. 
# 3 warnings for entering a float or negative.
# 3 warnings for > 50
# optimum answer is 50 
# Assigns a number of elepahnts and an ending. 
def choose_num_of_elephants():
    ending = None 

    invalid_input_count = 0
    too_high_count = 0
    lower_hint_count = 0 

    awaiting_lower_response = False
    previous_guess = None

    # Display introduction dialogue 
    print_lines(data.dialogue["levels"]["level_1"]["intro"])

    # main input loop 
    while ending is None:
        # Check for a float or negative
        raw_input = input("\nEnter guess:")
        game_state["elephant_number"] = raw_input
        number_of_elephants, input_error = is_float_or_negative(raw_input)
        
        
        
        # Three warnings for entering a float or negative 
        if input_error is not None:
    
            invalid_input_count += 1 

            if invalid_input_count == 1:
                print_lines(data.dialogue["levels"]["level_1"]["invalid_integer"]["warning_1"])

            elif invalid_input_count == 2:
                print_lines(data.dialogue["levels"]["level_1"]["invalid_integer"]["warning_2"])
            
            elif invalid_input_count == 3:
                print_lines(data.dialogue["levels"]["level_1"]["invalid_integer"]["warning_3"])

            else:
                ending = input_error

                print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"]) 
                print_lines(data.dialogue["levels"]["level_1"]["number_comment"]["invalid"])
                
            continue

         # Update game state with valid guess
        game_state["elephant_number"] = number_of_elephants
        
        
        # check for exactly 50 
        if number_of_elephants == 50:
            
            if invalid_input_count == 0 and lower_hint_count == 0 and too_high_count == 0:
                game_state["elephant_type"] = "shiny"
                print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["shiny"])
                print_lines(data.dialogue["levels"]["level_1"]["purpose"])
            else:
                print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"]) 
                print_lines(data.dialogue["levels"]["level_1"]["purpose"])

            return (50,None)   
        
        # check for 0 
        elif number_of_elephants == 0:
            print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"]) 
            print_lines(data.dialogue["levels"]["level_1"]["number_comment"]["invalid"])
            return (number_of_elephants,"zero_elephants")

        # check for < 50
        elif number_of_elephants < 50:
            print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"])
            print_lines(data.dialogue["levels"]["level_1"]["number_comment"]["too_low"])

            return(number_of_elephants,None)
        
        # check for > 50
        else:
            too_high_count += 1
            # check if last response was a lower hint
            # if player guesses higher after a lower hint returns their guess 
            if awaiting_lower_response:

                if number_of_elephants >= previous_guess:
                    print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["ignored_lower"])
                    print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"])
                    print_lines(data.dialogue["levels"]["level_1"]["number_comment"]["too_high"])
                    return(number_of_elephants,None)
                
                awaiting_lower_response = False
                
        # 2 warnings for > 50  
            if too_high_count == 1:
                print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["warning_1"])
            
            elif too_high_count == 2:
                print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["warning_2"])
            
            # lower hint will show 3 times unless new guess > previous guess 
            else:
                if lower_hint_count < 3:
                    print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["lower"])
                    lower_hint_count += 1
                    awaiting_lower_response = True
                    previous_guess = number_of_elephants
                else:
                    print_lines(data.dialogue["levels"]["level_1"]["number_statement"]["normal"])
                    print_lines(data.dialogue["levels"]["level_1"]["number_comment"]["too_high"])
                    return(number_of_elephants,None)

        
    return(number_of_elephants,ending)


# Level 2 
# Player chooses elephant diet.
# Hunger and bloodlust stats updtated.
def what_elephants_eat():
    print_lines(data.dialogue["levels"]["choose_elephant_diet"]["intro"])
    display_bar("Hunger", game_state["hunger"])
    print_lines(data.dialogue["levels"]["choose_elephant_diet"]["choices"])
   
    choice, ending = A_B_or_C()

    if ending is not None:
        return ending 
    
    if choice == "A":
        game_state["elephant_diet"] = "trees"
        game_state["hunger"] = 50
        game_state["bloodlust"] = 0

        print_lines(data.dialogue["levels"]["choose_elephant_diet"]["outcomes"]["trees"])
        

    elif choice == "B":
        game_state["elephant_diet"] = "mushrooms"
        game_state["hunger"] = 30
        game_state["bloodlust"] = 0

        print_lines(data.dialogue["levels"]["choose_elephant_diet"]["outcomes"]["mushrooms"])

    elif choice == "C":
        game_state["elephant_diet"] = "dwarves"
        game_state["hunger"] = 10
        game_state["bloodlust"] = 50

        print_lines(data.dialogue["levels"]["choose_elephant_diet"]["outcomes"]["dwarves"])

    display_bar("Hunger", game_state["hunger"])

    if game_state["bloodlust"] > 0:
         display_bar("Bloodlust", game_state["bloodlust"])

    return None     

#Travel to Level 3.
#Decreases elephant hunger by 5 
#Sets bloodlust to 75
#Prints changes 
def travel_to_dwarves():
    print_lines(data.dialogue["levels"]["travel_to_dwarves"]["before_status"])

    game_state["hunger"] -= 5
    display_bar("Hunger", game_state["hunger"])

    if game_state["elephant_diet"] == "dwarves":
        game_state["bloodlust"] = 75
        display_bar("Bloodlust", game_state["bloodlust"])

    print_lines(data.dialogue["levels"]["travel_to_dwarves"]["after_status"])
    return None

def ending_and_reset():
    if show_ending():
        reset_game()
        return True
    return False

# determines outcome of dwarf attack routes 
# Used in dwarf_encounter()
def dwarf_attack():
    if game_state["bloodlust"] < 100:
        return "attack_no_bloodlust"   

    elif game_state["elephant_number"] < 50:
        return "attack_failed"
    
    else:
        print_lines(data.dialogue["levels"]["dwarf_encounter"]["attack"]["successful_before_status"])
        
        game_state["hunger"] = 100
        game_state["dwarven_reputation"] -= 1000
        game_state["has_phrasebook"] = True
        game_state["bloodlust"] = 0

        display_bar("Hunger", game_state["hunger"])
        display_bar("Bloodlust", game_state["bloodlust"])

        print_lines(data.dialogue["levels"]["dwarf_encounter"]["attack"]["successful_after_status"])
    
    return None

# L3 
# Player chooses attack/diplomacy/Run
# Diplomacy sucess depends on dwarven level AND no bloodlust
# Attack success depends on bloodlust AND elephants > 50
# Dwarven phrasebook aquired on sucessful attack. 
def dwarf_encounter():
    print_lines(data.dialogue["levels"]["dwarf_encounter"]["intro"])

    if game_state["elephant_number"] < 50:

        print_lines(data.dialogue["levels"]["dwarf_encounter"]["below_50"])

    if game_state["elephant_diet"] == "dwarves":

        print_lines(data.dialogue["levels"]["dwarf_encounter"]["dwarf_diet"])
        game_state["bloodlust"] = 100

    game_state["hunger"] -= 5 
    display_bar("Hunger", game_state["hunger"])

    if game_state["bloodlust"] > 0 :

        display_bar("Bloodlust", game_state["bloodlust"])

    print_lines(data.dialogue["levels"]["dwarf_encounter"]["choices"]) 
    
    choice,ending = A_B_or_C()   

    if ending is not None:

        return ending
    

    if choice == "A":

        ending = dwarf_attack()

        if ending is not None:
            return ending
        route = "attack"

    elif choice == "B":

        print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["warning_intro"]) 
        print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["dwarven_warning"][game_state["dwarven_level"]])

        if game_state["dwarven_level"] == "none":
            return "diplomacy_none"

        elif game_state["dwarven_level"] == "basic":
            return "diplomacy_basic" 
        
        elif game_state["dwarven_level"] == "intermediate":
            return "diplomacy_intermediate"
        
        elif game_state["dwarven_level"] == "conversational":

            if game_state["elephant_type"] == "shiny":
                print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["conversational"]["shiny"])

                game_state["dwarven_reputation"] += 100

            else:
                print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["conversational"]["normal"])

            print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["shared_success"])    

            if game_state["bloodlust"] == 100:
                print_lines(data.dialogue["levels"]["dwarf_encounter"]["diplomacy"]["bloodlust_override"])

                ending = dwarf_attack()

                if ending is not None:
                    return ending
                
                route = "attack" 
                
            else:    
                game_state["hunger"] = 100
                display_bar("Hunger", game_state["hunger"])
                route = "diplomacy"

    elif choice == "C":
        return "dwarf_run" 

    if route == "attack":
        print_lines( data.dialogue["levels"]["dwarf_encounter"]["next_level"]["attack"])

    elif route == "diplomacy":
        print_lines( data.dialogue["levels"]["dwarf_encounter"]["next_level"]["diplomacy"])

    return None 

# Final level
def bridge():
    print_lines(data.dialogue["levels"]["bridge"]["intro"])

    if game_state["has_phrasebook"] == True:
        print_lines(data.dialogue["levels"]["bridge"]["choices"]["phrasebook"])

    else:
        print_lines(data.dialogue["levels"]["bridge"]["choices"]["normal"])
    
    choice, ending = A_B_or_C

    if ending is not None:
        return ending
    
    # Attack route 
    if choice == "A":

        # If you have phrasebook and try to cross
        # dwarf survivour insults you and cuts bridge 
        if game_state["has_phrasebook"] == True:
            # translate according to dwarven level
            print_lines(data.dialogue["levels"]["bridge"]["survivor"]["insult"][game_state["dwarven_level"]]) 
            print_lines(data.dialogue["levels"]["bridge"]["survivor"]["after_insult"]) 
            return "bridge_sabotage"
        
        # Elephants > 50, bridge collapses
        elif game_state["elephant_number"] > 50:
            return "bridge_collapse"
        
        # No phrasebook and elephants < 50. Sucessful crossing! 
        else:
            print_lines(data.dialogue["levels"]["bridge"]["survivor"]["after_insult"]) 

    # Find another route 
    elif choice == "B":
        return "no_route"
    
    # REST or READ 
    elif choice == "C":

        # Rest ending 
        if game_state["has_phrasebook"] == False:
            print_lines(data.dialogue["levels"]["bridge"]["rest"])
            return "elephants_wander_off"
        
        # Read phrasebook
        else:
            print_lines(data.dialogue["levels"]["bridge"]["phrasebook"][game_state["dwarven_level"]])

            # Upgrade dwarven proficiency 
            if game_state["dwarven_level"] == "none":

                game_state["dwarven_level"] = "basic"

            elif game_state["dwarven_level"] == "basic":

                game_state["dwarven_level"] = "intermediate"

            elif game_state["dwarven_level"] == "intermediate":

                game_state["dwarven_level"] = "conversational"
                
            return "elephants_wander_off"


# Main gameplay loop.
# Will restart after a death. 
def main():

    while True:

        #LEVEL 1 : How many Elephants?
        number_of_elephants, ending = choose_num_of_elephants()
        game_state["ending"] = ending

        if ending_and_reset():
            continue
        

        # LEVEL 2 : What do they eat?
        game_state["ending"] = what_elephants_eat()

        if ending_and_reset():
            continue

        # Travel 
        travel_to_dwarves()

        #LEVEL 3 : Dwarves 
        game_state["ending"] = dwarf_encounter()

        if ending_and_reset():
            continue
        
        #LEVEL 4 : Bridge
        game_state["ending"] = bridge()

        if game_state["ending"] == "good_ending":

            print_lines(data.dialogue["levels"]["bridge"]["good_ending"])
            print_lines(data.dialogue["final_stats"])

            break

        if ending_and_reset():
            continue


main()



    






 


    
      






   