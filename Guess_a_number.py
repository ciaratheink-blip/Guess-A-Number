import time

# speed setting dict for text_type fuction
TEXT_SPEED = {
    "extremely_slow": 0.2, 
    "slow": 0.08,
    "normal": 0.04,
    "fast": 0.01
}

# Dialogue dictionary (first scene written)
dialogue = {
    "death_reboot": {
        "text": r"""
+----------------------------+
|         DEATHLOGIC         |
|         INITIALISED        |
+----------------------------+
""",
        "speed": "fast"
    },

    "levels": {
        "level_1": {
            "intro": {
                "guess": {
                    "text": "Guess the number?",
                    "speed": "normal"
                },
                "warning": {
                    "text": "Enter whole numerals only or face the consequences.",
                    "speed": "slow"
                }
            },

            "number_statement": {
                "normal": {
                    "text": "You have {elephant_number} elephants.",
                    "speed": "normal"
                },
                "shiny": {
                    "text": "You have {elephant_number} {elephant_state} elephants.",
                    "speed": "normal"
                }
            },

            "number_comment": {
                "too_high": {
                    "text": "What a ridiculous number of elephants.",
                    "speed": "slow"
                },
                "too_low": {
                    "text": "That is unfortunate for you.",
                    "speed": "slow"
                }
            },

            "purpose": {
                "text": "It's good to have a purpose in life.",
                "speed": "normal"
            },

            "invalid_integer": {
                "warning_1": {
                    "text": "I said numerals only.",
                    "speed": "normal"
                },
                "warning_2": {
                    "text": "Using the digits 1 through 9. If you can count that high.",
                    "speed": "slow"
                },
                "warning_3": {
                    "text": [
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "Pick at least one of the above numbers."
                    ],
                    "speed": "extremely_slow"
                }
            },

            "too_high_warning": {
                "warning_1": {
                    "text": "Try a more sensible number.",
                    "speed": "normal"
                },
                "warning_2": {
                    "text": "Feeling ambitious, aren't we?",
                    "speed": "normal"
                },
                "lower": {
                    "text": "LOWER",
                    "speed": "slow"
                },
                "ignored_lower": {
                    "text": "You're not even trying, are you?",
                    "speed": "fast"
                }
            }
        }
    },

    "endings": {
        "float": {},
        "string": [
        {
            "speed": "normal",
            "text": (
                "You are playing a character whose perception of reality relies on an integer.\n"
                'You supplied "{elephant_number}".\n'
                'Your tiny little 2-bit brain cannot parse "{elephant_number}" elephants.\n'
                "And yet they're standing right there."
            ),
            "pause": 2
        },
        {
            "speed": "normal",
            "text": "You stare at them for three days, trying to comprehend their quantity."
        },
        {
            "speed": "slow",
            "text": "You forget to eat.\nYou forget to sleep."
        },
        {
            "speed": "normal",
            "text": (
                "The elephants wander off.\n"
                "Perhaps you should have picked a better number."
            )
        }
    ],
        "zero_elephants": {}
    }
}

# controls speed of narration and adds a pause after each line. 
# use print_lines([speed], [line], pause) instead of print() for dialogue
def print_lines(lines, speed="normal", pause=0.3):
    for line in lines:
        type_text(line, speed, pause)



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