# django-canned-responses
Simple Django project for testing HTTP requests by returning canned responses.

The purpose of `django-canned-responses` is to configure "canned" responses for various requests (API endpoints, HTML pages, etc.) to test things, like how gracefully (or not) a mobile app handles different API errors.

This repository contains a very simple Django project with a single `canned_responses` app. When I say "simple Django project" I mean it - it's basically just the default settings (SQLite3!) plus the `canned_responses` app added to `INSTALLED_APPS`. In case it doesn't go without saying, this is meant to be run on a development machine only, NOT in a production environment!

## Setting Up & Running

- A virtualenv is highly recommended. Create one and activate it.
- Clone this repository.
- Then:

```
cd django-canned-responses
pip install -r requirements.txt
cd canned
python manage.py migrate
python manage.py createsuperuser
```
(enter desired username & password, etc.)  Finally:
```
python manage.py runserver
```
Now you've got the server up and running LIKE A BOSS. Make some GET requests in a browser for things like http://localhost:8000/foo/bar/ and http://localhost:8000/some.thing/ - they should 404. Makes sense since you haven't created any canned responses yet.

## Creating Canned Responses

Now surf on over to http://localhost:8000/admin/ and log in as your superuser. Now go to http://localhost:8000/admin/canned_responses/cannedresponse/ and create a new canned response instance with these values:
- `Name`: My test canned response
- `Active`: true (checked)
- `Request method`: GET
- `Request path`: /foo/bar/
- `Response status code`: 200
- `Response sleep time`: 0
- `Response content type`: HTML
- `Response payload`: <html><h1>Woohoo! FooBar, baby!!</h1></html>

(and save it)

Now surf on over to http://localhost:8000/foo/bar/ - you should see the HTML you entered rendered in all its black-and-white glory.

That's pretty much all there is to it. Any request to this server other than those starting with `/admin/` will trigger a lookup for an active canned response with the path and method of the request being made. The canned response is simply returned with values from its instance. If not found, the view will 404.

## Shortcuts & Options

When a canned response instance is saved with `active=True`, all other canned responses with the same request method and request path get set to `active=False`, which makes it easy to switch among many different canned responses for the same method/path, to test different scenarios. `Response sleep time` is an optional time, in seconds, that the view handler will wait before returning a response. The default is zero (no added latency). It's handy to set that to a nonzero value when you want to test an actual timeout on the client side.

### Last updated: December 8, 2015
