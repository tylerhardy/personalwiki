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
mkdir env
cd env
virtualenv learningLog
cd ..
```
### Install Django
- Activate Virtual env and Install django
```
cd env
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
-