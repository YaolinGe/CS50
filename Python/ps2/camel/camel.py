user_input = input("camelCase: ")
print("snake_case: ", end="")
for c in user_input:
    if c.isupper():
        print("_", end="")
        print(c.lower(), end="")
    else:
        print(c, end="")
print("")