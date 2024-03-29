# Notes for web development in the course CS50Web

## Week 0, Intro
- `?field=value&field2=value2` is a query string


## Week 2, Python
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

## Week 3, Django
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
- `app/static/app/style.css` is the default location for static files, to avoid conflict with other apps.
- `{% url 'app:view_func' args %}` to create a url in the template, where `args` is the argument for the view function.
- `<a href="{% url 'item_detail' item.pk %}">{{ item.title }}</a>` to create a link in the template.
- check static link in the template: `{% load static %} <img src="{% static 'app/img.png' %}" alt="My image">`
- `<textarea></textarea>` should always be in the same line to avoid issues.

# Week 4, SQL
- Constraints
  * `NOT NULL` makes sure the value is not null
  * `UNIQUE` makes sure the value is unique
  * `PRIMARY KEY` makes sure the value is unique and not null
  * `FOREIGN KEY` makes sure the value is a valid value in another table
  * `CHECK` makes sure the value satisfies a boolean expression
- `mode columns` 
- `.headers yes` to show the headers
- `.mode column` to show the columns