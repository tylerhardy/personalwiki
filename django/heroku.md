# Heroku
## Pushing to Heroku
```shell
heroku login
heroku create
git push keroku master
```

```shell
heroku ps
heroku open
```

```shell Helps
git remote -v
git remote rm heroku
```

## Setting Up the Database on Heroku
```shell
heroku run python manage.py migrate
```

## Refining the Heroku Deployment
- Change the setting DEBUG to False

### Create a Superuser on Heroku
```shell
heroku run bash
ls
python manage.py createsuperuser
ll_admin
exit
```

### Creating a User-Friendly URL on Heroku
```shell
heroku apps:rename learninglogging
```

### Securing the Live Project
```py
# Allow only Heroku to host the project
ALLOWED_HOSTS = ['learninglogging.herokuapp.com']

DEBUG = False
```

### Creating Custom Error Pages
#### Making Custom Templates
```py settings.py
        'DIRS': [os.path.join(BASE_DIR, 'main_app/templates')],
```

#### Viewing the Error Pages Locally
```py settings.py
DEBUG = False

ALLOWD_HOSTS = ['localhost']
```

### Deleting Heroku App
```shell
heroku apps:destroy --app learninglogging
```