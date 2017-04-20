# Setting Up a Project
- When beginning a project you first need to describe the project in a specification, or *spec*.
## Writing a Spec
- A full spec details the project goals, describes the project's functionality, and discusses its appearance and user interface.
- A spec should keep you focused and help keep your project on track.

### Learning Log Spec
We’ll write a web app called Learning Log that allows users to
log the topics they’re interested in and to make journal entries
as they learn about each topic. The Learning Log home page
should describe the site and invite users to either register or log
in. Once logged in, a user should be able to create new topics,
add new entries, and read and edit existing entries.

## Creating a Virtual Environment
- A virtual environment is a place on your system where you can install packages
and isolate them from all other Python packages.

### Learning Log Virtual Environment
- Create a new directory called env and create a virtualenv in the learningLog directory.
```
mkdir venv
cd venv
virtualenv learningLog
cd ..
```
### Install Django
- Activate Virtual env and Install django
```
cd venv
cd learningLog
cd Scripts
activate
pip install django
cd ../../..
```
### Creating a Project in Django
```bash
mkdir learningLog
cd learningLog
git init
vim README.md
django-admin startproject learningLog .
```
- This command tells Django to set up a new project called learningLog.
- The dot at the end of the command creates the new project with a directory structure that contains four files.
- The mose important are:
  - `settings.py`, `url.py`, and `wsgi.py`
  - The `settings.py` file controls how Django interacts with your system and manages your project.
  - The `urls.py` tells Django which pages to build in response to browser requests.
  - The `wsgi.py` file helps Django serve the files it creates.

### Creating the Database and Viewing the Project
- Because Django stores most of the information related to a project in a
database, we need to create a database that Django can work with.
```bash
python manage.py migrate
```
- Issuing the `migrate` command for the first time tells Django to make sure the database matches the current state of the project.
  - Django creates a new database.
```bash
python manage.py runserver
```
- Django checks to make sure the project is set up properly.
  - If you receive the error message That port is already in use, tell Django to use a different port by entering `python manage.py runserver 8001` and cycle through higher numbers until you find an open port.

## Starting the App
- A Django project is organized as a group of individual apps that work together to make the project work as a whole.
- Run the startapp command:
```shell
python manage.py startapp main_app
```
- The command startapp `name` tells Django to create the infrastructure needed to build an app.
  - The important files are `models.py`, `admin.py`, and `views.py`.

### Defining Models
- Each user will need to create a number of topics in their learning log. Each entry they make will be tied to a topic, and these entries will be displayed as text. We’ll also need to store the timestamp of each entry so we can show users when they made each entry.
- Open `models.py`
- A model tells Django how to work with the data that will be stored in the app.
- Code-wise, a model is just a class; it has attributes and methods.
- To see the different kinds of fields you can use in a model, see the Django Model Field Reference at https://docs.djangoproject.com/en/1.11/ref/models/fields/. You won’t need all the information right now, but it will be extremely useful when you’re developing your own apps.

### Activating Models
- To use our models, we have to tell Django to include our app in the overall project.
- Open settings.py, and you’ll see a section that tells Django which apps are installed in the project
- Add the `app_name` (main_app) to the `INSTALLED_APPS=[` portion in settings.py
- Tell Django to modify the database so it can store information related to the model `Topic`.
```shell
python manage.py makemigrations main_app
```
- The command `makemigrations` tells Django to figure out how to modify the database so it can store the data associated with any new models we’ve defined.
- Apply this migration and have Django modify the database.
```shell
python manage.py migrate
```
- **Note**: Whenever we want to modify the data that `App Name` manages, we'll follow these three steps:
  1. Modify `models.py`
  2. Call `makemigrations` on `main_app`
  3. Tell Django to `migrate` the project.

## The Django Admin Site
- Django makes it easy for you to work with your models through the *admin site*.
### Setting Up a Superuser
- Django allows you to create a user who has all privileges available on the site, called a *superuser*.
- **Privilege** controls the actions a user can take.
- To create a superuser in Django use the following command:
```shell
python manage.py createsuperuser
```
- You will be prompted to enter the following:
  - Username:
  - Email:
  - Password:
  - Comfirm Password:
- **Note:** Some sensitive information can be hidden from a site’s administrators. For example, Django doesn’t actually store the password you enter; instead, it stores a string derived from the password, called a hash. Each time you enter your password, Django hashes your entry and compares it to the stored hash. If the two hashes match, you’re authenticated. By requiring hashes to match, if an attacker gains access to a site’s database, they’ll be able to read its stored hashes but not the passwords. When a site is set up properly, it’s almost impossible to get the original passwords from the hashes.
### Registering a Model with the Admin Site
- Django includes some models in the admin site automatically.
  - Such as `User` and `Group`.
- Open `admin.py`
- To register the model `Topic` enter it into the admin site.
```python
from main_app.models import Topic
admin.site.register(Topic)
```
- This code imports the model we want to register (`Topic`) and then uses `admin.site.register()` to tell Django to manage our model through the admin site.
- Navigate to http://localhost:8000/admin/ and enter the site using the superuser created earlier.

### Adding Topics
- The model `Topic` should now be registered with the admin site.
- In the http://localhost:8000/admin/ site click on Topics to go to the Topics page.
- Click `Add` to add new topics

