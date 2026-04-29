import random
import time
import os

# Terminal ki width nikalna
columns = os.get_terminal_size().columns

# Characters jo screen par girenge
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"

# Green color code (Terminal special)
GREEN = "\033[32m"
RESET = "\033[0m"

try:
    while True:
        # Random spaces aur characters print karna
        line = "".join(random.choice(chars) if random.random() > 0.95 else " " for _ in range(columns))
        print(GREEN + line + RESET)
        time.sleep(0.05) # Speed control
except KeyboardInterrupt:
    print("\nMatrix Stopped.")
