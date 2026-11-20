from player import Player
from ferrenberg import ferrenberg_room
from chekhovs import chekhovsFlag
from intro import start_game
from gameTime import check_time, help_command
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
        print("[5] Not a Casino")
        print("[6] Help")
        answer = input("Choice: ").strip().lower()
        check_time()

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
        elif (answer == "5"):
            if player.hasPants() and player.hasShoe():
                print("\nNot a security guard: See you're finally dressed, but still this place ain't open till the weekend. Don't you have something better to do?")
            else:
                print(
                    "You try to enter a suspicious looking building labeled 'Not a Casino'.")
                print(
                    "\nNot a security guard: You can't be trying to enter there looking like that.")
        elif (answer == "6" or answer == "help"):
            help_command()
        else:
            print("\nInvalid choice.")

        if (keepPlaying):
            input("[Press enter to continue] ")
            print('')
        else:
            print(
                "\nYou've survived Uptown, recovered your pants, shoes, and secured the BUS 302 Take Home Exam!")
            input("[Press enter to exit game]")


if __name__ == "__main__":
    main()
