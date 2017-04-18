# Django Nots
- Install Django Mac
```
python3 pip install virtualenv
python3 -m venv ~/Developer/venv
ve
pip install Django
django-admin startproject Treasuregram
python manage.py runserver
python manage.py startapp main_app
```
- Install Django PC
```

```
## Creating An Index View
- A view is simply a Python function that takes in a web request and returns a web response
- Modify the view.py
    - `from django.http import HttpResponse`
    - `def index(request): return HttpResponse('<h1>Hello Explorers!</h1>')`

## The URLs Dispatcher
- We want the `server/index` url to go to our *index view*.
- Path goes - `localhost::8000/index/` --> `Treasuregram/url.py` --> `main_app.views.index`

## Creating the New URL in the URL Dispatcher
- The project's URL dispatcher is in `urls.py` and will send the URL to the matching view.

## URL Dispatcher
### Best Practices
