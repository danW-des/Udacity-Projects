"""
v.3 > v.4 Patch Notes
- Made player input validation more strict, adjusting from:
    if '1' in response:
    to
    if response == 1:
- Included additional docstrings to improve code commenting
    and explanations.
"""
# Python modules
import time
import random
import sys


# Play again
def play_again():
    """
    Asks the player if they'd like to try the game again.
    Requests player input:
    '1' returns the user to the game beginning
    '2' exits the application.
    """
    while True:
        finish_response = input(
            "Would you like to try again?\n"
            "1. Try again.\n"
            "2. Exit program.\n")
        if finish_response == '1':
            print_pause(
                "Trying again...\n")
            sequence1()
        elif finish_response == '2':
            print_pause("Exiting game")
            time.sleep(2)
            sys.exit()
        else:
            print_pause(
                "Please enter '1' to try again "
                "or '2' to exit the game.")


# Player loss
def player_loss():
    """
    Prints loss string
    Calls play_again func
    """
    print_pause("Oh no! Something has gone horribly wrong. You lose!")
    play_again()


# Player win
def player_win():
    """
    Prints win string
    Calls play_again func
    """
    print_pause(
        "Excellent! You've successfully completed 'Spell Check'!\n"
        "Thank you for playing!")
    play_again()


# Random creature
def random_creature():
    """
    Returns a random creature from a list
    """
    creature_list = ["skeleton",
                     "ghoul",
                     "zombie"]
    creature = random.choice(creature_list)
    return creature


# Random room
def random_room():
    """
    Returns a random room description from a list
    """
    room_list = ["Old, wet stonework makes way to rotting wooden supports.",
                 "Dry, dusty racks of scrolls seem built into the structure.",
                 "Smooth, cool marble columns rise high above you."]
    room = random.choice(room_list)
    return room


# Random tome
def random_tome():
    """
    Returns a random tome description from a list
    """
    tome_list = ["Clean, intricate details decorate a well kept cover.",
                 "Mottled pages dangle loosely out from a broken binding.",
                 "On closer inspection, it appears to be more of a pamphlet."]
    tome = random.choice(tome_list)
    return tome


# Pause between print messages
def print_pause(string):
    print(string)
    time.sleep(2)


# Introduction to play session
def intro():
    """
    String presenting project credits and title
    Calls first sequence func
    """
    print_pause("Adventure Game Project\n"
                "Created by Dan Wilkins for\n"
                "Udacity Intro to Programming Fall 2019\n")
    print_pause("'Spell Check'\n")
    time.sleep(2)
    # Transition to first encounter
    sequence1()


