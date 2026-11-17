from player import Player
from ferrenberg import ferrenberg_room
from chekhovs import chekhovsFlag
from intro import start_game
from gameTime import check_time
from Jaimison import jaimison_room
from crawford import crawford


player = Player()


def main():
    start_game(player)
    check_time()
    input("[Press enter to continue] ")
    print('')
    print("Glancing at your watch, you decide to get moving.")
    print('')
    keepPlaying = True
    while (keepPlaying):
        print("Where to?")
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
            chekhovsFlag(player)
        elif (answer == "4"):
            crawford(player)
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
