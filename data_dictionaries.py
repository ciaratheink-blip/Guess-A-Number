# Dialog character speed dictionry 
# How many seconds between characters.
TEXT_SPEED = {
    "extremely_slow": 0.1, 
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
            "speed": "slow"
        },
        {
            "text": "Make sure you look after them.",
            "speed": "extremely_slow",
        
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
            
            }
        ],

        "dwarves": [
            {
                "text": "\nThere are no Dwarves here.",
                "speed": "slow",
                "pause": "long"
            },
            {
                "text": "Your elephants are hungry.",
                "speed": "slow",
                "pause" : "long"
            },
            {
                "text": "Your elephants will remember your promises.",
                "speed": "extremely_slow",
                
            }
        ]
    }
},

"travel_to_dwarves": {

    "before_status": [
        {
            "text": "You continue along the river for some distance.",
            "speed": "normal"
        },
        {
            "text": "Your elephants start to get hungry.",
            "speed": "slow"
        }
    ],

    "after_status": [
        {
            "text": "I hope you can keep them fed.",
            "speed": "slow",
            "pause": "concerning"
        }
    ]
},


        
"dwarf_encounter": {

    # INTRO
    

    "intro": [
        {
            "text": "\nYou keep following the river.",
            "speed": "normal"
        },
        {
            "text": "You follow the river through a cave.",
            "speed": "normal"
        },
        {
            "text": "When you emerge, a wide valley stretches out below you.",
            "speed": "normal"
        },
        {
            "text": "At its entrance, a small army of dwarves blocks your path.",
            "speed": "normal"
        },
        {
            "text": "They are heavily armed.",
            "speed": "normal"
        }
    ],

    "below_50": {
        "text": "They look like they could take on {elephant_number} elephants.",
        "speed": "slow",
        "pause": "long"
    },

    "dwarf_diet": {
        "text": "Your elephants have noticed the dwarves.",
        "speed": "extremely_slow"
    },

    "choices": [
        {
            "text": "What would you like to do?",
            "speed": "normal"
        },
        {
            "text": "A: Attack!\nB: Diplomacy!\nC: Run!",
            "speed": "normal"
        }
    ],

   #ATTACK

    "attack": {

        "successful_before_status": [
            {
                "text": "\nYou order your elephants to attack.",
                "speed": "normal"
            },
            {
                "text": "The dwarves raise their weapons.",
                "speed": "normal"
            },
            {
                "text": "Your elephants charge.",
                "speed": "normal"
            },
            {
                "text": "The dwarves are exceptionally well trained.",
                "speed": "normal",
                "pause": "long"
            },
            {
                "text": "They form ranks, brace their shields and prepare to defend the valley.",
                "speed": "normal"
            },
            {
                "text": "Unfortunately, none of their training covered this particular situation.",
                "speed": "normal"
            },
            {
                "text": "The battle is brief.",
                "speed": "normal"
            },
            {
                "text": "The meal takes considerably longer.",
                "speed": "slow",
                "pause": "long"
            },
            {
                "text": "You survey the aftermath.",
                "speed": "normal"
            },
            {
                "text": "Your elephants seem pleased with themselves.",
                "speed": "normal"
            }
        ],

        "successful_after_status": [
            {
                "text": "\nYou find a Dwarven to English phrasebook among the abandoned supplies.",
                "speed": "normal"
            },
            {
                "text": "You leaf through it.",
                "speed": "normal"
            },
            {
                "text": "The Dwarven word for 'elephant' is followed by several pages of increasingly specific warnings.",
                "speed": "normal"
            },
            {
                "text": "You put it in your bag.",
                "speed": "normal"
            },
            {
                "text": "Your elephants are no longer hungry.",
                "speed": "normal"
            },
            {
                "text": "For now.",
                "speed": "slow",
                "pause": "concerning"
            }
        ]
    },



    "diplomacy": {

        "warning_intro": {
            "text": "\nA dwarf steps forward and begins shouting.",
            "speed": "normal"
        },

        # Same speech, progressively translated.


        "dwarven_warning": {

            "none": {
                "text": "\nFgbc! Guvf vf n cebgrpgrq nern. Qver jbyirf oerrq urer. Gurl jrer arneyl jvcrq bhg va gur jne. Lbh pnaabg oevat ryrcunagf guebhtu.",
                "speed": "fast"
            },

            "basic": {
                "text": "\nFgbc! Guvf vf n cebgrpgrq nern. Dire wolves oerrq urer. Gurl jrer arneyl jvcrq bhg va gur war. Lbh pnaabg oevat elephants guebhtu.",
                "speed": "fast"
            },

            "intermediate": {
                "text": "\nStop! Guvf vf n protected area. Dire wolves oerrq urer. Gurl jrer nearly wiped out va gur war. You cannot bring elephants guebhtu.",
                "speed": "fast"
            },

            "conversational": {
                "text": "\nStop! This is a protected area. Dire wolves breed here. They were nearly wiped out in the war. You cannot bring elephants through.",
                "speed": "normal"
            }
        },

        "conversational": {

            "normal": [
                {
                    "text": "\nYou warn the dwarves not to spook the elephants.",
                    "speed": "normal"
                },
                {
                    "text": "The dwarves lower their weapons.",
                    "speed": "normal"
                },
                {
                    "text": "They seem relieved to find someone they can actually communicate with.",
                    "speed": "normal"
                }
            ],

            "shiny": [
                {
                    "text": "\nThe dwarves are stunned by your shiny elephants.",
                    "speed": "normal"
                },
                {
                    "text": "They have never seen anything quite like them.",
                    "speed": "normal"
                },
                {
                    "text": "Several lower their weapons.",
                    "speed": "normal"
                },
                {
                    "text": "One of them cautiously approaches to get a better look.",
                    "speed": "normal"
                },
                {
                    "text": "You explain that you're trying to reach your destination.",
                    "speed": "normal"
                },
                {
                    "text": "The dwarves seem considerably more willing to talk.",
                    "speed": "normal"
                }
            ]
        },

        "shared_success": [
            {
                "text": "\nThe dwarves explain that the valley is a protected conservation area.",
                "speed": "normal"
            },
            {
                "text": "The local dire wolf population was nearly wiped out during the war.",
                "speed": "normal"
            },
            {
                "text": "This is one of their last remaining breeding grounds.",
                "speed": "normal"
            },
            {
                "text": "Unfortunately, a herd of elephants wandering through would rather undermine the conservation effort.",
                "speed": "normal"
            },
            {
                "text": "You explain that you're only trying to reach your destination.",
                "speed": "normal"
            },
            {
                "text": "The dwarves understand, but they cannot allow you to pass through the valley.",
                "speed": "normal"
            },
            {
                "text": "Instead, they offer you supplies and directions to an alternative route.",
                "speed": "normal"
            },
            {
                "text": "How reasonable.",
                "speed": "slow",
                "pause": "long"
            }
        ],

        "bloodlust_override": [
            {
                "text": "\nYou thank the dwarves for their assistance.",
                "speed": "normal"
            },
            {
                "text": "It appears you've reached a peaceful resolution.",
                "speed": "normal"
            },
            {
                "text": "Unfortunately, your elephants have been paying absolutely no attention to the negotiations.",
                "speed": "normal"
            },
            {
                "text": "They've been looking at the dwarves.",
                "speed": "normal"
            },
            {
                "text": "Quite intently.",
                "speed": "slow",
                "pause": "long"
            },
            {
                "text": "You suddenly remember what you promised them.",
                "speed": "normal"
            },
            {
                "text": "The elephants charge.",
                "speed": "fast"
            }
        ]
    },


    # TRANSITION TO NEXT LEVEL


    "next_level": {

        "diplomacy": [
            {
                "text": "\nFollowing the dwarves' directions, you take the alternative route around the conservation area.",
                "speed": "normal"
            }
        ],

        "attack": [
            {
                "text": "With nobody left to object, you proceed through the valley.",
                "speed": "normal"
            }
        ]
    }
},

        "bridge": {},
        "final_level": {}
    },

    "multiple_choice_warnings": {
    "warning_1": {
        "text": "\nI said A, B or C.",
        "speed": "slow"
    },
    "warning_2": {
        "text": "\nA\nB\nOR\nC",
        "speed": "extremely_slow"
    },
    "warning_3": {
        "text": "\nIf you don't enter A B or C, I'm ending this.",
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
    }],

        "no_letters": [
    {
        "speed": "normal",
        "text": "no_letters ending PLACE HOLDER",
    }],
    
