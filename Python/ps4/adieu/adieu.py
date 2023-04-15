import inflect

p = inflect.engine()

names = []
while True: 
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

print("Adieu, adieu, to ", end="")
print(p.join(names))