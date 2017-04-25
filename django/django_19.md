# User Accounts
## Allowing Users to Enter Data
- Add pages that allow users to enter their own data.
  - Give users the ability to add a new topic, add a new entry, and edit their previous entries.

### Adding New Topics
- Give users the ability to add a new topic.
- Form based pages works in much the same way as the pages created previously.
  - Define a URL, write a view function, and write a template.
  - One major difference is the addition of a new module called forms.py.

#### The Topic ModelForm
- A `form` is a page that allows users to submit data.
- Validate provided information that it is correct.
- Process and save valid information to the database.
- `ModelForm` is a simple way to build a form in Django.
- The `ModelForm` uses the data defined in models to build the form.
```python
# forms.py Example
from django import forms
from . models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
```
- First import the `forms` module.
- Import the `Topic` model.
- Define a class called `TopicForm` which inherits from `forms.ModelForm`.
  - A simple version of a `ModelForm` consists of a nested `Meta` class telling Django which model to base the form on and which fields to include in the form.
- Build a form from the `Topic` model and include only the `text` field.
  - The fields and labels variables tell Django to not generate a label for the text field.

#### The new_topic URL
- The URL for a new page should be short and descriptive
- The URL pattern for the `new_topic` page that will be added to `main_app/urls.py`
```python
# new_topic urlpattern Example
# Page for adding a new topic
url(r'^new_topic/$', views.new_topic, name='new_topic')
```

#### The `new_topic()` View Function
- The `new_topic()` function will need to handle two different situations:
  - Inital requests for the `new_topic` page.
  - Processing of any data submitted in the form.
- It will then redirect the user back to the `topics` page.
```python
# new_topic() Example
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import TopicForm

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted: process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:topics'))
    context = {'form': form}
    return render(request, 'main_app/new_topic.html', context)
```
- Import the class `HttpResponseRedirect` which will redirect the reader back to the topics page after they submit their topic.
- The `reverse()` function determines the URL from a named URL pattern.
  - Django will generate the URL when the page is requested.
- Import the form we just wrote, `TopicForm`.

#### GET and POST Requests
- Two main types of request in web apps:
  - GET requests
  - POST requests
- GET requests for pages that only read data from the server.
- POST requests when the user needs to submit information through a form.
- The function `new_topic()` takes in the request object as a parameter.
  - When user initially requests this page their browser will send a GET request.
  - When user has filled out and submitted the form their browser will submit a POST request.
- Depending on the request we will know whether the user is requesting a blank form (GET request) or asking us to process a completed form (POST request).
  - The `if` statement determines whther the request method is GET or POST.
- If GET, make an instance of `TopicForm`, store it in the variable `form`, and send the form to the template in the context dictionary variable.
  - Since there were no arguments passed to `TopicForm` Django creates a blank form that the user can fill out.
- If POST, the else block will run and processes the data submitted in the form.
  - Make an instance of `TopicForm` and pass it the data entered by the user, stored in `request.POST`.
  - The `form` object that is returned contains the information submitted by the user.
- Check the information to verify that it is valid.
  - The `is_valid()` function checks that all required fields have been filled in.
    - All fields in a form are required by default.
  - The function checks if the data entered matches the field types expected.
- If the data entered is valid then we can call `save()`.
  - The `save()` function writes the data from the form to the database.
- Once data is saved we can leave the page.
  - The `reverse()` function to get the URL for the topics page.
  - Passes the URL to `HttpResponseRedirect()`.
    - The `HttpResponseRedirect()` function redirects the user's browser to the `topics` page.
- On the `topics` page the user should see the topic they just entered.

#### The new_topic Template
- Create a new template called `new_topic.html` to display the form we just created:
```html
<!--new_topic.html Example-->
{% extends "main_app/base.html" %}
{% block content %}
    <p>Add a new topic:</p>
    <form action="{% url 'main_app:new_topic' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">add topic</button>
    </form>
{% endblock content %}
```
- This template extends `base.html` so it has the same base structure as the rest of the project.
- Define an HTML form.
  - The `action` argument tells the server where to send the data submitted in the form.
    - It is sent back to the view function `new_topic()`
  - The `method` argument tells the browser to submit the data as a POST request.
