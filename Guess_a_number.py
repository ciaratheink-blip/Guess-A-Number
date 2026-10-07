import time
import data_dictionaries as data

# 
def type_text(text, speed="normal", pause=0.3):
    delay = data.TEXT_SPEED.get(speed, 0.04)

    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)

    print()
    time.sleep(pause)

# controls speed of narration and adds a pause after each line. 
# Prints dialogue using speeds and pauses stored in the dialogue dictionary.
# Use print_lines(dialogue_chunks) instead of print() for narration.
def print_lines(chunks):
    for chunk in chunks:
        text = chunk["text"]
        speed = chunk.get("speed", "normal")
        pause = chunk.get("pause", 0.3)

        type_text(text, speed, pause)

print_lines(dialogue["endings"]["string"])




def choose_num_of_elephants(number_of_elephants, elephant):
    enter_num_count_is_int_count = 0
    enter_num_count_is_bigger_100_count = 0
    elephant_type = "Normal"

    # Try to get a numeric answer
    while not number_of_elephants.isdigit() and enter_num_count_is_int_count < 3:
        enter_num_count_is_int_count += 1
        number_of_elephants = input("That is not a number: ")

    # Will still accept a non numeric answer afte 3 attempts 
    if not number_of_elephants.isdigit():
        return(number_of_elephants)

    # Converts a numeric 
    number_of_elephants = int(number_of_elephants)


    if number_of_elephants > 100:
       while not number_of_elephants < 3:
        enter_num_count_is_bigger_100_count += 1
        if enter_num_count_is_bigger_100_count == 1:
            number_of_elephants = input("Pick a better number: ")
        elif enter_num_count_is_bigger_100_count == 2:
            number_of_elephants = input("Try something sensible: ")
        elif enter_num_count_is_bigger_100_count > 3:
            number_of_elephants = input("LOWER: ")
        elif enter_num_count_is_bigger_100_count > 5:
            return(number_of_elephants)
     


    elif (
    number_of_elephants == 50
    and enter_num_count_is_int_count == 0
    and enter_num_count_is_bigger_100_count == 0 ):
        elephant_type = "Shiny"
        return number_of_elephants, elephant_type 
        
if not number_of_elephants.isdigit():
        print(f"Fine, you have {number_of_elephants} elephants. Good luck with that.")