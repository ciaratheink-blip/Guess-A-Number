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




def choose_num_of_elephants(number_of_elephants):
    input_not_int_count = 0
    input_is_bigger_50_count = 0
    elephant_type = "Normal"
    

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