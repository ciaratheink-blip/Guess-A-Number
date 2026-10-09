import time
import data_dictionaries as data

elephant_number = 0
elephant_state = "normal"

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
        text = chunk["text"].format(elephant_number=elephant_number)
        speed = chunk.get("speed", "normal")
        pause = chunk.get("pause", "normal")

        type_text(text, speed, data.TEXT_PAUSE.get(pause, 0.3))

print_lines(data.dialogue["endings"]["string"])

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

# player chooses how many elephants they want 
# 3 warnings for entering a float or negative
# 3 warnings for > 50
# assigns a number of elepahnts and an ending 
def choose_num_of_elephants():
    elephant_type = 'Normal'
    ending = None 

    invalid_input_count = 0
    too_high_count = 0
    lower_hint_count = 0 

    awaiting_lower_response = False
    previous_guess = None

    # Display introduction dialogue 
    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["intro"])

    # main input loop 
    while ending is None:
        number_of_elephants = input('Enter guess:') # add to dict or make it loop to the intro?
        
        # Check for a float or negative 
        number_of_elephants, input_error = is_float_or_negative(number_of_elephants)
        
        # Three warnings for entering a float or negative 
        if input_error is not None:
    
            invalid_input_count += 1 

            if invalid_input_count == 1:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["invalid_integer"]["warning_1"])

            elif invalid_input_count == 2:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["invalid_integer"]["warning_2"])
            
            elif invalid_input_count == 3:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["invalid_integer"]["warning_3"])

            else:
                ending = input_error
                
            continue
        
        # convert to integer 
        number_of_elephants = int(number_of_elephants)
        
        # check for exactly 50 
        if number_of_elephants == 50:
            
            if invalid_input_count == 0 and lower_hint_count == 0 and too_high_count == 0:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_statement"]["normal"])
                
            else:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_statement"]["shiny"]) 

            return (50,None)   
        
        # check for 0 
        elif number_of_elephants == 0:
            return (number_of_elephants,"zero_elephants")

        # check for < 50
        elif number_of_elephants < 50:
            print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_statement"]["normal"])
            print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_comment"]["too_low"])

            return(number_of_elephants,None)
        
        # check for > 50
        else:
            too_high_count += 1
            # check if last response was a lower hint
            # if player guesses higher after a lower hint returns their guess 
            if awaiting_lower_response:

                if number_of_elephants >= previous_guess:
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["too_high_warning"]["ignored_lower"])
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_statement"]["normal"])
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_comment"]["too_high"])
                    return(number_of_elephants,None)
                
                awaiting_lower_response = False
                
        # 2 warnings for > 50  
            if too_high_count == 1:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["too_high_warning"]["warning_1"])
            
            elif too_high_count == 2:
                print_lines(data_dictionaries.dialogue["levels"]["level_1"]["too_high_warning"]["warning_2"])
            
            # lower hint will show 3 times unless new guess > previous guess 
            else:
                if lower_hint_count < 3:
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["too_high_warning"]["lower"])
                    lower_hint_count += 1
                    awaiting_lower_response = True
                    previous_guess = number_of_elephants
                else:
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_statement"]["normal"])
                    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["number_comment"]["too_high"])
                    return(number_of_elephants,None)

        
    return(number_of_elephants,ending)

           

    
      






   