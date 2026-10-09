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

# Checks if the number of elephants is a float or negative 
def is_float_or_negative(number_of_elephants)
    try:
        number_of_elephants = float(number_of_elephants)

        if not number_of_elephants.is_integer() and number_of_elephants < 0:
            return None, "float"

        return int(number_of_elephants), None

    except ValueError:
        return None, "string" 

def choose_num_of_elephants(number_of_elephants):
    elephant_type = "Normal"
    number_of_elephants = None
    ending = None 

    invalid_input_count = 0
    too_high_count = 0
    lower_hint_count = 0 
    
    # Display introduction dialogue 
    print_lines(data_dictionaries.dialogue["levels"]["level_1"]["intro"])

    # main input loop 
    while ending is None:
        number_of_elephants = input("Enter guess:") # add to dict or make it loop to the intro?
        
        # Check for a float or negative 
        number_of_elephants, input_error = is_float_or_negative(player_input)
        
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






    # Will still accept a non numeric answer after 3 attempts 
    if not number_of_elephants.isdigit():
        return(number_of_elephants)

    # Converts a numeric 
    number_of_elephants = int(number_of_elephants)

    # cryptic hints > 50 is too high
    if number_of_elephants > 50:
       input_is_bigger_50_count += 1
       while not input_is_bigger_50_count < 5:
        input_is_bigger_100_count += 1

        if input_is_bigger_50_count is 1:
            number_of_elephants = input(print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["warning_1"]))

        elif input_is_bigger_50_count == 2:
            number_of_elephants = input(print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["warning_2"]))

        elif input_is_bigger_50_count > 3:
             # fix this 
            lower_hint_count += 1
            print_lines(data.dialogue["levels"]["level_1"]["too_high_warning"]["lower"])

           
            previous_guess = number_of_elephants
            lower_hint_elephants = int(input())
            if lower_hint_count > 1 and lower_hint_elephants > 
            
    :



        elif input_is_bigger_50_count is 5:
            return(number_of_elephants)
     


    elif (
    number_of_elephants == 50
    and enter_num_count_is_int_count == 0
    and enter_num_count_is_bigger_100_count == 0 ):
        elephant_type = "Shiny"
        return number_of_elephants, elephant_type 
        
if not number_of_elephants.isdigit():
        print(f"Fine, you have {number_of_elephants} elephants. Good luck with that.")