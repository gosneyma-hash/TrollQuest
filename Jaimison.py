from player import Player
from gameTime import check_time, endgame

def jaimison_room(player: Player) -> None:
    print("\n===================================================================\n")

    if player.hasShoe():
        print("Troll Jaimison: You've already answered my riddle.")
        print("\n===================================================================\n")
        return

    print("You follow the alleyway behind Uptown.")
    print("A mysterious figure emerges from the shadows.")
    print("His trollish features are off puting but you think you can make out a face.")
    print(" Seeing the all to familiar soccer jersy it comes to you in an instant!")
    print("this is none other than a trollish version of jamison")

    print("Professor Jaimison calmly holds up your missing left shoe.")
    print("To get this back you'll need to answer my one little question")
    print("What is the value of the squareroot(lim[x->-4] (x^2 - 16)/ (x-4))?")

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print("\nTroll Jamison")
        print("What is the value of the squareroot(lim[x->-4] (x^2 - 16)/ (x-4)).")
        print("\n Type 4 to ask Jaimison a question")
        answer = input("Your answer: ")

        try:
            validanswer = int(answer)
            
            if validanswer == 4:
                nope = input("Enter your question: ")
                print("\n Thats a good question!")
                attempts -= 1
                continue
            
            if validanswer == 0:
                print("\nTroll Jaimisons lips parse into a deep smile.")
                print("Take your shoe")

                player.setShoe(True)

                print("[Shoe has now been obtained]")
                print("Troll Jaimison run off now!")
                print("===================================================================\n")
                return 

            attempts += 1
            if attempts < max_attempts & validanswer != 4:
                print( f"Troll Jaimison: Incorrect. {max_attempts - attempts} attempts remaining.")
                print("\nTroll Jaimison: Out of attempts.")
                print("You see his figure start to morph into a tall lumpy troll")
                print("Three trollish faces peer out at you as you grabbed by the Hat Troll")
                print("\n===================================================================\n")
                endgame()
        except ValueError:
            attempts+=1
