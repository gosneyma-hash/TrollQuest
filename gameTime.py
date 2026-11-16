# time should be set to 1700 intially so that we can give the player a fair amount of actions
import sys
import time

TOTAL_TIME = 1700
start_time = time.time()
first_seen = False
second_seen = False


def check_time() -> None:
    global first_seen, second_seen

    remaining = TOTAL_TIME - int(time.time() - start_time)

    if remaining <= 0:
        endgame()
    elif remaining <= 425 and not second_seen:
        second_seen = True
        secondSighting()
    elif remaining <= 850 and not first_seen:
        first_seen = True
        firstSighting()


def firstSighting() -> None:
    print("\n--- Half Time (850s Left) ---")
    print("You start to feel your head spin.\n")
    print("You visions starts to blurr.\n")
    print("A hatted silhouetted  is breifly visible.\n")
    print("the spining room slows to a stop and you regain your footing.\n")


def secondSighting() -> None:
    print("\n--- Quarter Time (425s Left) ---")
    print("A cold chill shoots down your spine as your watch ticks louder.")
    print("From the corner of your eye, the tall trench coated figure is much closer now.")
    print("Three pairs of glowing eyes blink at once before vanishing into the shadows.\n")


def endgame() -> None:
    print("Your head begins to feal fuzzy.\n")
    print("You feel your vision start to grow darker.\n")
    print("As you peer into the growing darkeness shrouding yor vision.\n")
    print("You start to see a prestine hatted figure which begins stepping closer.\n")
    print("Three trollish faces stacked a top each other.\n")
    print("You know they've come for you as they reach out there hands and. . .\n")
    print("THIS LINE WAS REDACTED BY MIAMI UNIVERSITIES CODE OF CONDUCT.\n")
    print("the end")
    sys.exit()


# Kept just incase you still need it but if it's good to delete just go ahead!
def completeAction(current_time) -> int:
    current_time -= 50

    if current_time <= 0:
        endgame()

    if current_time == 850:
        firstSighting()
    return current_time

# Kept just incase you still need it but if it's good to delete just go ahead!


def checkTime(current_time: int) -> int:
    print(current_time)
    return current_time
