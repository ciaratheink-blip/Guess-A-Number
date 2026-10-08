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
    for chunk in chunks:
        text = chunk["text"].format(elephant_number=elephant_number)
        speed = chunk.get("speed", "normal")
        pause = chunk.get("pause", "normal")

        type_text(text, speed, data.TEXT_PAUSE.get(pause, 0.3))

print_lines(data.dialogue["endings"]["string"])

# Cursed choose a number game.
# Returns a number or string chosen by the player.
# 50 is the correct answer. 
def choose_num_of_elephants(number_of_elephants, elephant):
    input_is_int_count = 0
    input_is_bigger_100_count = 0
    elephant_type = "Normal"



    