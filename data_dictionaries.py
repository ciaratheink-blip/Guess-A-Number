# Dialog character speed dictionry 
# How many seconds between characters.
TEXT_SPEED = {
    "extremely_slow": 0.2, 
    "slow": 0.08,
    "normal": 0.04,
    "fast": 0.01
}

# Dialog pause speed dictionry 
# How many seconds between chunks.
TEXT_PAUSE = {
    "normal": 0.3,
    "long": 1.5,
    "concerning": 4.0
}

# Dialogue dictionary
# Lists are used for dialogue played in sequence.
# Dictionaries are used for dialogue selected by name or condition.

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
            "intro": [
                {"text": "Guess the number?", "speed": "normal"},
                {
                    "text": "Enter whole positive numerals only or face the consequences.",
                    "speed": "slow"
                }
            ],
            "number_statement": {
                "normal": {
                    "text": "\nYou have {elephant_number} elephants.",
                    "speed": "normal"
                },
                "shiny": {
                    "text": "\nYou have {elephant_number} {elephant_type} elephants.",
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
                },
                "invalid": {
                    "text": "I guess.",
                    "speed": "slow",
                    "pause" : "concerning"
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
                    "text": "1\n2\n3\n4\n5\n6\n7\n8\n9\nPick at least one of the above numbers.",
                    "speed": "extremely_slow"
                },
                "accept_invalid": {
                    "text": "Fine.",
                    "speed": "fast",
                    "pause": "concerning"
                }
                
                
            },
            "too_high_warning": {
                "warning_1": {
                    "text": "\nTry a more sensible number.",
                    "speed": "normal"
                },
                "warning_2": {
                    "text": "\nFeeling ambitious, aren't we?",
                    "speed": "normal"
                },
                "lower": {
                    "text": "\nLOWER",
                    "speed": "slow"
                },
                "ignored_lower": {
                    "text": "\nYou're not even trying, are you?",
                    "speed": "fast"
                }
            }
        },
        
"choose_elephant_diet": {

    "intro": [
        {
            "text": "\nYou are transporting a herd of elephants along a river to your destination.",
            "speed": "normal"
        },
        {
            "text": "Your elephants are hungry.",
            "speed": "normal"
        },
        {
            "text": "When this is empty your elephants will starve.",
            "speed": "normal"
        },
        {
            "text": "Make sure you look after them.",
            "speed": "extremely_slow",
            "pause": "long"
        }
    ],

    "choices": [
        {
            "text": "\nWhat do elephants eat?",
            "speed": "normal"
        },
        {
            "text": "A: Trees\nB: Mushrooms\nC: Dwarves",
            "speed": "normal"
        }
    ],

    "outcomes": {

        "trees": [
            {
                "text": "\nYou find a clearing of trees.",
                "speed": "normal"
            },
            {
                "text": "Your elephants strip them bare.",
                "speed": "normal"
            },
            {
                "text": "Everything is fine.",
                "speed": "normal"
            },
            {
                "text": "Isn't nature wonderful?",
                "speed": "normal"
            }
        ],

        "mushrooms": [
            {
                "text": "\nI don't know how you thought you could find enough mushrooms to feed {elephant_number} elephants but you give it your best shot.",
                "speed": "normal"
            },
            {
                "text": "You manage to find some you think are edible.",
                "speed": "normal"
            },
            {
                "text": "It doesn't go very far.",
                "speed": "slow",
                "pause": "long"
            },
            {
                "text": "I hope you can find more.",
                "speed": "extremely_slow",
                "pause": "concerning"
            }
        ],

        "dwarves": [
            {
                "text": "\n There are no Dwarves here.",
                "speed": "slow",
                "pause": "long"
            },
            {
                "text": "Your elephants are hungry.",
                "speed": "normal"
            },
            {
                "text": "Your elephants will remember your promises.",
                "speed": "extremely_slow",
                "pause": "concerning"
            }
        ]
    }
},

        "dwarf_encounter": {},
        "bridge": {},
        "final_level": {}
    },

    "multiple_choice_warnings": {
    "warning_1": {
        "text": "I said A, B or C.",
        "speed": "slow"
    },
    "warning_2": {
        "text": "A\nB\nOR\nC",
        "speed": "extremely_slow"
    },
    "warning_3": {
        "text": "If you don't enter A B or C, I'm ending this.",
        "speed": "fast"
    }
},

    "endings": {
        "float": [   
    {
        "speed": "normal",
        "text": "float elephant ending PLACE HOLDER",
    }],
        "string": [
    {
        "speed": "normal",
        "text": (
            "\nYou are playing a character whose perception of reality relies on an integer.\n"
            'You supplied "{elephant_number}".\n'
            'Your tiny little 2-bit brain cannot parse "{elephant_number}" elephants.\n'
            "And yet they're standing right there."
        ),
        "pause": "long"
    },
    {
        "speed": "extremely_slow",
        "text": "You stare at them for three days.",
        "pause": "concerning"
    },
    {
        "speed": "slow",
        "text": "You forget to eat.",
        "pause": "long"
    },
    {
        "speed": "slow",
        "text": "You forget to sleep.",
        "pause": "long"
    },
    {
        "speed": "slow",
        "text": "You can't comprehend their quantity.",
        "pause": "long"
    },
    {
        "speed": "slow",
        "text": (
            "The elephants wander off.\n"
            "Perhaps you should have picked a better number."
        ),
        "pause": "normal"
    }
],
        "zero_elephants": [
    {
        "speed": "normal",
        "text": "zero elephant ending PLACE HOLDER",
    }]
    },

    "current_run_stats": {
        "heading": "CURRENT RUN STATS",
        "deaths_total": "Total deaths",
        "dwarven_level": "Dwarven level",
        "elephant_number": "Elephants remaining"
    }
}
