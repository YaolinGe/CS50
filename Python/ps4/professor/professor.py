import random


def main():
    level = get_level()
    correct = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        counter = 0
        while True: 
            z = int(input(f"{x} + {y} = ").strip())
            if z == x + y:
                correct += 1
                break
            else:
                print("EEE")
                counter += 1
                if counter == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
    print(f"Score: {correct}")

def get_level():
    while True: 
        try:
            level = int(input("Level: ").strip())
            if level in range(1, 4):
                return level
        except ValueError:
            pass

        
def generate_integer(level):
    try: 
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except ValueError:
        sys.exit("ValueError: Level must be an integer between 1 and 3.")


if __name__ == "__main__":
    main()