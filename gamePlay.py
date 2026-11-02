from player import Player

player = Player()


def start_game() -> None:
    print("===================================================================")
    print("            THE EPIC TROLLVENTURE - VOLUME 1                       ")
    print("===================================================================")
    print("\nYou wake up on a bench in uptown, as the sun hits your face.")
    print("All you can remeber is studying for 160 hours straight for BUS")
    print("302: Coloring Between the Lines.")
    print("\nYou stand up and look at your wrist, your watch reads 7:30.")
    print("Your head is pounding and theres a fuzzy feeling when you try to")
    print("remeber last night.")
    print("\nAll you can remember is a shadowy figure in a trench coat who")
    print(" called themselves The Hat Man and a bad feeling almost like your")
    print("forgetting something important. Yet as you stand there you start")
    print("to feel a brisk morning breeze hit your lower half... almost like")
    print("you are pantless. But of course due to the Miami University Code")
    print("of Conduct, we will leave your leg coverage status ambigous. You ")
    print("have also realized you're missing your left shoe and your diginity")
    print("\n===================================================================\n")


def chekhovsFlag() -> None:
    if (player.hasFlag()):
        print("You look around. There's nothing new in here. Better keep looking.")
        print("\n===================================================================\n")
        return
    print("As you look around, you see a tile in the ground that's sticking out. Odd...")

    if (not player.hasPants()):
        print("You ignore it. You decide you need to focus on finding your pants.")
        print("\n===================================================================\n")
        return
    
    print("You go up to it and touch the tile. It moves, revealing a dent in the ground.")
    print("\nIt's a Chekhov's [CENSORED BY MIAMI'S VALUES]!")
    print("More specifically, a flag [CENSORED BY MIAMI'S VALUES]!")
    print("Deciding you might need it, you take it with you and leave.")
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
    
    print("\nRealizing its the same shape as the Chekhov\'s [CENSORED BY MIAMI'S ")
    print("VALUES], you insert it into the hole.")
    print("\nThe door opens, and a troll that looks a lot like President Crawford ")
    print("steps out.")

    if (not player.hasPants()):
        print('\nThe troll stares at you in horror. "Where are your clothes from ')
        print('yesterday?! This does not align with Miami\'s Values!"" He slams the ')
        print('door in your face.')
        print("\nYou look down and remember you still don't have all your clothes on.")
        print("Maybe you can find them somewhere else...")
        print("\n===================================================================\n")
        return

    print('\nYou follow the troll inside, anxious to get whatever your last item is.')
    print('Your pants, your shoe... what else is left?')
    print('\n"You\'ve done well," the troll says. "But here is your final riddle to ')
    print('put all you have learned to the test..."')

    incorrect = True
    while (incorrect):
        print('\n"In Miami University\'s Code of Student Conduct 2026-2027, what object ')
        print('to tell the time is depicted on the cover?"')
        print("\nAnswer (or type 'HELP' for guidance): ", end = '')
        answer = input().lower()
        if (answer == 'sundial' or answer == 'sun dial'):
            incorrect = False
            print('\n"That\'s correct! You\'ve successfully proven your knowledge of Miami ')
            print('University\'s Values!"')
            print('\n"For your hard work, here is your final item."')
            player.setExam(True)
            print("The troll hands you pieces of paper stapled together. The top reads 'BUS ")
            print("302: Coloring Between the Lines. Take Home Exam'.")
        elif (answer == 'help'):
            print("\nYou gasp. The help option wasn't useless after all!")
            help()
        else:
            print('"Incorrect!"')
            # check timer
            # if (timer exceeds time):
            #     print('"I am sorry, but it looks like you have run out of time..."')
            #     hatMan()
            #     return
            # else:
            #     print('"I will give you another chance. Use it wisely."')
            #     add to timer
    print("\n===================================================================\n")


def help() -> None:
    print("For more guidance, view Miami University's Student Code of Conduct ")
    print("at the following link:")
    print("https://docs.google.com/document/d/e/2PACX-1vRMucz0S7mWTht0NnItC6y9Vx289nsgQWPpNh5dICrPtNttSJ8hVR-GpD_cQbCvh6q4fqQ4xiROfAWh/pub?urp=gmail_link")


def main():
    start_game()


if __name__ == "__main__":
    main()
