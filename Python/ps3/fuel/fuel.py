def get_fraction(): 
    while True: 
        try: 
            x, y = input("Fraction: ").strip().split("/")
            if int(x) > int(y):
                continue
            return int(x) / int(y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def main():
    z = round(get_fraction() * 100)
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")

if __name__ == "__main__":
    main()