# Sequence 1: Awaken in cell
def sequence1():
    """
    Sequence 1:
    A random room and creature are generated w/
    random_room and random_creature func
    The player awakes in a cell.
    Player input requests lead to varying paths:
    Event 1 inputs: 1>1 prt string, calls sequence 2 func
    Event 1 inputs: 1>2 prt string, calls player_loss func
    Event 1 inputs: 2 prt string,calls player_loss func
    """
    room = random_room()
    creature = random_creature()
    print_pause(f"You awake suddenly.\n"
                f"Looking around, you find yourself on the floor "
                f"of a small, windowless room.\n{room}")
    print_pause(f"One of the walls is made of iron bars and a gate. "
                f"Beyond the bars, a {creature} stands facing "
                f"away towards a hall.\n"
                f"The {creature} doesn't seem aware of your presence.\n")
    print_pause("Before you can do anything, you hear your mentor's "
                "disembodied voice echo through the room.")
    print_pause("'Sleeping during spell study has consequences!'\n"
                "'If tomes are too dull for you, we'll try this instead.'\n"
                "'Find a way out - or don't. Plenty of new mage apprentices "
                "waiting for a spot to open up!'\n"
                "Your mentor's last words fade away into the darkness "
                "of your new cell.\n")
    while True:
        response = input(f"You sigh. Not ANOTHER detention!\n"
                         f"The {creature} makes no indication it heard you "
                         f"or your mentor's stupid-loud spell voice.\n"
                         f"The {creature} is wearing a rather fashionable "
                         f"belt with a large key on it.\n"
                         f"1. Quietly magic the key off the {creature}'s "
                         "belt and unlock the door.\n"
                         "2. Go back to sleep, you could use the rest.\n")
        if response == '1':
            print_pause("You cast a quick cantrip and think of the key "
                        "floating into your open palm.\n"
                        "After a brief argument, the key agrees and "
                        f"lifts off the {creature}'s belt, "
                        "traveling quietly to your hand.")
            print_pause("You approach the gate, insert "
                        "the key, and turn.\n"
                        "CLICK!\n")
            while True:
                sequence1_response = input(f"The {creature} suddenly becomes "
                                           f"alert! It turns to the open door"
                                           f", trying to grab you!\n"
                                           f"1. Dodge the {creature}, push it "
                                           f"into the cell, and lock the "
                                           f"gate!\n"
                                           f"2. Give it a big hug!\n")
                if sequence1_response == '1':
                    print_pause(f"You feel pretty cool as you dodge "
                                f"the {creature}'s lumbering grapple and "
                                f"lock it in your cell.\n"
                                f"It seems the {creature} was more bothered "
                                f"by the open door than you escaping.\n"
                                f"It stands motionless, "
                                f"staring at the wall.\n")
                    # Event transition
                    sequence2()
                elif sequence1_response == '2':
                    print_pause(f"You give the {creature} a big hug!\n"
                                f"While it is personally thankful "
                                f"for the gesture, it has bills to pay and "
                                f"a promotion to consider.\n"
                                f"The {creature} tosses you back into "
                                f"the cell and locks the door.")
                    print_pause(f"A short time later, many {creature} "
                                f"approach you carrying an "
                                f"oversized cooking pot.")
                    print_pause(f"'You can't be serious...' you mutter.\n"
                                f"One of the {creature}s nods "
                                f"enthusiastically, producing a fork and "
                                f"knife from somewhere.\n")
                    # Event transition
                    player_loss()
                    time.sleep(2)
                else:
                    # Validate player input / force valid input
                    print_pause("Please enter '1' or '2' to select your "
                                "next action.\n")
        elif response == '2':
            print_pause(f"You yawn, stretch, and return to your nap.\n")
            time.sleep(2)
            print_pause(f"A commotion wakes you. You peer out of your cell "
                        f"to see many {creature} walking towards you, "
                        f"carrying an oversized cooking pot.")
            print_pause(f"'You can't be serious...' you mutter.\n"
                        f"One of the {creature}s nods enthusiastically, "
                        f"producing a fork and knife from somewhere.\n")
            # Event transition
            player_loss()
            time.sleep(2)
        else:
            # Validate player input / force valid input
            print_pause("Please enter '1' or '2' to select your "
                        "next action.\n")


# Sequence 2: Hallway
def sequence2():
    """
    Sequence 2:
    A random room is generated w/
    random_room func
    The player moves into a hallway.
    Player input requests lead to varying paths:
    Event 2 inputs: 1 prt string, returns user to input request
    Event 2 inputs: 2 prt string, calls sequence 3 func
    Event 2 inputs: 3 prt string, calls player_loss func
    """
    room = random_room()
    print_pause("You turn around to face the hallway.\n")
    print_pause(f"{room}\nIn the center of the hall, a lone "
                f"pedestal stands presenting a tome.\n"
                f"Beyond, at the far end of the hallway "
                f"is another door.\n")
    print_pause("You take a step forward - a bright flash erupts "
                "at the end of the hall!\n")
    while True:
        print_pause("A magical wall of fire appears, blocking your "
                    "way through the far door.")
        response = input("'Hmmmm...' you say out loud.'\n"
                         "1. Reason with the firewall.\n"
                         "2. Inspect the tome.\n"
                         "3. Walk through the fire and open the door.\n")
        if response == '1':
            print_pause("You may not be the smartest mage, but you "
                        "certainly are charming!\n"
                        "You attempt to get the firewall's attention "
                        "but it seems indifferent, or unable to "
                        "understand your dialect.\n"
                        "The firewall ignores you.\n")
        elif response == '2':
            print_pause("'Always with the books and scrolls...'\n")
            # Event transition
            sequence3()
            time.sleep(2)
        elif response == '3':
            print_pause("'The Mentors certainly wouldn't let us come "
                        "to harm,' you say aloud.\n")
            print_pause("Testing its heat, you believe this spell to "
                        "be a simple illusion.")
            print_pause("You confidentaly walk into the firewall, "
                        "reaching towards the do-\n")
            print("AH! AAAAAAAHHHHHH!\n")
            print_pause("The fires are rather very hot, and immediately "
                        "turn you to ash.\n")
            player_loss()
        else:
            # Validate player input / force valid input
            print_pause("Please enter '1','2', or '3' to select "
                        "your next action.\n")


