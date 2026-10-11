import time
import data_dictionaries as data

# tracks game state across levels 
game_state = {
    "elephant_number": None,
    "elephant_type": "Normal",
    "dwarven_level": 0,
    "hunger": 25,
    "bloodlust": 0
}

# displays Hunger or Bloodlust bar 
def display_bar(name,percentage):
    bar_length = 20
    filled = int(percentage/100 * bar_length)
    empty = bar_length - filled 

    bar = "█" * filled + " " * empty

    print(f"{name}: [{bar}] {percentage}%")
   
# Choice validation. 
# checks if input is A B or C
# player gets 3 warinings or the game restarts
#stretch goal - make them play guess the letter ?
# failure counts as a death 
def A_B_or_C(choice):
    A_B_C_count = 0
    while A_B_C_count < 3 and choice not in ("A", "B", "C"):
        A_B_C_count += 1
        choice = input("enter choice:")
        if A_B_C_count == 1:
          print_lines(data.dialogue["multiple_choice_warnings"]["warning_1"])
        elif A_B_C_count == 2:
            print_lines(data.dialogue["multiple_choice_warnings"]["warning_2"]) 
        elif A_B_C_count == 3:
            print_lines(data.dialogue["multiple_choice_warnings"]["warning_3"])
        else:
            A_B_C_count = 0
            ending = "no_letters"
            return ending
    return choice

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
# Use print_lines(dialogue_chunks) instead of print() for narration.
def print_lines(chunks):
     # Wrap single dialogue entries in a list.
    if isinstance(chunks, dict):
        chunks = [chunks]

    for chunk in chunks:
        text = chunk["text"].format(**game_state)
        speed = chunk.get("speed", "normal")
        pause = chunk.get("pause", "normal")

        type_text(text, speed, data.TEXT_PAUSE.get(pause, 0.3))


# Checks if the number of elephants is a float or negative, 
# used in choose_num_of_elephants
def is_float_or_negative(number_of_elephants):
    try:
        number_of_elephants = float(number_of_elephants)

        if not number_of_elephants.is_integer() or number_of_elephants < 0:
            return None, "float"

        return int(number_of_elephants), None

    except ValueError:
        return None, "string" 

# level 1 
# player chooses how many elephants they want 
# 3 warnings for entering a float or negative
# 3 warnings for > 50
# optimum answer is 50 
# assigns a number of elepahnts and an ending 
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

# checks if ending has been achieved and prints it. 
def show_ending(ending):
    if ending is not None:
        print_lines(data.dialogue["endings"][ending])
        death_count += 1


def what_elephants_eat():

number_of_elephants, ending = choose_num_of_elephants()

show_ending(ending)

if ending is None:
    # Continue to the elephant diet level
    pass   


    
      






   