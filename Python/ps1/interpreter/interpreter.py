x, y, z = input("Expression: ").split(" ")
# print("x =", x)
# print("y =", y)
# print("z =", z)
match y:
    case "+":
        print(f"{(float(x) + float(z)):.1f}")
    case "-":
        print(f"{(float(x) - float(z)):.1f}")
    case "*":
        print(f"{(float(x) * float(z)):.1f}")
    case "/":
        if z == "0":
            print("Division by zero!")
        else:
            print(f"{(float(x) / float(z)):.1f}")