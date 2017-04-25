# Styling and Deploying an App
- Styling: use the Bootstrap library.
  - The Bootstrap library is a collection of tools for styling web applications so they look professional on all modern devices.
- We will be using django-bootstrap3 app.
- Deploy using 'Heroku'.
- Use Git to track changes in the project.
## Styling Learning Log
- Introduce to django-bootstrap3.

### The django-bootstrap3 App
- Install the django-bootstrap3 app in your virtual environment:
```shell
pip install django-bootstrap3
```
- Modify `settings.py` under `INSTALLED_APPS` with bootstrap3
```py
# Third party apps
'bootstrap3',
```
- Add 'jQuery', a JavaScript library that enables some of the interactive elements that the Bootstrap template provides.
- Add the code at the end of `settings.py`:
```py
# Settings for django-bootstrap3
BOOTSTRAP3 = {
  'include_jquery':True
}
```

### Using Bootstrap to Style Learning Log
- We will modify `base.html` and some of `index.html`

### Modifyin `base.html`
- Need to modify `base.html` template to accomodate the Bootstrap template.

#### Defining the HTML Headers
- The first change to `base.html` defines the HTML headers in the file so whenever a Learning Log page is open, the browser title bar displays the site name.
- We will add some requirements for using Bootstrap in our templates.
- Delete everything in `base.html` and replace it with the following code:
```html
{% load bootstrap3 %}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Learning Log</title>

        {% bootstrap_css %}
        {% bootstrap_javascript %}
    </head>
```
- We load the collection of template tags available in django-bootstrap3.
- Declare this file as an HTML document written in English.
- We include a `title` element for the page.
- We use one of django-bootstrap3's custom template tags.
  - It tells Django to include all the Bootstrap style files.
- The tag that follows enables all the interactive behavior you might use on a page.

#### Defining the Navigation Bar
- Append `base.html` with the following:
```html
    <body>

        <!-- Static nabvar -->
        <nav class="navbar navbar-default navbar-static-top">
            <div class="container">

                <div class="navbar-hearder">
                    <button type="button" class="navbar-toggle collapsed" 
                        data-toggle="collapse" data-target="#navbar" 
                        aria-expanded="false" aria-controls="navbar">
                    </button>
                    <a class="navbar-brand" href="{% url 'main_app:index' %}">Learning Log</a>
                </div>

                <div id="navbar" class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="{% url 'main_app:topics' %}">Topics</a></li>
                    </ul>

                    <ul class="nav navbar-nav navbar-right">
                        {% if user.is_authenticated %}
                            <li><a>Hello, {{ user.username }}.</a></li>
                            <li><a href="{% url 'users:logout' %}">log out</a></li>
                        {% else %}
                            <li><a href="{% url 'users:register' %}">register</a></li>
                            <li><a href="{% url 'users:login' %}">log in</a></li>
                        {% endif %}
                    </ul>
                </div><!--/.nav-collapse -->
            
            </div>
        </nav>
```
- A selector determines which elements on a page a certain style rule applies to.

#### Defining the Main Part of the PAge
- The rest of `base.html` contains the main part of the page:
```html
        <div class="container">

            <div class="page-header">
                {% block header %}{% endblock header %}
            </div>
            <div>
                {% block content %}{% endblock content %}
            </div>

        </div><!-- /container -->
    </body>
</html>
```

### Styling the Home Page Using a Jumbotron
- Update the home page using the newly defined `header` blocker and another Bootstrap element called a *jumbotron*.
```html index.html
{% extends "main_app/base.html" %}

{% block header %}
    <div class="jumbotron">
        <h1>Track your learning.</h1>
    </div>
{% endblock header %}

{% block content %}
    <h2>
        <a href="{% url 'users:register' %}">Register an account</a> to make your own Learning Log, and list the topics you're learning about.
    </h2>
    <h2>
        Whenever you learn something new about a topic, make an entry summaraizing what you've learned.
    </h2>
{% endblock content %}
```

### Styling the Login Page
- modify the login page:
```html login.html
{% extends "main_app/base.html" %}
{% load bootstrap3 %}

{% block header %}
    <h2>Log into your account.</h2>
{% endblock header %}

{% block content %}

    <form method="POST" action="{% url 'users:login' %}" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
        <button name="submit" class="btn btn-primary">log in</button>
        {% endbuttons %}

        <input type="hidden" name="next" value="{% url 'main_app:index' %}" />
    </form>
{% endblock content %}
```

### Styling the `new_topic` Page
- Modify the `new_topic.html` page with the following:
```html new_topic.html

```