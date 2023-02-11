import random
import time


SC_chance = 20
fishing_speed_multiplier = 1


def fish():
    time_for_fish = 20 * fishing_speed_multiplier
    time.sleep(time_for_fish)
    if random.randint(1, 20) != 21:  # 21 is only for testing
        randnum = random.randint(1, 108)
        if randnum <= 60:
            print("You caught a cod.")
        elif randnum <= 85:
            print("You caught a salmon.")
        elif randnum <= 98:
            print("You caught a pufferfish.")
        elif randnum <= 102:
            print("You caught a clownfish.")
        elif randnum <= 108:
            print("You caught some clay.")


while True:
    cmd = input("f to fish, h for help: ")
    if cmd == "f":
        fish()
    elif cmd == "h":
        print("""
f - fish
h - help
        """)
