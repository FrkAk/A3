#! C:\Program Files (x86)\Python38-32\python
import http.cookies as Cookie
from Database import Database as db
import random
import cgi
import os

if "HTTP_COOKIE" in os.environ:
    tempUser = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    tempUser.clear()
    print("""
    <html>
        <head>
        </head>
        <body>
        <a onclick = "window.location.href='index.py'">Logging Out</a>
        </body>
    </html>
    
    """)

