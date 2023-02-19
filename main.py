import random
import time

SC_chance = 20
fishing_speed_multiplier = 0.0001
XP = 0
coins = 0

inventory = []


def fish():
    global XP, coins
    time_for_fish = 20 * fishing_speed_multiplier
    time.sleep(time_for_fish)
    if random.randint(20, 20) != 20:  # 1, 20
        randnum = random.randint(1, 108)
        if randnum <= 60:
            print("You caught a cod and sold it for 6 coins.")
            XP += 25
            coins += 6
        elif randnum <= 85:
            print("You caught a salmon and sold it for 10 coins.")
            XP += 35
            coins += 10
        elif randnum <= 98:
            print("You caught a pufferfish and sold it for 15 coins.")
            XP += 50
            coins += 15
        elif randnum <= 102:
            print("You caught a clownfish and sold it for 20 coins.")
            XP += 100
            coins += 20
        else:
            print("You caught some clay and sold them for 12 coins.")
            XP += 30
            coins += 12
    elif random.randint(1, 10) != 11:  # 10
        randnum = random.randint(1, 88)
        if randnum <= 15:
            randnum = random.randint(1000, 10000)
            print(f"You fished up {randnum} coins.")
            XP += 160
            coins += randnum
        elif randnum <= 30:
            print("You caught a bait (unimplimented).")
            XP += 160
            coins += 0
            inventory.append("bait")
        elif randnum <= 45:
            print("You caught a music disc")
            XP += 160
            inventory.append("music disc")
        elif randnum <= 55:
            print(f"You fished up a golden apple and sold it for 125 coins.")
            XP += 160
            coins += 125
        elif randnum <= 65:
            print(
                f"You fished up a big bottle of green potions and sold it for 4000 coins")
            XP += 160
            coins += 4000
        elif randnum <= 73:
            print(f"You fished up a sea lantern and sold it for 60 coins")
            XP += 160
            coins += 60
        elif randnum <= 78:
            print(f"You fished up a prismarine shard and sold it for 5 coins")
            XP += 50
            coins += 5
        elif randnum <= 83:
            print(f"You fished up a prismarine crystal and sold it for 5 coins")
            XP += 50
            coins += 5
        else:
            print(f"You fished up a piece of sponge and sold it for 50 coins")
            XP += 160
            coins += 50


while True:
    cmd = input("f to fish, h for help: ")
    if cmd == "f":
        fish()
    elif cmd == "h":
        print("""
f - fish
h - help
s - stats
h - hack(debug)
q - quit
        """)
    elif cmd == "s":
        print(f"""
XP: {XP}
Coins: {coins}
        """)
        print("inventory:", inventory)
    elif cmd == "q":
        quit()
