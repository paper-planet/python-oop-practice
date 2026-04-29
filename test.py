import sys
import time
import math
import shutil

SHADES = " .:-=+*#%@"

def clear():
    print("\033[H", end="")

def get_size():
    return shutil.get_terminal_size((80, 24))

def render_frame(t):
    width, height = get_size()
    cx, cy = width // 2, height // 2

    buffer = []

    for y in range(height):
        row = ""

        for x in range(width):
            # normalize coordinates
            nx = (x - cx) / cx
            ny = (y - cy) / cy

            # square distance (this is the important part)
            dist = max(abs(nx), abs(ny))

            # forward motion
            depth = dist * 1.8 - t * 1.5

            # subtle structure (less chaotic than before)
            pattern = math.sin(depth * 5.5) # (pattern + 1) / 2 * (1 - dist)

            # lighting falloff
            shade_val = (1 - dist) * 0.8 + (pattern * 0.2)

            idx = int(shade_val * (len(SHADES) - 1))
            idx = max(0, min(len(SHADES) - 1, idx))

            row += SHADES[idx]

        buffer.append(row)

    return "\n".join(buffer)


def run():
    t = 0
    print("\033[?25l", end="")  # hide cursor
    try:
        while True:
            clear()
            sys.stdout.write(render_frame(t))
            sys.stdout.flush()
            t += 0.02  # slower = smoother motion
            time.sleep(0.03)
    except KeyboardInterrupt:
        print("\033[?25h")
        print("\nStopped.")


if __name__ == "__main__":
    run()