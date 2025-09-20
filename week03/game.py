#Adventure Game
entrance = input("You stand before a dark cave. On the ground, you see a TORCH and a ROPE. Which one do you pick up?")

print("")

#answer
if entrance.lower() == "torch":
    torch = input("You light the torch and enter. A narrow TUNNEL and a stone STAIRCASE appear. Do you take the TUNNEL or the STAIRCASE?")

    print("")
    #answer for torch (tunnel or staircase)

    if torch.lower() == "tunnel":
        narrow = input("An skeleton appears! Do you FIGHT or RUN?")

        print("")
        #answer for tunnel (fight or run)

        if narrow.lower() == "fight":
            print("you use the torch to burn the bones away! You find treasure behind the skeleton. You win!")

        elif narrow.lower() == "run":
            print("you run away and, but you are caught in a trap.")

        else:
            print("Invalid choice. The ogre catches you. Game over.")

    elif torch.lower() == "staircase":
        stone = input("You find a glowing chest. Do you OPEN it or IGNORE it? ")

        print("")
        #answer for staircase (open or ignore)

        if stone.lower() == "open":
            print("The chest contains the mirror of desires! You win!")

        elif stone.lower() == "ignore":
            print("You walk away and miss out on treasure. Game over.")

        else:
            print("Invalid choice. The chest explodes mysteriously. Game over.")

    else:
        print("Invalid choice. You get lost in the cave. Game over.")

elif entrance.lower() == "rope":
    rope = input("The floor collapses beneath you! The rope saves you. Below, there’s a dark lake. Do you enter the WATER or EXPLORE the shore?")

    print("")
    #answer for rope (water or explore)

    if rope.lower() == "water":
        water = input("A sea mermaid pulls you under! Do you FIGHT or ESCAPE?")

        print("")
        #answer for water (fight or escape)

        if water.lower() == "fight":
            print("You defeat the creature and escape with your life. You Win!")

        elif water.lower() == "escape":
            print("You escape safely but miss out on treasure. Game over.")

        else:
            print("Invalid choice. The creature drags you down. Game over.")

    elif rope.lower() == "explore":
        explore = input("You find a rusty bow. Do you TAKE it out or LEAVE it?")

        print("")
        #answer for explore (pull or leave)

        if explore.lower() == "take":
            print("The sbow is magical! You become a hero. You win!")

        elif explore.lower() == "leave":
            print("You walk away and miss out on a magical sword. Game over.")

        else:
            print("Invalid choice. The cave collapses. Game over.")

else:
    print("Invalid choice. The dragon wakes up and you are caught. Game over.")
