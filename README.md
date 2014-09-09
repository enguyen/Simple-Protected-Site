What
----

Here's a simple, Python, Google-App-Engine-based shell for serving your content from App Engine in a way that protects requests for _all_ files (including "static" ones) with some sort of authentication. There are lots of alternatives to this (e.g. .htaccess), but this takes advantage of GAE's authentication APIs. As configured here, it's best for restricting access to users with emails in a given domain.

Out of the box, this will serve static content easily. Just add your own handlers if you start doing something more.

How
----
For the default setup (restricting users to members of a given domain):  

1. Get the source, put it somewhere (e.g. `~/my-prototypes/`).
1. Edit ""@yourdomain.com" to your domain in `main.py`.
1. [Get App Engine tools](https://developers.google.com/appengine/) if you don't have them yet.
1. Add the files you want to serve to a subdirectory (e.g. `~/my-prototypes/app1/`).
1. Create a project on App Engine (e.g. "my-prototypes").
1. Edit "your-app" to your project name in `app.yaml`.
1. Push your files up, and serve! (in this example: http://my-prototypes.appspot.com/app1/index.html or something).

If you want to simply whitelist a set of email addresses, you'll have to modify the ProxiedStaticHandler to check it.

This script simply checks email address strings. You can also have your App Engine app [Restrict your auth to members of your domain](https://developers.google.com/appengine/articles/auth). If you do this, you'll need to also [add that project]( https://developers.google.com/appengine/articles/auth#AppspotDomainAuth) to your Google Apps Domain.
