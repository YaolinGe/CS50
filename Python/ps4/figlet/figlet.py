import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

fonts = figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))
# print(fonts)

if len(sys.argv) == 1:
    user_input = input("Input: ").strip()
    font = choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            user_input = input("Input: ").strip()
            font = sys.argv[2]
            figlet.setFont(font=font)
            print(figlet.renderText(user_input))
        else:
            sys.exit("Font not found.")
    else:
        sys.exit("Usage: figlet.py -f/--font <font>")
else:
    sys.exit("Usage: figlet.py -f/--font <font>")
