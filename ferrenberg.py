import random
from player import Player
from gameTime import endgame, check_time

PG_RIDDLES = [
    {
        "question": "You throw away my outside, eat my inside, then throw away the inside. What am I?",
        "answer": "corn"
    },
    {
        "question": "What gets wetter the more it dries?",
        "answer": "towel"
    },
    {
        "question": "What do you call a fake noodle?",
        "answer": "impasta"
    },
    {
        "question": "What has hands and a face, but can not hold anything or smile?",
        "answer": "clock"
    }
]


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
    print("Indeed this respectable professor at the esteem Miami Oxford University has indeed turned to a troll and"
          "have stollen or found your pants.")
    print("Dr. Ferrenberg: Now for me to help you, you must answer my riddle!")
    print("Dr. Ferrenberg: How do you make a plumber cry?")

    attempts = 0
    max_attempts = 3
    selected_riddle = random.choice(PG_RIDDLES)

    while attempts < 1:
        answer = input("Your answer: ").strip().lower()
        check_time()

        if answer == "help":
            help_command()
            continue

        if "kill his family" in answer:
            print("\nDr. Ferrenberg slaps his knee and laughs out loud!")
            print("Dr. Ferrenberg: Correct! Now here is your reward.")
            player.setPants(True)
            print("\n[Item Obtained] Dr. Ferrenberg hands over your pants!")
            print("Dr. Ferrenberg whispers: 'If you're still looking for something, you should check the alley in Uptown.'\n")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(
                f"\nDr. Ferrenberg groans: 'Wrong! That doesn't make any sense!' (Warning: You feel a cold shadow creeping up... {remaining} tries left)")
            print(
                "Dr. Ferrenberg: Let's try something else [CENSORED BY MIAMI UNIVERSITY]?")
            print(
                f"Dr. Ferrenberg: Well maybe something a little more PG: {selected_riddle['question']} \n")

    while attempts < max_attempts:
        answer = input("Your answer: ").strip().lower()
        check_time()
        if answer == "help":
            help_command()
            continue

        if selected_riddle["answer"] in answer:
            print("\nDr. Ferrenberg slaps his knee and laughs out loud!")
            print("Dr. Ferrenberg: Correct! Now here is your reward.")
            player.setPants(True)
            print("\n[Item Obtained] Dr. Ferrenberg hands over your pants!")
            print("Dr. Ferrenberg whispers: 'If you're still looking for something, you should check the alley in Uptown.'\n")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(
                    f"\nDr. Ferrenberg groans: 'Wrong! That doesn't make any sense!' (Warning: You feel a cold shadow creeping up... {remaining} tries left)\n")

    print("\nDr. Ferrenberg: You have failed my riddles... and now he is here.")
    print("===================================================================\n")
    endgame()
