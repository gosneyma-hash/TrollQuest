def chekhovsFlag(player) -> None:
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