- Django uses the template tag `{% csrf_token %}` to prevent attackers from using the form to gain unauthorized access to the server.
  - This attack is called a *cross-site request forgery*.
- The form is displayed.
  - Django makes tasks such as displaying a form very simple.
  - The template variable `{{ form.as_p }}` is needed for Django to create all fields necessary to display the form automatically.
    - The `as_p` modifier tells Django to render all the form elements in paragraph format.
- Django doesn't create a submit button so we define one for our form.

#### Linking to the new_topic Page
- Inlcude a link to the `new_topic.html` page on the `topics.html` page:
```html
<!--adding link to new_topic.thml-->
<a href="{% url 'main_app:new_topic' %}">Add a new topic:</a>
```
- The link is placed after the list of existing topics.

### Adding New Entries
- Define a URL, write a view function and a template, and link to the page.
- Create another calss to forms.py

#### The `Entry` ModelForm
- Create a form associated with the `Entry` model.
```python
# Entry ModelForm Example
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
```
- Update the `import` statement to include `Entry` as well as `Topic`.
- The class `EntryForm` inherits from `forms.ModelForm`
  - A simple version of a `ModelForm` consists of a nested `Meta` class telling Django which model to base the form on and which fields to include in the form.
- Build a form from the `Entry` model and include only the `text` field.
  - The fields and labels variables tell Django to not generate a label for the text field.
- The class `Meta` includes the `widgets` attribute.
  - A *widget* is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list.
- By including the `widgets` attribute you can override Django's default widget choices.
- By telling Django to use a `forms.Textarea` element, you customize the input widget for the field `'text'` so the text area will be 80 columns wide.
  - The default is 40.

#### The new_entry URL
- Include a `topic_id` argument in the URL for adding a new entry.
  -  Each new entry must be associated with a particular topic.
```py
# Page for adding a new entry
url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
```
- This URL pattern matches any URL with the form `http://localhost:8000/new_entry/id/` where `id` is a number matching the topic ID.
- The code `(?P<topic_id>\d+)` captures a numerical value and stores it in the variable `topic_id`.
  - When a URL matching this pattern is requested, Django sends the request and the ID of the topic to the `new_entry()` view function.

#### The `new_entry()` Function
- The `view` function for `new_entry` is much like the function for adding a new topic:
```py
# new_entry() Example
from .forms import TopicForm,EntryForm
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('main_app:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'main_app/new_entry.html', context)
```
- Update the `import` statement to include `EntryForm`.
- The definition `new_entry()` has a `topic_id` parameter to store the value it receives from the URL.
  - The topic is needed to render the page and process the form's data.
- Check if it is a GET or POST.
- If GET, then a blank form is returned.
- If POST, then the data is processed by making an instance of `EntryForm`, populated with the POST data from the `request` object.
- Check if the form is valid.
  - If form is valid set the entry object's `topic` attribute before saving it to the database.
- The `save()` function is called with the argument `commit=False` to tell Django to create a new entry object and store it in `new_entry` without saving it to the database.
- Set `new_entry`'s `topic` attribute to the topic we pulled from the database at the beginning of the function.
- The `save()` function is called with no arguments to save the entry to the database with teh correct associated topic.
- The user is redirected to the topic page.
- The `reverse()` function requires two arguments:
  - The name of the URL pattern we want to generate a URL for.
  - The `args` list containing any arguments that need to be included in the URL.
    - The `args` list has one item in it, `topic_id`.
- The `httpResponseRedirect()` call then redirects the user to the topic page they made an entry for.
  - The new entry should appear in the list of entries.

#### The `new_entry` Template
- The template for `new_entry` is similar to the template for `new_topic`.
```html
<!--new_entry.html example-->
{% extend "main_app/base.html" %}
{% block content %}
    <p><a href="{% url 'main_app:topic ' topic.id %}">{{ topic }}</a></p>
    <p>Add a new entry:</p>
    <form action="{% url 'main_app:new_entry' topic.id %}" method='POST'>
        {% csrf_token %}
        {{ form.as_p }}
        <button name='submit'>add entry</button>
    </form>
{% endblock content %}
```
- The topic is shown at the top of the page.
- The form's `action` argument includes the `topic_id` value in the URL.
  - This allows the view function can associate the new entry with the correct topic