"attack_no_bloodlust": [
    {
        "text": "You urge your elephants to attack.",
        "speed": "normal"
    },
    {
        "text": "They look confused.",
        "speed": "normal",
        "pause": "long"
    },
    {
        "text": "These are not battle elephants.",
        "speed": "normal"
    },
    {
        "text": "They're pretty much only interested in eating {elephant_diet}.",
        "speed": "normal"
    },
    {
        "text": "You slap Nellie on the rump to get the herd moving.",
        "speed": "normal"
    },
    {
        "text": "It works.",
        "speed": "normal",
        "pause": "long"
    },
    {
        "text": "You think.",
        "speed": "normal",
        "pause": "long"
    },
    {
        "text": "Unfortunately, she knocks you over in the process.",
        "speed": "normal"
    },
    {
        "text": "The last thing you see is your herd charging towards the dwarves.",
        "speed": "normal"
    },
    {
        "text": "You get trampled.",
        "speed": "slow"
    }
],

"attack_failed": [
    {
        "text": "You order your elephants to attack.",
        "speed": "normal"
    },
    {
        "text": "They charge towards the dwarves.",
        "speed": "normal"
    },
    {
        "text": "The dwarves form ranks and brace themselves.",
        "speed": "normal"
    },
    {
        "text": "Your elephants are enthusiastic.",
        "speed": "normal"
    },
    {
        "text": "There just aren't very many of them.",
        "speed": "normal"
    },
    {
        "text": "The dwarves fight back.",
        "speed": "normal"
    },
    {
        "text": "For a brief moment you consider retreating.",
        "speed": "normal"
    },
    {
        "text": "Unfortunately, you're standing between two armies, neither of which is particularly concerned about your survival.",
        "speed": "normal"
    },
    {
        "text": "You are killed in the crossfire.",
        "speed": "normal"
    },
    {
        "text": "Your elephants lose the battle.",
        "speed": "normal"
    },
    {
        "text": "I hope that was worth it.",
        "speed": "slow",
        "pause": "long"
    }
],

