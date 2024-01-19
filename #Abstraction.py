#Abstraction

#Intro
#Parameters (name of user, name of game)
#Introduce user to your game
def intro(user, game):
    def user():
        input("What is your name?")
    def game():
        input("What game do you want to play?")

#Say goodbye
def outro(user, game):
    print("Goodbye", + user + "thanks for playing" + game)

