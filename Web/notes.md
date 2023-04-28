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
- `django-admin startproject test` to start a new project.
- `python manage.py runserver` will launch the web application.
- `python manage.py startapp hello` to start an app.
- time zone needs to be such as `America/New_York` or `Europe/Oslo` instead of `EST` or `EDT`.
- `python manage.py shell` to enter the shell interactive mode.

- `python manage.py makemigrations projectname` to create a migration file every time you change the model.
- `python manage.py sqlmigrate projectname 0001` to see the sql code that will be executed.
- `python manage.py migrate` to apply the migration every time you change the model.
- loose coupling for the model and the view.
- `urls.py` specifies the mapping between the url and the view. Thus it is good to use a loose coupling in case if we need to upgrade the url later. ]
- `python manage.py test polls` to run the test.



