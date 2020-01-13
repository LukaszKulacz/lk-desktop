# LK-Desktop

A barebones Desktop app, which can easily be deployed to Heroku.
It uses Django framework.

## Creating Guide

To create own instance of Heroku app:
- login on Heroku site [link](https://id.heroku.com/login)
- go to dashboard [link](https://dashboard.heroku.com/apps)
- create new app named **app-name**
- login on GitHub site [link](https://github.com/)
- create new repository named **app-name**
- go to 'Deploy' tab and select 'Deployment method as GitHub'
- in 'Connect to GitHub' section type **app-name** and click search
- select connect near correct repository
- clone repository [LK-Desktop](https://github.com/LukaszKulacz/lk-desktop.git)
```sh
$ git clone https://github.com/LukaszKulacz/lk-desktop.git
```
- remove git remote origin and add own git remote
```sh
$ git remote rm origin
$ git remote add heroku **own-repository-link**
```
- (optionally) change all **lk-dekstop** to own **app-name**
```sh
app.json
lk-dekstop/settings.py
lk-dekstop/wsgi.py
lk-dekstop
manage.py
Procfile
```

- push files to own repository
```sh
$ git push heroku master
```
- go back to Heroku app deployment tab
- enable automatic deploys on some branch or manually deploy app

## Running Locally

To run project locally go to your app path.

Do this steps for first time only:
```sh
$ python -m venv lk-venv
$ lk-venv\Scripts\activate (work in CMD, not in PowerShell)
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic
```

Remember to create superuser account!
Locally:
```sh
$ python manage.py createsuperuser
```
On Heroku server (Heroku CLI required):
```sh
$ heroku run python manage.py createsuperuser
```
It is possible that you will need to specify app name
```sh
$ heroku run -a '**app-name**' python manage.py createsuperuser
```
**Finally, run server locally:**
```sh
$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

In the next console you can test your app by (you need Firefox installed):
```sh
$ python funcional_tests.py
```

## Deploying to Heroku

Deploy your application by just pushing it to 'public' branch.
```sh
$ git push heroku master
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:
- [Python on Heroku](https://devcenter.heroku.com/categories/python)

Application made based on article:
- [Heroku - Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python]
