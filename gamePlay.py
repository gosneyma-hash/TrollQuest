from player import Player
from ferrenberg import ferrenberg_room
from intro import start_game
from gameTime import endgame, check_time
from Jaimison import jaimison_room


player = Player()


def chekhovsFlag() -> None:
    print("\n===================================================================\n")
    if (player.hasFlag()):
        print("You look down at the ground. You see dirt.")
        print("\n===================================================================\n")
        return

    print("You look down at the ground.")
    print("It's a Chekhov's [CENSORED BY MIAMI'S VALUES]!")
    print("Deciding you might need it, you take it.")
    print("[Item Obtained] You steal a Chekhov's [CENSORED BY MIAMI'S VALUES]!")
    player.setFlag(True)
    print("\n===================================================================\n")


def crawford() -> None:
    print("\n===================================================================\n")
    print("You approach the house. As you do, you see there's a hole in the ")
    print("wall next to the door. It looks like a key slot.")

    if (not player.hasFlag()):
        print("\nLooking around, you don't see anything that can open it.")
        print("Maybe there's something you could use from somewhere else...")
        print("\n===================================================================\n")
        return

    print("Realizing it's the same shape as the Chekhov's [CENSORED BY MIAMI'S ")
    print("VALUES], you insert it into the hole.")
    print("The door opens, and a troll that looks like President Crawford steps out.")
    input("\n[Press enter to continue] ")
    print('')

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
    print("President Crawford: You've done well. But here is your final riddle ")
    print("to put your understanding of Miami's Values to the test...")
    print("You only have 2 attempts.")

    incorrect = True
    max_attempts = 2
    curr_attempts = 0
    while (incorrect):
        print("\nPresident Crawford: In Miami University's Code of Student Conduct 2026-2027,")
        print("what object to tell the time is depicted on the cover?")
        print("Your answer (or type 'HELP' for assistance): ", end='')
        answer = input().lower()
        check_time()
        if (answer == 'sundial' or answer == 'sun dial'):
            incorrect = False
            print("\nPresident Crawford: Well done. You've successfully proven your knowledge of")
            print("Miami's Values!")
            print("President Crawford: For your hard work, here is your final item.")
            player.setExam(True)
            print("[Item Obtained] President Crawford hands you an exam!")
            print("You read the title at the top of it. 'BUS 302: Coloring")
            print("Between the Lines. Take Home Exam'.")
            print("President Crawford: Love and Honor.")
        elif (answer == 'help'):
            print("\nFor more guidance, view Miami University's Student Code of Conduct ")
            print("at the following link:")
            print("https://docs.google.com/document/d/e/2PACX-1vRMucz0S7mWTht0NnItC6y9Vx289nsgQWPpNh5dICrPtNttSJ8hVR-GpD_cQbCvh6q4fqQ4xiROfAWh/pub?urp=gmail_link")
        else:
            curr_attempts += 1
            print("\nPresident Crawford: WRONG! You do not understand Miami's Values!")
            if (curr_attempts == max_attempts):
                print("President Crawford: You have run out of time...")
                print("\n===================================================================\n")
                input("[Press enter to die]")
                print('')
                endgame()
                return
            else:
                print("President Crawford: I will give you only one other chance!")
    print("\n===================================================================")


def main():
    start_game(player)
    check_time()
    input("[Press enter to continue] ")
    print('')
    print("Glancing at your watch, you decide to better get moving.")
    print('')
    keepPlaying = True
    while (keepPlaying):
        print("Where to?")
        if (not player.hasPants() or not player.hasShoe()):
            print("[1] The Farmer School of Business")
            print("[2] A dark-looking alley")
            print("[3] The ground")
            answer = input("Choice: ")
            if (answer == "1"):
                ferrenberg_room(player)
            elif (answer == "2"):
                jaimison_room(player)
            elif (answer == "3"):
                chekhovsFlag()
            else:
                print("\nInvalid choice.")
        else:
            print("[1] The Farmer School of Business")
            print("[2] A dark-looking alley")
            print("[3] The ground")
            print("[4] A house")
            answer = input("Choice: ")
            if (answer == "1"):
                ferrenberg_room(player)
            elif (answer == "2"):
                jaimison_room(player)
            elif (answer == "3"):
                chekhovsFlag()
            elif (answer == "4"):
                crawford()
                if (player.hasExam()):
                    keepPlaying = False
            else:
                print("\nInvalid choice.")
        if (keepPlaying):
            input("[Press enter to continue] ")
            print('')
        else:
            input("[Press enter to exit game]")


if __name__ == "__main__":
    main()
