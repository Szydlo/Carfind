# CarFind

**Carfind** is a small project, made mainly to learn django and tailwindcss. It's similar to websites like craiglist or ebay, but only for cars. 

## Features:

- Creating account
- Dashboard for account, with adding offers, editing, deleting them.
- List of offers, with searchbar
- Offer preview, which shows all important information about car.

Currently carfind lacks responsive design for smartphones.

# Getting started

1. Clone project with: `https://github.com/Szydlo/Carfind.git`
2. Install django `pip install django` and install django-browser-reload for easier development `pip install django-browser-reload`
2. Install tailwind via npm in jstools folder (with you want to edit css)
3. Make migrations with `py .\manage.py makemigrations` (run command in main folder where manage.py is located), `py .\manage.py sqlmigrate carfind_core 0001` (if you wish to use sqllite), and then `py .\manage.py migrate`
4. If you want to edit css, run tailwindcss run command, with: `tailwind-watch": "tailwindcss -i ../input.css -o ../static/css/output.css --watch`
5. Then `py .\manage.py runserver` to run a server

If you want to configure a project for your needs, look up django documentation

# TO-DO

- Remake templates for smartphones
- Code refactor, to use django forms and views
- Writing tests
- A system for managing, reviewing, and accepting offers
- Better image support for user

# Showcase of Carfind

[![IMAGE ALT TEXT](http://img.youtube.com/vi/GaIjIgWziy0/0.jpg)](https://www.youtube.com/watch?v=GaIjIgWziy0 "carfind")