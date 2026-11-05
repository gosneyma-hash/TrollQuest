# time should be set to 1700 intially so that we can give the player a fair amount of actions


def completeAction(current_time) -> int:
    current_time -= 50

    if current_time <= 0: 
        endgame()

    if current_time == 850:
        firstSighting()
    return current_time

def checkTime(current_time: int) -> int:
    print(current_time)
    return current_time

def firstSighting() -> None:
    print("You start to feel your head spin.\n")
    print("You visions starts to blurr.\n")
    print("A hatted silhouetted  is breifly visible.\n")
    print("the spining room slows to a stop and you regain your footing.\n")


def endgame() -> None:
    print("Your head begins to feal fuzzy.\n");
    print("You feel your vision start to grow darker.\n")
    print("As you peer into the growing darkeness shrouding yor vision.\n")
    print("You start to see a prestine hatted figure which begins stepping closer.\n")
    print("Three trollish faces stacked a top each other.\n")
    print("You know they've come for you as they reach out there hands and. . .\n")
    print("THIS LINE WAS REDACTED BY MIAMI UNIVERSITIES CODE OF CONDUCT.\n")
    print("the end")