# Sequence 3: Tome Check
def sequence3():
    """
    Sequence 3:
    A random tome is generated w/
    random_tome func
    The player interacts with the tome.
    Player input requests lead to varying paths:
    Event 3 inputs: 1 prt string, calls sequence 4 func
    Event 3 inputs: 2>1 prt string, calls sequence 4 func
    Event 3 inputs: 2>2 prt string, calls player_loss func
    """
    tome = random_tome()
    print_pause(f"You approach the tome.\n")
    print_pause(f"{tome}")
    while True:
        response = input("This looks like the spell we were learning in class "
                         "before I fell asleep.\n"
                         "1. Open the tome.\n"
                         "2. Toss the tome into the firewall "
                         "- no more books!\n")
        if response == '1':
            print_pause("You turn to a random page, and sure enough "
                        "the spell 'Howling Gale' and its casting "
                        "are described just like from class.")
            print_pause("Despite your best efforts, you end up "
                        "learning something today.")
            print_pause("You set the tome back onto the pedestal.\n")
            # Event transition
            sequence4()
        elif response == '2':
            print_pause("You pick up the tome and prepare to toss it into "
                        "the firewall.")
            print_pause("'Wait wait wait wait wait!' sputters the tome.\n"
                        "'That's pretty messed up, you're gonna\n"
                        "throw me in the fire, just like that?'\n")
            while True:
                sequence3_response = input("'Oh...' you say.\n"
                                           "Some of these old tomes are "
                                           "rather dramatic.\n"
                                           "1. Learn from the tome.\n"
                                           "2. 'Into the firewall with ya'.\n")
                if sequence3_response == '1':
                    print_pause("You turn to a random page, and sure enough "
                                "the spell 'Howling Gale' and its casting "
                                "are described just like from class.")
                    print_pause("Despite your best efforts, you end up "
                                "learning something today.")
                    print_pause("You set the tome back onto the pedestal.")
                    # Event transition
                    sequence4()
                elif sequence3_response == '2':
                    print_pause("You toss the tome into the firewall.")
                    print_pause("'Gaaaaah!' 'aaaaaahhhh!' cries the tome.")
                    print_pause("'AAAAAAHHHHH!'")
                    print_pause("'Aaahh!' 'Aah!'")
                    print_pause("'...'")
                    print_pause("The tome seems at rest.")
                    print_pause("Suddenly, a spectral visage with a striking "
                                "resemblence to the tome you just murdered "
                                "flies from the firewall.")
                    print_pause("'Fool!' barks the tome.\n"
                                "'You have released me from my prison!'\n"
                                "'The Dark Library shall rise again!'\n")
                    print_pause("The ghostly novella casts 'Howling Gale',\n"
                                "launching you into the firewall.")
                    print_pause("You turn to ash, just like the book "
                                "you murdered.. that... murdered you.\n")
                    player_loss()
                else:
                    # Validate player input / force valid input
                    print_pause("Please enter '1' or '2' to select your next "
                                "action.")
            # Event transition
            player_loss()
            time.sleep(2)
        else:
            # Validate player input / force valid input
            print_pause("Please enter '1' or '2' to select your next action.")


# Sequence 4: Remove the Firewall
def sequence4():
    """
    Sequence 4:
    The player casts a spell on the firewall to escape.
    Player input requests lead to varying paths:
    Event 4 inputs: 1 prt string, calls player_win func
    Event 4 inputs: 2 prt string, calls player_loss func
    """
    print_pause("'Only one thing to do now.'\n")
    print_pause("You approach the firewall.")
    while True:
        response = input("'Trap me in a weird, purpose driven "
                         "dungeon to make me learn, huh?'\n"
                         "1. Cast 'Howling Gale' on the firewall.\n"
                         "2. Cast 'Gowling Hale' to spite your mentor.\n")
        if response == '1':
            print_pause("The firewall is suffocated as an immense burst "
                        "of air buffets from your hands.\n")
            print_pause("The hallway door beyond splinters and flys off "
                        "its hinges, revealing your mentor's study.\n"
                        "Your mentor looks up from their desk and sighs.\n")
            print_pause("'Same time tomorrow?' you ask with a grin.\n")
            # Event transition
            player_win()
        elif response == '2':
            print_pause("Miscasting spells always create bizarre behaviors.\n")
            print_pause("This time, instead of air, blasts of negative "
                        "energy\n"
                        "bend out of your palm, destroying the magical "
                        "fabric\n"
                        "of time and space that created this dungeon.\n")
            print_pause("A piece of wall detonates under the energy, "
                        "exposing empty void - absolute nothingness.")
            print_pause("'Uh o-'")
            print_pause("You, the firewall, the tome. Everything is sucked "
                        "into "
                        "the eternal nothingness, ceasing to ever have been.")
            # Event transition
            player_loss()
            time.sleep(2)
        else:
            # Validate player input / force valid input
            print_pause("Please enter '1' or '2' to select your next action.")


# Call Adventure Game
intro()