## Defining the Entry Model
- To record what we've been learning about the topics we've added we need to define a model for the kinds of entries users can make in their learning logs.
- Each entry needs to be associated with a particular topic.
  - This relationship is called a *many-to-one relationship*, meaning entries can be associated with one topic.
- Open `modify.py`
  - (Refer to `models.py` for the information added)

## Migrating the Entry Model
- With every addition of a new model we must migrate the database again.
- This process will become quite familiar:
  1. Modify `models.py`
  2. Run command: `python manage.py makemigrations main_app`
  3. Run command: `python manage.py migrate`

## Registering Entry with the Admin Site
- Modify the `admin.py` file to register the `Entry` model we just created.
- Now you can add/modify entries under the topics added.

## The Django Shell
- You can examin the data programmatically through an interactive terminal session.
- This interactive environment is called the Django Shell.
```shell
python manage.py shell
```
```shell
from main_app.models import Topic
Topci.objects.all()
```
- We import the model `Topic` from the `main_app.models` module.
- We then use the method `Topic.objects.all()` to get all of the instances of the model `Topic`.
  - The list returned is called a *queryset*.
- We can loop over a queryset just as we'd loop over a list.
```shell
topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)
```
- If you know the ID of a particular object you can get that object and examine any attribute the object has.
```shell
t = Topic.objects.get(id=1)
t.text

t.date_added

```
- We can also look at the entries related to a certain topic.
```shell
t.entry_set.all()
```
- To get data through a foreign key relationship you use the lowercase name of the related model followed by an underscore and the word set.
- **Note:** Each time you modify your models, you’ll need to restart the shell to see the effects of those changes. To exit a shell session, enter `ctrl-D`; on Windows enter `ctrl-Z` and then press `enter`.

# Making Pages: The learning Log Home Page
- Making webpages with Django consists of three stages:
  1. Defining URLs
  2. Writing Views
  3. Writing Templates
- First, you must define patterns for URLs.
  - A URL pattern describes the way the URL is laid out and tells Django what to look for when mathcing a browser request with a site URL so it knows which page to return.
- Each URL then maps to a particular *view*--the view function retrieves and processes the data needed for that page.
- The view function often calls a *template*, which builds a page that the browsers can read.
- Make a home page for Learning Log Project.
  - Define the URL for the home page
  - Write its view function
  - Create a simple template
## Mapping a URL
- Users request pages by entering URLs into a browser and clicking links.
- By default Django the base URL is mapped to http://localhost:8000/.
- We will change this by mapping the base URL to Learning Log's home page.
- Open `urls.py`
- The first two lines import the functions and modules that manage URLs for the project and admin site.
- Add the following import statement:
```python
from django.conf.urls import include
```
- The body of the file defines the `urlpatterns` variable.
- The code in `urlpatterns` inlcudes the modul `admin.site.urls` which defines all the URLs that can be requested from the admin site.

## Writing a View
### Creating `urls.py` in main_app
- Modify root `urls.py` to include link to `main_app/urls.py`
```python
url(r'', include('main_app.urls', namespace='main_app')),
```
- Created the module `urls.py` in the `main_app` folder
- Imported the `url` module.
```python
from django.conf.urls import url
```
- Imported the `views` module from within current directory `.`
```python
from . import views
```
- Created a new variable `urlpatterns` as a list.
```python
urlpatterns = []
```
- Added a `url()` in the list.
```python
url(r'^$', views.index, name='index'),
```
### Modifying the `view.py` file
- Created a function in the `view.py` file.
  - The function will have to process any data but return the request to the `render()` function.
  - The `render()` function takes in two arguments, the original `request` object and a template it can use to build the page.
```python
def index(request):
    """The home page for Learnig Log"""
    return render(request, 'main_app/index.html')
```

## Writing a Template
- A template sets up the structure for a webpage.
- It defines what the page should look like.
- Django fills in the relevant data each time the page is requested.
- It allows you to access any data provided by the view.

# Building Additional Pages
## Template Inheritance
- Base templates can be used to contain repeated elements.
- Each page can inherit from the template.

### The Parent Template
- open `templates/main_app` and create a new file called `base.html`
```html
<p>
    <a href="{% url 'main_app:index' %}">Learning Log</a>
</p>
{% block content %}{% endblock content %}
```
- A *template tag* are indicated by braces and the percent sign `{% %}`.
- A template tag is a bit of code that generates information to be displayed on a page.
  - `<a href="{% url 'main_app:index' %}">Learning Log</a>`
    - The `main_app:index` generates a URL matching the URL pattern defined in `main_app/urls.py` with the name `index`.
  - In this example the `main_app` is the *namespace* and `index` is a uniquely named URL pattern in that namespace.
- The pair of `block tags`, named `content`, is a placeholder.
  - The child template will define the kind of information that goes in the content block.
  - A child template doesn't have to define every block from its parent.
  - You can reserve space in parent templates for as many blocks as you like.
  - The child template uses only as many as it requires.
- **Note:** In Python code, we almost always indent four spaces. Template files tend to have more levels of nesting than Python files, so it’s common to use only two spaces for each indentation level.

### The Child Template
- open `index.html` and rewrit to inherit from `base.html`