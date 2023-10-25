"""
Ian King's Game (Hero vs. Monsters)
The Goal of This Project: Design a text-based game where a hero challenges various monsters, each having a unique vulnerability.
These include: (Dragon, Zombie, Ghost, Minotaur, Sword, Arrow, Magic, Hammer)
"""

import random

# Initialize hero's attributes
hero_health = 3  # The hero can withstand 3 incorrect weapon choices, so basically three lives
hero_arsenal = {
    "sword": random.randint(1, 5),
    "arrow": random.randint(1, 5),
    "magic": random.randint(1, 5),
    "hammer": random.randint(1, 5)
}

# Monsters and their weaknesses
monsters = {
    "Dragon": "arrow",
    "Zombie": "sword",
    "Ghost": "magic",
    "Minotaur": "hammer"
}

# Shuffle the order of monsters for random encounters
shuffled_monsters = list(monsters.keys())

def game(hero_health):
    defeated_monsters = 0

    while shuffled_monsters and hero_health > 0:
        current_monster = shuffled_monsters.pop()

        print("You encounter a", current_monster)
        print("Your arsenal:")
        for item, quantity in hero_arsenal.items():
            print(f"{item}: {quantity}")
        print("You have", hero_health, "health points.")

        action = input(f"What will you use against the {current_monster}? (sword, arrow, magic, hammer, exit game): ").lower()

        if action == "exit game":
            print("You chose to exit the game. Game over!")
            break

        if action in hero_arsenal and hero_arsenal[action] > 0:
            if monsters[current_monster] == action:
                print("You defeat the", current_monster, "with your", action)
                hero_arsenal[action] -= 1
                defeated_monsters += 1
            else:
                print("You used the wrong weapon, but you have", hero_health - 1, "health points left.")
                hero_health -= 1
        else:
            print("You don't have that weapon or it's broken. Choose a valid option.")

    if hero_health <= 0:
        print("Your health reached 0. You lose!")

    print("Game Over! You defeated", defeated_monsters, "monsters.")

# Start the game
while True:
    game(hero_health)
    play_again = input("Play again? (yes or no): ").lower()
    if play_again != "yes":
        break