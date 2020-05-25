#! C:\Program Files (x86)\Python38-32\python
import random
import cgi
import sys
import http.cookies as Cookie
from Database import Database as db
import os

internshipliste = []
htmlWrong = """
<html>
        <head>
            <title>Post Error</title>  
            <link rel="stylesheet" href="common.css">
        </head>
    <body>
         <h2>Post Error</h2>
         <button type = "button" onclick = "window.location.href='signInUpPage.py'" >Return Sign In Page</button>
    </body>
</html>
"""
htmlPost = """
      <html>
       <head>
           <title>Internship</title>  
           <link rel="stylesheet" href="login.css">
       </head>
       <body>
       <h3>Successfully Posted</h3>
       <button type = "button" <a onclick = "window.location.href='login.py?{internshipliste[4]}'">Back</a></button>
       </body>
   </html>
   """
htmlUser = """
      <html>
       <head>
           <title>Internship</title>  
           <link rel="stylesheet" href="login.css">
       </head>
       <body>
       <h3>Successfully Posted</h3>
       <p>Username= {cUser}</p>
       <button type = "button" <a onclick = "window.location.href='login.py'">Back</a></button>
       </body>
   </html>
"""
if "HTTP_COOKIE" in os.environ:
    cookies = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    if "session" in cookies.keys():
        cUser = cookies["username"].value
        print(htmlPost.format(**locals()))

form = cgi.FieldStorage()

internshipliste.append(form.getvalue("position"))
internshipliste.append(form.getvalue('description'))
internshipliste.append(form.getvalue('expectation'))
internshipliste.append(form.getvalue('deadline'))
internshipliste.append("apple")

returnval = db.internshipAdd(internshipliste)
if returnval == "NullValue":
    print(htmlWrong)
#else:
    #print(htmlPost)
