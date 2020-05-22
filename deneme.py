#! C:\Program Files (x86)\Python38-32\python

import os
import http.cookies as Cookie
import cgi
def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Login")

if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    print (" {} ".format(cookie["session"].value))
    if "session" in cookie.keys():
        print("<p>[Customized Text]</p>")

    else:
        print("<p>Login required</p>")

else:
    print("<p>Login required</p>")
printFooter()