# Notes for web development in the course CS50Web

## Week 0, Intro
- `?field=value&field2=value2` is a query string


## Week 3, Python
- `f"here comes {name}"`, use f string to speed up the printing process.
- decorator is a powerful tool
  ```
  def announce(f):
    def wrapper():
      print("About to run this function...")
      f()
      print("Finished running this function. ")
    return wrapper

  @announce
  def hello():
    print("Hello, world!")
  ```
- except handler is a good way to handle the error
  ```
  try:
    print(x)
  except NameError:
    print("Variable x is not defined")
    sys.exit(1)
  ```

## Week 4, Django
`django-admin startproject test` to start a new project.
`python manage.py runserver` will launch the web application.
`python manage.py startapp hello` to start an app.
- add `hello` to settings.py
```python
from django.http import HttpResponse
def index(request):
  return HttpResponse("Hello world")
```
