from player import Player

# Can be put inside another method


def help() -> None:
    print("Enter one of the listed numbers to choose your option.")
    print("For more guidance, view Miami University's Student Code of Conduct at the following link: https://miamioh.edu/policy-library/students/student-code-of-conduct/")


def start_game(player: Player) -> None:
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


def main():
    player = Player()

    start_game(player)


if __name__ == "__main__":
    main()
