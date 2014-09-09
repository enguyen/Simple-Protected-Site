#!/usr/bin/env python

from google.appengine.api import users

import os
import mimetypes
import webapp2

class ProxiedStaticHandler(webapp2.RequestHandler):
  def get(self):
    # Check if we have a valid user.
    user = users.get_current_user()
    if not (user and user.email().endswith("@yourdomain.com")):
      self.response.status = 302
      self.response.write('Not authorized.')
      return

    # If we have a valid user, read the file (if valid path) and serve it.
    try:
      file = open(os.path.dirname(__file__) + self.request.path)
      type = mimetypes.guess_type(self.request.path)[0]
      self.response.headers.add_header("Content-type", type)
      self.response.write(file.read())
    except:
      self.response.status = 404
      self.response.write('404 Not Found.')

app = webapp2.WSGIApplication([
    ('/.*', ProxiedStaticHandler)
], debug=True)
