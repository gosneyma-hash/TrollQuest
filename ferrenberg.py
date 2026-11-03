from player import Player


def help_command() -> None:
    print("\n--- HELP MENU ---")
    print("Enter one of the listed numbers to choose your option.")
    print("For more guidance, view Miami University's Student Code of Conduct at:")
    print("https://miamioh.edu/policy-library/students/student-code-of-conduct/\n")


def ferrenberg_room(player: Player) -> None:
    print("As you stumble around town you realize you need to find your pants"
          " before you can continue any further.")
    print("But for the life of you, you can't think of where you put them.")
    print("Then as you're walking in front of Farmer School of Business you hear"
          "a whisper in the bushes talking to other sleep deprived students as they pass by.")
    print("As you get closer before you can hear anything a monster, almost troll like"
          "jumps out at you!")
    print("Dr. Ferrenberg: Halt! Oh, it's just you the animal from last night. Look at you"
          "walking around like that, you should be ashamed.")
    print("Dr. Ferrenberg: You know I have something that might just help you with your problem.")
    print("Dr. Ferrenberg: These magical pants!")
    print("You realize this must be a fever dream, but after pinching yourself you snap back to reality.")
    print("Indeed this respectablly professor at the esteem Miami Oxford University has indeed turned to a troll and"
          "have stollen or found your pants.")
    print("Dr. Ferrenberg: Now for me to help you, you must answer my riddle!")
    print("Dr. Ferrenberg: How do you make a plumber cry?")

    first_joke_attempts = 0
    max_first_attempts = 1
    attempts = 0
    max_attempts = 3

    while first_joke_attempts < max_first_attempts:
        answer = input("Your answer: ").strip().lower()

        if answer == "help":
            help_command()
            continue

        if "kill his family" in answer:
            print("\nDr. Ferrenberg slaps his knee and laughs out loud!")
            print("Dr. Ferrenberg: Correct! Now here is your reward.")

            player.setPants(True)
            print("\n[Item Obtained] Dr. Ferrenberg hands over your pants!")
            print("Dr. Ferrenberg whispers: If you're still looking for something, you should check the alley in Uptown.'\n")
            return
        else:
            first_joke_attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(
                    f"Dr. Ferrenberg groans: 'Wrong! That doesn't makes any sense!' (Warning: You feel a cold shadow creeping up... {remaining} tries left)\n")
                print(
                    "Dr. Ferrenberg: Lets try something else CENSORED BY MIAMI UNIVERSITY?")
                print("Dr. Ferrenberg: Well maybe something a little more PG, you throw away my outside, eat my inside, then throw away the inside. What am I?")
    while attempts < max_attempts:
        answer = input("Your answer: ").strip().lower()

        if answer == "help":
            help_command()
            continue

        if "corn" in answer:
            print("\nDr. Ferrenberg slaps his knee and laughs out loud!")
            print("Dr. Ferrenberg: Correct! Now here is your reward.")

            player.setPants(True)
            print("\n[Item Obtained] Dr. Ferrenberg hands over your pants!")
            print("Dr. Ferrenberg whispers: If you're still looking for something, you should check the alley in Uptown.'\n")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(
                    f"Dr. Ferrenberg groans: 'Wrong! That doesn't makes any sense!' (Warning: You feel a cold shadow creeping up... {remaining} tries left)\n")
