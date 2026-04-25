from random import randint
from sys import stdout
from time import sleep, time

def roll(min_val, max_val):
    return randint(min_val, max_val)


def animate_roll(final_value, duration=1.0):
    start_time = time()
    
    while time() - start_time < duration:
        fake = randint(1, final_value if final_value > 1 else 1)
        stdout.write(f"\rRolling... {fake}")
        stdout.flush()
        sleep(0.05)

    stdout.write(f"\rFinal Roll: {final_value}      \n")

def animate_screen(duration=0.3):
    width = 80
    steps = int(duration / 0.02)

    for i in range(steps):
        fill = int((i / steps) * width)
        bar = "=" * fill + " " * (width - fill)
        print(f"\r{bar}", end="")
        sleep(0.02)

    print()  # move to next line