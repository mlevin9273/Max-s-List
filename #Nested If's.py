#Max Levin
#10/20/23
#Nested If's
#Suggested Pet
def suggestedPet():
    print("This is a pet suggester.")
    print("Answer the questions to determine what pet is most suitable for you!")

    ans = input("cute or scary?")
    if ans == "cute":
        ans = input("small or big?")
        if ans == "big":
            ans = input("outside or inside?")
            if ans == "outside":
                print("You should buy a Miniature Horse!")
            else:
                print("You should buy a Cat!")

    ans = input("cute or scary?")
    if ans == "cute":
        ans = input("small or big?")
        if ans == "small":
            ans = input("hair or no hair?")
            if ans == "no hair":
                print("You should buy a Goldfish!")
            else:
                print("You should buy a hamster")

    ans = input("cute or scary?")
    if ans == "scary":
        ans = input("petite or large?")
        if ans == "large":
            ans = input("water or land?")
            if ans == "water":
                print("You should buy an Eel!")
            else:
                print("You should buy a Snake!")

    ans = input("cute or scary?")
    if ans == "scary":
        ans = input("petit or large?")
        if ans == "petit":
            ans = input("shell or no shell?")
            if ans == "no shell":
                print("You should buy a Tarantula!")
            else:
                print("You should buy a Hermit Crab!")

suggestedPet()