#### Linking to the `new_entry` Page
- Include the link to the `new_entry` page from each topic page:
```html
<p>
    <a href="{% url 'main_app:new_entry' topic.id %}">add new entry</a>
</p>
```
- The `new_entry` link is just before the showing entries.

### Editing Entries
- Make a page that allow users to edit the entries they've already added.

#### The `edit_entry` URL
- The URL for the page needs to pass the ID of th entry to be edited:
```py
# Page for editing an entry
url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
```
- The ID passed in the URL is stored in the parameter `entry_id`.
- The URL pattern sends requests that match this format to the view function `edit_entry()`.

#### The `edit_entry()` View Function
- When the `edit_entry` page receives a GET request the `edit_entry()` will return a form for editing the entry.
- When the `edit_entry` page receives a POST request with revised entry text it will save the modified text into the database.
```py
# edit_entry() Example
def edit_entry(request, entry_id):
    """Edits an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Inital request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'main_app/edit_entry.html', context)
```
- Import the `Entry` model.
- Initiate the entry object to edit and the topic associated with this entry.
- If block checks for GIT or POST.
- If GET request, we make an instance of `EntryForm` with the argument `instance=entry`.
  - This argument tells Django to create the form prefilled with information from the existing entry object.
- IF POST request, we pass the `instance=entry` arguement and the `data=request.POST` argument.
  - These arguments tell Django to create a form instance base on the information associated with the existing entry object, updated with any relevant data from `request.POST`.
- Check the form if valid, if form is valid the `save()` function is called with no arguments.
- The user is redirected to the `topic` page.
- The updated entry will be present in the `topic` page.

#### The `edit_entry` Template
- It is similar to `new_entry.html`.
```html
<!--edit_entry.html Example-->
{% extends "main_app/base.html" %}
{% block content %}
<p><a href="{% url 'main_app:topic' topic.id %}">{{ topic }}</a></p>
<p>Edit Entry:</p>
<form action="{% url 'main_app:edit_entry' entry.id %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <button name='submit'>save changes</button>
</form>
{% endblock content %}
```
- The `action` argument sends the form back to the `edit_entry()` function for processing.
- The Entry ID is included as an argument in the `{% url %}` tag.
  - This allows the view function able to modify the correct entry object.

#### Linking to the `edit_entry` Page
- Include a link to the `edit_entry` page for each entry on the topic page:
```html
<!--link to edit_entry.html Example-->
<p>
    <a href="{% url 'main_app:edit_entry' entry.id %}">edit entry</a>
</p>
```
- The `edit_entry` link is after each entry's date and text displayed.
- The `{% url %}` template tag to determine the URL for the named URL pattern `edit_entry`, along with the ID attribute of the current entry in the loop (`entry.id`).
- The link text `edit entry` appears after each entry on the page.

## Setting Up User Accounts
- Setup user registration and authorization system.
- Creat a new app to contain all the functionality related to working with users.
- Modify the `Topic` model slightly so every topic belongs to a certain user.
### The `users` App
- Create a new app called `users` using the startapp command:
```shell
manage.py startapp users
```

#### Adding users to settings.py
- Add the new app to `INSTALLED_APPS` in settings.py:
```py
'users',
```

#### Including the URLs from users
- Modify the root `urls.py` so it includes the URLs for the `users` app:
```py
url(r'^users/', include('users.urls', namespace='users')),
```
- The added line will include the file `urls.py` from `users`.
- This will match any URL that starts with the word *users*.
- The namespace `'users'` was also created so that URLs can be distinguished from those used in the `main_app` app.

### The Login Page
- Use the default `login` view Django provides.
- Create a new `urls.py` file in the directory `learningLog/users/`.
- Add the follwoing:
```python
"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login Page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    
]
```
- Import the default `login` view.
- The login page's pattern matches the URL `http://localhost:8000/users/login/`.
- When Django reads this URL, the word `users` tells Django to look in `users/urls.py`, and `login` tells it to send requests to Django's default `login` view.
- Because we are not writing our own view function, we pass a dictionary telling Django where to find the template we're about to write.
- This template will be part of the `users` app, not the `main_app` app.

