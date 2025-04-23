print("Welcome to the Lorena's Terminal Game!")
print("While exploring a haunted house, you accidentally triggered a trap.")
print("You fell into a dark pit and lost consciousness.")
print("When you wake up, you find yourself in a mysterious dark room.")
print("You hear strange noises and feel a chill in the air.")
print("To survive you need to make a choice to escape!! Which door do you want to open? (left/right)")

door = input("Enter your choice. Choose wisely: ")

if door == "left":
    print("You push open the left door with trembling hands and discover a sparkling treasure chest!")
    print("Do you want to open it? (yes/no)")
    action = input("Enter your choice. Choose wisely: ")
    if action == "yes":
        print("A dazzling burst of light shines out as you reveal a trove of gold coins. Jackpot! You win!")
    else:
        print("You decide not to open the chest. Sometimes, playing it safe comes at a cost... Game over :p")


elif door == "right":
    print("You slowly open the right door and come face-to-face with a wild, bellowing monster!")
    print("Do you want to fight it or run away? (fight/run)")
    action = input("Enter your choice: ")
    if action == "fight":
        print("You muster up your courage and engage in an epic battle, defeating the monster and emerging a hero!")
    else:
        print("You run away safely... but oh, how cowardly you were! Better luck next time. Game over :p")
else:
    print("That door doesn't exist in this creepy mansion. You've completely lost your way. Game over :p")





