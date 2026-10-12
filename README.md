# Deathlogic: Guess the Number

**I'd recommend playing with the following instructions:** 

>Follow the prompts on screen. Failure is how we learn.

> For more comprehensive instructions scroll down.

## How to play

1. Make sure you have **Python 3** installed.
2. Download or clone the repository and keep `Guess_a_number.py` and `data_dictionaries.py` in the **same folder**.
3. Open a terminal in that folder and run:

   ```bash
   python Guess_a_number.py
   ```

   On some systems you may need `python3 Guess_a_number.py` instead.
4. Read the on screen prompts and enter your answers. Type **Q** at an input prompt to quit.


## Project files

- **`Guess_a_number.py`** contains the game logic, choices, state, progression, and endings.
- **`data_dictionaries.py`** contains the dialogue, text speeds, and pause settings. It is imported by the main script.
- **`deathlogic_stitched_flowchart.png`** is the flowchart showing the game's branches and outcomes. It had to be stitched together from screenshots. Can be viewed in full [here](https://miro.com/app/board/uXjVEdy3zI4=/?share_link_id=37161252913)

**Repository:** [Deathlogic on GitHub](https://github.com/ciaratheink-blip/Guess-A-Number.git)

---

```text

  ##############################################################
  #                                                            #
  #   SSSSS   PPPPP    OOOOO   IIIII  L       EEEEE  RRRRR     #
  #   S       P    P  O     O    I    L       E      R    R    #
  #   SSSSS   PPPPP   O     O    I    L       EEEE   RRRRR     #
  #       S   P       O     O    I    L       E      R   R     #
  #   SSSSS   P        OOOOO   IIIII  LLLLL   EEEEE  R    R    #
  #                                                            #
  #                      W A R N I N G                         #
  #                                                            #
  #        THE SECTIONS BELOW EXPLAIN GAME MECHANICS,          #
  #             HIDDEN CONDITIONS AND WINNING ROUTES.         #
  #                                                            #
  #              STOP HERE IF YOU WANT TO EXPLORE.            #
  #                                                            #
  ##############################################################

```
```text

  ##############################################################
  #                                                            #
  #   SSSSS   PPPPP    OOOOO   IIIII  L       EEEEE  RRRRR     #
  #   S       P    P  O     O    I    L       E      R    R    #
  #   SSSSS   PPPPP   O     O    I    L       EEEE   RRRRR     #
  #       S   P       O     O    I    L       E      R   R     #
  #   SSSSS   P        OOOOO   IIIII  LLLLL   EEEEE  R    R    #
  #                                                            #
  #                      W A R N I N G                         #
  #                                                            #
  #        THE SECTIONS BELOW EXPLAIN GAME MECHANICS,          #
  #             HIDDEN CONDITIONS AND WINNING ROUTES.         #
  #                                                            #
  #              STOP HERE IF YOU WANT TO EXPLORE.            #
  #                                                            #
  ##############################################################

```

## Detailed instructions (spoilers)
A text based, branching Python adventure about choosing a number of elephants and attempting to transport them to their destination. Your decisions affect their survival, your relationship with the local dwarves, and, quite possibly, your future career prospects.
### The basic objective

Your job is to deliver a herd of elephants. The game starts by asking you to choose how many elephants you have, then presents a series of A/B/C choices about feeding them, dealing with dwarves, and crossing a bridge.

Inputs have consequences. Incorrect answers may produce warnings, endings, or different routes, and the game restarts after a failed run. The goal is to find a path that delivers your elephants successfully.

### Choosing elephants

- **50 elephants** is the optimal number. Entering 50 as your first valid guess, without earlier warnings, gives you **shiny elephants**.
- **Fewer than 50** can continue, but may struggle against the dwarves.
- **More than 50** triggers warnings and hints. A herd of more than 50 cannot safely cross the bridge.
- **Zero elephants** and repeated invalid numerical input lead to their own endings.

### Food, hunger and bloodlust

Choose between **trees**, **mushrooms**, and **dwarves** as elephant food. Each changes the herd's hunger and possibly its bloodlust. Hunger changes as you travel, and choosing dwarves can make your herd act violently during an otherwise peaceful negotiation.

### The dwarves and learning Dwarven

The dwarves are protecting a breeding ground for endangered dire wolves. They speak Dwarven, and the amount you understand depends on your language proficiency:

`none` → `basic` → `intermediate` → `conversational`

At lower proficiency levels, negotiations go badly because you misunderstand their warning. At **conversational** proficiency, you can reach a peaceful agreement, provided your elephants aren't intent on eating the dwarves.

A successful attack on the dwarves lets you take a **Dwarven-to-English phrasebook**. Reading it later improves your Dwarven by one level, but you lose track of the elephants while studying. **Dwarven proficiency persists between runs**; other run-specific stats reset after death. Repeated failures are therefore part of the route to success.

### The bridge

At the bridge you can try to cross, look for another route, or rest/read the phrasebook, depending on what you're carrying.

- If you bring **more than 50 elephants**, the bridge collapses.
- If you attacked the dwarves and have their **phrasebook**, a surviving dwarf sabotages the bridge when you try to cross. His insults are only as intelligible as your current Dwarven proficiency; you don't have time to consult the book.
- Looking for another way around or leaving the herd unattended has its own consequences.
- If you have **50 or fewer elephants** and reached the bridge without massacring the dwarves, you can cross and complete your delivery.

### One route to victory

1. Start with **50 elephants**.
2. Choose **trees** for food.
3. At the dwarves, choose **diplomacy**. You will need **conversational Dwarven** for this to succeed.
4. Follow their alternative route to the bridge.
5. Choose **A: Cross the bridge**.

To obtain conversational Dwarven from a fresh game, you'll need to experiment with the attack and phrasebook routes over multiple runs. Winning is deliberately not possible through diplomacy on your very first run.

### Endings and statistics

There are multiple endings, including failed diplomacy, disastrous battles, impossible elephant quantities, alternative life choices, and successful delivery. On the winning route, the game displays final statistics, including the number and type of elephants delivered, diet, Dwarven proficiency and reputation, and the accumulated death count.

## Known limitation

The current number validator uses Python's `float()` conversion. Extremely precise decimals can be rounded to whole numbers, and extremely small numerical inputs can become zero. This can cause unexpected behaviour for unusual inputs, although ordinary gameplay works as intended. A possible future improvement is to validate the original input string without first converting it to a floating-point number.

## Development notes

Deathlogic was built in Python as a branching text adventure, using separate dialogue dictionaries, reusable input validation, conditional dialogue, and a persistent game state. The flowchart documents its branches and outcomes.