#### The `login` Template
- Django will use its default `login` view when users request the login page.
- We still need to provide a template for the page.
- Create a new directory in `learningLog/users/` called `templates`.
- Create another directory called `users` within the newly created `templates` folder.
- Create a `login.html` file in the `users` folder within the `templates` folder.
```html
{% extends "main_app/base.html" %}
{% block content %}
{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}
<form method="POST" action="{% url 'users:login' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">log in</button>
    <input type="hidden" name="next" value="{% url 'main_app:index' %}" />
</form>
{% endblock content %}
```
- This templates extends `base.html` to ensure that the login page will have the same look and feel as the rest of the site.
  - The template in one app can extend a template from another app.
- If the form's `rrors` attribute is set, we display an error message.
  - The error message reports that the username and password combination don't math.
- We want the login view to process the form so we set the `action` argument as the URL of the login page.
- The login view sends a form to the template.
- Include a hidden form element, `next`.
  - The `value` argument tells Django where to redirect the user after they've logged in successfully.

#### Linking to the Login Page
- Add the login link to `base.html` so it is on every page.
- We don't want the link to appear once the user has logged in so it is nested in a `{% if %}` tag.
```html
{% if user.is_authenticated %}
    Hello, {{ user.username }}.
{% else %}
    <a href="{% url 'users:login' %}">log in</a>
{% endif %}
```
- In Django's authentication system, every template has a `user` variable available, which always has an `is_authenticated` attribute set:
  - The attribute is `True` if the user is logged in.
  - The attribute is `False` if the user is not logged in.
- This allows you to display one message to authenticated users and another to unauthenticated users.
- Display a greeting to users logged in.
- Authenticated users have an additional `username` attribute set, which we use to personalize the greeting and remind the user they're logged in.
- Display a link to the login page for users who haven't been authenticated.

#### Using the Login Page
- Enter in the username and password created earlier.

### Logging Out
- Provide a way for users to log out.
- Doesn't have to be a new page.
- Define a URL pattern for the logout link, write a view function, and provide a logout link in base.html

#### The `logout` URL
- Define the URL pattern for loggin out in `users/urls.py`.
```py
# Logout page
url(r'^logout/$', views.logout_view, name='logout'),
```
- The URL pattern sends the request to the `logout_view()` function which is anemed as such to distinguish it from the `logout()` function we will call from within the view.

#### The `logout_view()` View Function
- The `logout_view()` function is straightforward:
  - Import Django's `logout()` function, call it, and then redirect back to the home page.
```py
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))
```
- Import the `logout()` function from `django.contrib.auth`.
- In the function we call `logout()` which requires the `request` object as an argument.
- Redirect to the home page.

#### Linking to the `logout` View
- Include the logout link as part of `base.html` so it is available on every page.
- Include it in the `{% if user.is_authenticated %}` portion.
```html
<a href="{% url 'users:logout' %}">log out</a>
```

### The Registration Page
#### The register URL
- Add the URL pattern for the registration page.
```py
# Registration Page
url(r'^register/$', views.register, name='register')
```

#### The `register()` View Function
- The `register()` view function needs to display a blank registration form when the registration page is first requested.
- Process completed registration forms when they're submitted.
- Log in the new user if registration is successfull.
```py
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('main_app:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
```

#### The `register` Template
- Create a new file named: `register.html`
```html
{% extends "main_app/base.html" %}
{% block content %}
<form method="POST" action="{% url 'users:register' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">register</button>
    <input type="hidden" name="next" value="{% url 'main_app:index' %}" />
</form>
{% endblock content %}
```

#### Linking to the Registration Page
- Add link in `base.html` for the registration page for anyone who is not logged in.
```html
<a href="{% url 'users:register' %}">register</a> -
```
- **NOTE**: The registration system we've set up allows anyone to make any number of accounts for Learning Log.  But some systems require users to confirm their identity by sending a confirmation email the user must reply to.  By doing so, the system generates fewer spam accounts than the simple system we're using here.  However, when you're  learning to build apps, it's perfectly appropriate to practice with a simple user registration system like the one we're using.

