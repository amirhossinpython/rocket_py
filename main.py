import os
import time
import sys
from colorama import init, Fore, Back, Style
# ```
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_rocket(position, flame_length):
    rocket = [
        f"{' ' * position}       ^       ",
        f"{' ' * position}      / \\      ",
        f"{' ' * position}     /   \\     ",
        f"{' ' * position}    /_____\\    ",
        f"{' ' * position}   |       |   ",
        f"{' ' * position}   |       |   ",
        f"{' ' * position}   |       |   ",
        f"{' ' * position}  /|       |\\  ",
        f"{' ' * position} / |       | \\ ",
        f"{' ' * position}/  |       |  \\"
    ]
    
    flame = [
        f"{' ' * position}    {'|' * flame_length}    ",
        f"{' ' * position}    {'/' * flame_length}    ",
        f"{' ' * position}   {'_' * (flame_length+2)}   "
    ]
    
    for line in rocket:
        print(Fore.YELLOW + line)
    
    for line in flame:
        print(Fore.RED + line)

def draw_explosion(size):
    explosion = [
        f"   {'*' * size}   ",
        f"  {'*' * (size+2)}  ",
        f" {'*' * (size+4)} ",
        f"{'*' * (size+6)}",
        f" {'*' * (size+4)} ",
        f"  {'*' * (size+2)}  ",
        f"   {'*' * size}   "
    ]
    
    for line in explosion:
        print(Fore.RED + line.center(50))
        time.sleep(0.1)

def launch_sequence():
    print(Fore.GREEN + "\nآماده سازی پرتاب موشک...\n" + Style.RESET_ALL)
    
   
    for i in range(5, 0, -1):
        print(Fore.RED + f"پرتاب در {i} ثانیه..." + Style.RESET_ALL)
        time.sleep(1)
    
   
    print("\n" * 3)
    for i in range(15):
        clear_screen()
        print("\n" * 5)
        draw_rocket(i, min(i, 5))
        time.sleep(0.1)
    
   
    clear_screen()
    print("\n" * 10)
    for size in range(1, 8):
        draw_explosion(size)
    
  
    print("\n" * 2)
    print(Fore.GREEN + "=" * 50)
    print(Fore.RED + "یاعلی ابن ابی‌طالب، حمله به سرزمین‌های اشغالی آغاز شد!".center(50))
    print(Fore.GREEN + "الله اکبر".center(50))
    print("=" * 50 + Style.RESET_ALL)

def main():
    try:
        launch_sequence()
        time.sleep(3)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nپرتاب لغو شد!" + Style.RESET_ALL)
        sys.exit(0)

if __name__ == "__main__":
    main()
