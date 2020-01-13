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



## Running Locally

Make sure you have Python 3.7.3 [installed locally].
To push to Heroku, you'll need to install the [Heroku CLI] (https://devcenter.heroku.com/articles/heroku-cli).
Additionally you will need to install the [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/LukaszKulacz/lk-desktop.git
$ cd lk-desktop

$ python -m venv lk-venv
$ lk-venv\Scripts\activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local -f Procfile.windows 
$ or
$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

First time deploying.
```sh
$ git remote add heroku https://github.com/LukaszKulacz/lk-desktop.git
```

Deploy your application by just pushing it to 'public' branch.
```sh
$ git push heroku public
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:
- [Python on Heroku](https://devcenter.heroku.com/categories/python)

Application made based on article:
- [Heroku - Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python]
