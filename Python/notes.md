# Notes for CS50 Python

## Week 0, Intro
- `name.strip()` removes the whitespace at the beginning and end of the string.
- `name.title()` capitalizes the first letter of each word in the string.
- `"hello, \" world \" "` is a string that includes the quotation marks.
- `match` can be used to switch between cases in python
   ```
  name = input("What's your name? ")

  match name:
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
   ```
- `for _ in range(5):` is a way to loop 5 times, `_` is a placeholder for the variable, no effect on the loop.


!!! For unittest, the folder structure should be like this:
```
- src
    - num.py
    - num2.py
    - etc.py
- tests
    - test.py
```
Then in `test.py`, you can add the path to the `src` folder like this:
```python
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'sort'))
```

## Week 3, Exceptions
- `try` and `except` can be used to catch exceptions
- `else` can be used to execute code if no exception is raised
```
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

- `raise` can be used to raise exceptions
- `finally` can be used to execute code regardless of whether an exception is raised or not
- `assert` can be used to check if a condition is true, if not, raise an `AssertionError`
