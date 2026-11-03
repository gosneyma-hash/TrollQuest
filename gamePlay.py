from player import Player
from ferrenberg import ferrenberg_room
from intro import start_game

player = Player()


def chekhovsFlag() -> None:
    if (player.hasFlag()):
        print("You look around. There's nothing new in here.")
        print("\n===================================================================\n")
        return
    print("As you look around, you see a tile in the ground that's sticking out. Odd...")

    if (not player.hasPants()):
        print("You see everyone staring at you and decide to leave.")
        print("You need to focus on finding your pants.")
        print("\n===================================================================\n")
        return

    print("You touch the tile. It moves, revealing a dent in the ground.")
    print("It's a Chekhov's [CENSORED BY MIAMI'S VALUES]!")
    print("More specifically, a flag [CENSORED BY MIAMI'S VALUES]!")
    print("Deciding you might need it, you take it with you and leave.")
    print("[Item Obtained] You steal a Chekhov's [CENSORED BY MIAMI'S VALUES]!")
    player.setFlag(True)
    print("\n===================================================================\n")


def crawford() -> None:
    print("You approach the house. As you do, you see there's a hole in the ")
    print("wall next to the door. It looks like a key slot.")

    if (not player.hasFlag()):
        print("\nLooking around, you don't see anything that can open it.")
        print("Maybe there's something you could use from somewhere else...")
        print("\n===================================================================\n")
        return

    print("Realizing it's the same shape as the Chekhov's [CENSORED BY MIAMI'S ")
    print("VALUES], you insert it into the hole.")
    print("The door opens, and a troll that looks a lot like President Crawford ")
    print("steps out. At this point, you aren't surprised.")

    if (not (player.hasPants() and player.hasShoe())):
        print("\nThe troll stares at you in horror.")
        print("President Crawford: Where are your clothes from yesterday?! This does not ")
        print("align with Miami's Values!")
        print("He slams the door in your face.")
        print("You look down and remember you still don't have all your clothes on.")
        print("Maybe you can find them somewhere else...")
        print("\n===================================================================\n")
        return

    print("President Crawford: I see you've upheld Miami's dress code. Come in.")
    print('You follow him inside, anxious to get whatever your last item is.')
    print('Your pants, your shoe... what else is left?')
    print("President Crawford: You've done well. But here is your final riddle ")
    print("to put your understanding of Miami's Values to the test...")

    incorrect = True
    max_attempts = 2
    curr_attempts = 0
    while (incorrect):
        if (curr_attempts > 0):
            print("You only have %d attempts left!" % (3 - curr_attempts))
        else:
            print("You have 3 attempts.")
        print("\nPresident Crawford: In Miami University's Code of Student Conduct 2026-2027,")
        print("what object to tell the time is depicted on the cover?")
        print("Your answer (or type 'HELP' for guidance): ", end='')
        answer = input().lower()
        if (answer == 'sundial' or answer == 'sun dial'):
            incorrect = False
            print("\nPresident Crawford: Well done. You've successfully proven your knowledge of")
            print("Miami's Values!")
            print("President Crawford: For your hard work, here is your final item.")
            player.setExam(True)
            print("[Item Obtained] President Crawford hands you an exam!")
            print("You read the title at the top of it. 'BUS 302: Coloring")
            print("Between the Lines. Take Home Exam'.")
        elif (answer == 'help'):
            print("\nYou gasp. The help option isn't useless!")
            help()
            print("")
        else:
            print("\nPresident Crawford: WRONG! You do not understand Miami's Values!")
            if (curr_attempts == max_attempts):
                print("President Crawford: You have run out of time...")
                # hatMan()
                return
            else:
                print("President Crawford: I will give you another chance. Use it wisely.")
                curr_attempts += 1
    print("\n===================================================================\n")


def help() -> None:
    print("For more guidance, view Miami University's Student Code of Conduct ")
    print("at the following link:")
    print("https://docs.google.com/document/d/e/2PACX-1vRMucz0S7mWTht0NnItC6y9Vx289nsgQWPpNh5dICrPtNttSJ8hVR-GpD_cQbCvh6q4fqQ4xiROfAWh/pub?urp=gmail_link")


def main():
    start_game(Player)
    ferrenberg_room(Player)


if __name__ == "__main__":
    main()
