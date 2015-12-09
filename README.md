# django-canned-responses

This is a simple Django project for testing HTTP requests by returning canned responses.

The purpose of `django-canned-responses` is to configure "canned" responses for various requests (API endpoints, HTML pages, etc.) to test things like how gracefully (or not) a mobile app handles different API errors.

This repository contains a very simple Django project with a single `canned_responses` app. When I say "simple Django project" I mean it - it's basically just the default settings (SQLite3!) plus the `canned_responses` app added to `INSTALLED_APPS`. In case it doesn't go without saying, this is meant to be run on a development machine only, NOT in a production environment!

## Setting Up & Running

Since this project is useful to many types of developers (who aren't necessarily familiar with Python/Django), I'm going to try to keep this section as straightforward as possible. Experienced Python/Django developers can probably skip down to the "Canned Responses Setup" section.

### Prerequisites: Python, pip, virtualenv

First off, you're going to need Python 2.7.x. If you're on Linux or Mac OS X, congratulations, you're probably all set. To check:

`python -V`

That should return something like 

`Python 2.7.5`

If you don't have Python, head to [The Python Software Foundation site](https://www.python.org/) and download and install the most handsome version of Python 2.7 you can find.

Next you're gonna need `pip`, the Python package manager. If you can't run `pip freeze` from the command line, you're gonna need to [install it](https://pip.pypa.io/en/stable/installing/).

Next up is `virtualenv`, which is a way to separate different versions of various Python packages for different uses/projects. After [installing virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html), create a new virtualenv called something like `canned` and activate it. [This page tells you how.](http://virtualenv.readthedocs.org/en/latest/userguide.html)

### Canned Responses Setup

Okay, so now you've got Python 2.7.x, `pip` and `virtualenv` installed and you've created and activated a virtual environment for this project, right? Don't make me come over there.

Okay, so now `cd` to your favorite development directory and clone this repository, like so:

`git clone https://github.com/whalerock/django-canned-responses.git`

Then you can install the required Python packages, initialize a database and create a superuser:

```
cd django-canned-responses
pip install -r requirements.txt
cd canned
python manage.py migrate
python manage.py createsuperuser
```

(enter desired username & password, etc.)  Now you can start the development server:

```
python manage.py runserver
```

This runs a web server on localhost (127.0.0.1) on port 8000. Note: that command can run the server using a different IP/port too, so something like `python manage.py runserver <your computer's IP address on NetworkX>:<the port>` would make the web server accessible to other devices on NetworkX (if the port is open). But for now, we'll keep it on localhost:8000.  Ctrl+C to stop it when you need to.

Okay, so now you've got the server up and running LIKE A BOSS. In a web browser, surf over to [http://localhost:8000/some-thing/](http://localhost:8000/some-thing/) - it should 404. Makes sense since you haven't created any canned responses yet.

## Creating Canned Responses

Now surf on over to [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in as the superuser you created earlier. Now go to [http://localhost:8000/admin/canned_responses/cannedresponse/](http://localhost:8000/admin/canned_responses/cannedresponse/) and create a new canned response instance with these values:
- `Name`: My test canned response
- `Active`: true (checked)
- `Request method`: GET
- `Request path`: /foo/bar/
- `Response status code`: 200
- `Response sleep time`: 0
- `Response content type`: HTML
- `Response payload`: `<html><h1>Woohoo! FooBar, baby!!</h1></html>`

Then save it.

Now when you surf on over to [http://localhost:8000/foo/bar/](http://localhost:8000/foo/bar/) - you should see the HTML you entered rendered in all its black-and-white glory.

That's pretty much all there is to it. Any request to this server other than those starting with `/admin/` will trigger a lookup for an active canned response with the path and method of the request being made. The canned response is simply returned with values from its instance. If not found, the view will 404.

## Shortcuts & Options

When a canned response instance is saved with `active=True`, all other canned responses with the same request method and request path get set to `active=False`, which makes it easy to switch among many different canned responses for the same method/path, to test different scenarios. `Response sleep time` is an optional time, in seconds, that the view handler will wait before returning a response. The default is zero (no added latency), but if you want you can set that to a nonzero value when you want to test an actual timeout on the client side.

### Last updated: December 9, 2015
