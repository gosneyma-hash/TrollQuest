from player import Player
from intro import start_game
from ferrenberg import ferrenberg_room
# Can be put inside another method


def help() -> None:
    print("Enter one of the listed numbers to choose your option.")
    print("For more guidance, view Miami University's Student Code of Conduct at the following link: https://miamioh.edu/policy-library/students/student-code-of-conduct/")


def main():
    player = Player()

    start_game(player)
    ferrenberg_room(player)


if __name__ == "__main__":
    main()
