from gameTime import endgame, check_time

def crawford(player) -> None:
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
        print("The troll stares at you in horror.")
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
                input("[Press enter]")
                print('')
                endgame()
                return
            else:
                print("President Crawford: I will give you only one other chance!")
    print("\n===================================================================")