"diplomacy_none": [
    {
        "text": "You don't understand a word.",
        "speed": "normal"
    },
    {
        "text": "The dwarf continues shouting.",
        "speed": "normal"
    },
    {
        "text": "He appears increasingly agitated.",
        "speed": "normal"
    },
    {
        "text": "You attempt to reassure him.",
        "speed": "normal"
    },
    {
        "text": "This does not appear to help.",
        "speed": "normal"
    },
    {
        "text": "He approaches your elephants, waving his arms.",
        "speed": "normal"
    },
    {
        "text": "Your elephants panic.",
        "speed": "normal"
    },
    {
        "text": "You get trampled.",
        "speed": "slow"
    }
],

"diplomacy_basic": [
    {
        "text": "You consider the information available to you.",
        "speed": "normal"
    },
    {
        "text": "Apparently, the dwarves are threatening to go to war with your elephants.",
        "speed": "normal"
    },
    {
        "text": "You attempt to explain that you have no interest in fighting their wolves.",
        "speed": "normal"
    },
    {
        "text": "The dwarf looks confused.",
        "speed": "normal"
    },
    {
        "text": "He starts shouting again.",
        "speed": "normal"
    },
    {
        "text": "You appear to have made the situation worse.",
        "speed": "normal"
    },
    {
        "text": "He approaches your elephants, waving his arms.",
        "speed": "normal"
    },
    {
        "text": "Your elephants panic.",
        "speed": "normal"
    },
    {
        "text": "You get trampled.",
        "speed": "slow"
    }
],

"diplomacy_intermediate": [
    {
        "text": "You consider the information available to you.",
        "speed": "normal"
    },
    {
        "text": "The dwarves are clearly protecting the valley against your elephants.",
        "speed": "normal"
    },
    {
        "text": "And apparently there's been a war.",
        "speed": "normal"
    },
    {
        "text": "You assure them that your elephants have no intention of getting involved in their conflict.",
        "speed": "normal"
    },
    {
        "text": "The dwarf looks bewildered.",
        "speed": "normal"
    },
    {
        "text": "He begins shouting something about breeding.",
        "speed": "normal"
    },
    {
        "text": "You wonder if you've misunderstood.",
        "speed": "normal"
    },
    {
        "text": "Before you can ask for clarification, another dwarf rushes forward.",
        "speed": "normal"
    },
    {
        "text": "Your elephants spook.",
        "speed": "normal"
    },
    {
        "text": "You get trampled.",
        "speed": "normal"
    },
    {
        "text": "You were getting quite good at Dwarven, too.",
        "speed": "slow",
        "pause": "long"
    }
],

"dwarf_run": [
    {
        "text": "\nYou assess the situation.",
        "speed": "normal"
    },
    {
        "text": "The dwarves are heavily armed.",
        "speed": "normal"
    },
    {
        "text": "Your elephants are unpredictable.",
        "speed": "normal"
    },
    {
        "text": "You decide that discretion is the better part of valour.",
        "speed": "normal"
    },
    {
        "text": "You run.",
        "speed": "normal"
    },
    {
        "text": "Your elephants run too.",
        "speed": "normal"
    },
    {
        "text": "They're considerably faster than you.",
        "speed": "normal"
    },
    {
        "text": "Within minutes, the herd has disappeared into the distance.",
        "speed": "normal"
    },
    {
        "text": "You attempt to follow their tracks.",
        "speed": "normal"
    },
    {
        "text": "There are quite a lot of tracks.",
        "speed": "slow",
        "pause": "long"
    },
    {
        "text": "You become lost.",
        "speed": "normal"
    },
    {
        "text": "After several days without food, you begin to regret your decision.",
        "speed": "normal"
    },
    {
        "text": "You starve.",
        "speed": "normal"
    },
    {
        "text": "The elephants are probably fine.",
        "speed": "slow",
        "pause": "concerning"
    }
],

    },
    

    "current_run_stats": {
        "heading": "CURRENT RUN STATS",
        "deaths_total": "Total deaths",
        "dwarven_level": "Dwarven level",
        "elephant_number": "Elephants remaining"
    }
}
