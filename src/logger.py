import sys, time

COLORS = {
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'green': '\033[92m'
}


def print_like_human(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


def input_like_human(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    return input().lower().strip()