import time

# speed setting dict for text_type fuction
TEXT_SPEED = {
    "extremely_slow": 0.2, 
    "slow": 0.08,
    "normal": 0.04,
    "fast": 0.01
}

# controls speed of narration and adds a pause after each line. 
# use type_text(text, speed, pause) instead of print() for dialogue
def type_text(text, speed=0.04, pause=0.3):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(speed)

    print()
    time.sleep(pause)



type_text("Guess the number?")
type_text("LOWER", 0.15)
type_text("You have 50 elephants.", 0.01)

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