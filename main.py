import random
import time


SC_chance = 20
fishing_speed_multiplier = 1
XP = 0
coins = 0


def fish():
    global XP, coins
    time_for_fish = 20 * fishing_speed_multiplier
    time.sleep(time_for_fish)
    if random.randint(1, 20) != 21:
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
        elif randnum <= 108:
            print("You caught some clay and sold them for 12 coins.")
            XP += 30
            coins += 12


while True:
    cmd = input("f to fish, h for help: ")
    if cmd == "f":
        fish()
    elif cmd == "h":
        print("""
f - fish
h - help
s - stats
q - quit
        """)
    elif cmd == "s":
        print(f"""
XP: {XP}
Coins: {coins}
        """)
    elif cmd == "q":
        quit()