## Allowing Users to Own Their Data
- Create a system to figure out which data belongs to which user.
- Restrict access to certain pages so users can work with only their own data.
### Restricting Access with `@login_required`
- Restrict access to certain pages to logged-in users through the `@login_required` decorator.
  - A *decorator*  is a directive placed just before a function definition that Python applies to the function before it runs to alter how the function code behaves.

#### Restricing Access to the Topics Page
- Each topic will be owned by a user.
- Only registered users should be able to request the topics page.
```py
from django.contrib.auth.decorators import login_required
@login_required
def topics(request):
```
- Import the `login_required()` function.
- Apply `login_required()` as a decorator to the `topics()` view function.
  - Prepend `login_required` with the `@` symbol so Python knows to run the code in `login_required()` before the code in `topics()`.
- The `login_required()` function checks to see if a user is logged in.
  - Django will only run the code in `topics()` only if the user is logged in.
  - If the user is not logged in then they will be directed to the login page.
- Modify `settings.py` so Django knows where to find the login page.
- Add the following at the very end of `settings.py`:
```py
# My settings
LOGIN_URL = '/users/login/'
```

#### Restricting Access Through Learning Log
- Django makes it easy to restrict access to pages.
- Restrict every page except the home page, registration page, and logout.
```py
@login_required
```

### Connecting Data to Certain Users
- Connect the data submitted to the user who submitted it.
- Only need to connect the data highest in the hierarchy to a user, and the lower-level data will follow.
- Modify the `Topic` Model by adding a foreign key relationship to a user.
- Migrate the database.
- Modify some of the views so they only show the data associated with the currently logged-in user.

#### Modifying the Topic Model
- Modify `models.py`
```py
from django.contrib.auth.models import User
owner = models.ForeignKey(User)
```

#### Identifying Existing Users
- When we migrate the database, Django will modify the database so it can store a connection between each topic and a user.
- Link all topics to an existing user.
- Find the ID of that user:
```shell
manage.py shell
```
```py
from django.contrib.auth.models import User
User.objects.all()
for user in User.objects.all():
    print(user.username, user.id)
```

#### Migrating the Database
- With the user ID's we can migrate the database.
```shell
python manage.py makemigrations main_app
```
- Select option 1, then type in 1 in the interactive python prompt.
```shell
python manage.py migrate
```
- Verify that the migration worked as exprected in the shell session.
```shell
from main_app.models import Topic
for topic in Topic.objects.all():
    print(topic, topic.owner)
```
- **NOTE**: You can simply reset the database instead of migrating, but that will lsoe all existing data.  It's good practice to learn how to migrate a database while maintaining the integrity of user' data.  If you do want to start with a fresh database, issue the command `python manage.py flush` to rebuild the database structure. You'll have to create a new superuser, and all of your data will be gone.

### Restricting Topics Access to Appropriate Users
- Currently all logged in users can see all the topics.
- We will change that by showing users only the topics that belong to them.
- Make the following change to the `topics()` function in `views.py`.
```py
topics = Topic.objects.filter(owner=request.user).order_by('date_added')
```
- When a user is logged in, the request object has a `request.user` attribute set that stores information about the user.
- The code fragment `Topic.objects.filter(owner=request.user)` tells Django to retrieve only the `Topic` objects from the database whose `owner` attribute matches the current user.

### Protecting a User's Topics
- Perform a check before retrieving the requested entries in the `topic()` view function:
```py
from django.http import HttpResponseRedirect, Http404

# Make sure the topic belongs to the current user.
if topic.owner != request.user:
    raise Http404
```

### Protecting the `edit_entry` Page
- Protect the `edit_entry` pages.
```python
# Make sure the topic belongs to the current user.
if topic.owner != request.user:
    raise Http404
```

### Associating New Topics with the Current User
- Currently our page for adding new topics is broken.
- Django cannot create a new topic without specifying a value for the topic's `owner` field.
```py views.py
new_topic = form.save(commit=False)
new_topic.owner = request.user
new_topic.save()
```

