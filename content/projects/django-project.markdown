title: Django site mockup: philo-b.xyz
slug: projects-django-mockup
category: projects
date: 2019-02-14
modified: 2019-02-14
Sortorder: 001


Even though **[this site][1]** is just a mockup, it is fully functioning. Feel free to login and try out the commenting system for example.

The project combines a lot of different types of technologies, many of which were new to me before I started this solo project. It was not always easy to get the different aspects of this full-stack project to work together. 

Examples of situations that started out with total cluelessness: 

* setting up Nginx to serve static files,
* discovering necessary but deleted settings in docker-compose files,
* preventing containers to run in root, and with PostgreSQL databases secured,
* finding out gcc was needed to build binaries during image creations,
* not undertanding why automated e-mails are not sent during sign-up (answer: gmail can block automated logins)
.

<br>
The specs are:

* Python-Django framework,
* Dockerized (docker-compose),
* Postgresql database,
* Nginx reverse proxy,
* WSGI server (Gunicorn),
* Sentry (Raven-Python),
* SSL (Let's Encrypt),
* Javascript,
* Ajax calls (for forum interaction),
* HTML templating,
* CSS,
* Bash scripting,
* Hosted on Digital Ocean,
* Created in Linux (Mint)
.

<br>
To visit the site click **[here][1]**.
The repository can be found **[here](https://github.com/DZet/philo-b.xyz)**.

[1]: http://druqtemaker.com/philo-b/
