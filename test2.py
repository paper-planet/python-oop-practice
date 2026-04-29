import sys
import math
import time
import shutil
import termios
import tty
import select

# --- MAP ---
MAP = [
    "##########",
    "#        #",
    "#   ##   #",
    "#        #",
    "#   #    #",
    "#        #",
    "#   ##   #",
    "#        #",
    "##########",
]

MAP_W = len(MAP[0])
MAP_H = len(MAP)

# --- PLAYER ---
px, py = 5.0, 5.0
angle = 0.0

FOV = math.pi / 3
DEPTH = 20

SHADES = " .:-=+*#%@"

def get_size():
    return shutil.get_terminal_size((80, 24))

def get_input():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)
    return None

# --- COLOR FUNCTION (RGB foreground) ---
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

RESET = "\033[0m"

def run():
    global px, py, angle

    width, height = get_size()

    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

    print("\033[?25l", end="")

    try:
        while True:
            start = time.time()
            output = [""] * height

            for x in range(width):
                ray_angle = (angle - FOV/2) + (x / width) * FOV

                dist = 0
                hit = False

                eye_x = math.cos(ray_angle)
                eye_y = math.sin(ray_angle)

                while not hit and dist < DEPTH:
                    dist += 0.05

                    test_x = int(px + eye_x * dist)
                    test_y = int(py + eye_y * dist)

                    if test_x < 0 or test_x >= MAP_W or test_y < 0 or test_y >= MAP_H:
                        hit = True
                        dist = DEPTH
                    elif MAP[test_y][test_x] == "#":
                        hit = True

                ceiling = int((height / 2) - height / dist)
                floor = height - ceiling

                # brightness factor (0 to 1)
                brightness = max(0, 1 - dist / DEPTH)

                for y in range(height):
                    if y < ceiling:
                        # ceiling (dark blue-ish)
                        color = rgb(10, 10, int(40 * brightness))
                        char = " "
                    elif y <= floor:
                        # walls (orange torch-like)
                        r = int(200 * brightness)
                        g = int(120 * brightness)
                        b = int(40 * brightness)
                        color = rgb(r, g, b)

                        shade_idx = int(brightness * (len(SHADES)-1))
                        char = SHADES[shade_idx]
                    else:
                        # floor (cool gray fade)
                        bval = int(80 * brightness)
                        color = rgb(bval, bval, bval)

                        shade_idx = int(brightness * (len(SHADES)-1))
                        char = SHADES[shade_idx]

                    output[y] += f"{color}{char}{RESET}"

            print("\033[H", end="")
            sys.stdout.write("\n".join(output))
            sys.stdout.flush()

            # --- INPUT ---
            key = get_input()

            move_speed = 0.1
            rot_speed = 0.05

            if key == "a":
                angle -= rot_speed
            if key == "d":
                angle += rot_speed
            if key == "w":
                nx = px + math.cos(angle) * move_speed
                ny = py + math.sin(angle) * move_speed
                if MAP[int(ny)][int(nx)] != "#":
                    px, py = nx, ny
            if key == "s":
                nx = px - math.cos(angle) * move_speed
                ny = py - math.sin(angle) * move_speed
                if MAP[int(ny)][int(nx)] != "#":
                    px, py = nx, ny
            if key == "q":
                break

            time.sleep(max(0, 0.03 - (time.time() - start)))

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        print("\033[?25h")
        print("\nExited.")


if __name__ == "__main__":
    run()