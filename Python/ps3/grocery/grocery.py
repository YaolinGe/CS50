
def get_grocery_list(): 
    """ Get the user inputted the grocery list, sort the list and then count the number of items in the list. """
    grocery_list = dict()
    while True: 
        try: 
            item = input("").strip().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except KeyError:
            pass
        except EOFError:
            break
    
    grocery_list = sorted(grocery_list.items())
    for item, count in grocery_list:
        print(f"{count} {item}")


if __name__ == "__main__":
    get_grocery_list()       