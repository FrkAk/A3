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
         <button type = "button" onclick = "window.location.href='loginCookie.py'" >Back</button>
    </body>
</html>
"""

htmlUser = """
      <html>
       <head>
           <title>Internship</title>  
           <link rel="stylesheet" href="common.css">
       </head>
       <body>
       <h2>Successfully Posted</h2>
       <h3>Position: {internshipliste[0]}</h3>
       <h3>Description: {internshipliste[1]}</h3>
       <h3>Expectation: {internshipliste[2]}</h3>
       <h3>Deadline: {internshipliste[3]}</h3>
       <h3>Username: {internshipliste[4]}</h3>
       <button type = "button" <a onclick = "window.location.href='loginCookie.py'">Back</a></button>
       </body>
   </html>
"""
cUser=""
if "HTTP_COOKIE" in os.environ:
    cookies = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = str(db.getSessionUsername(cookies["sessionID"].value))

else:
    print(htmlWrong)

form = cgi.FieldStorage()

internshipliste.append(form.getvalue("position"))
internshipliste.append(form.getvalue('description'))
internshipliste.append(form.getvalue('expectation'))
internshipliste.append(form.getvalue('deadline'))
internshipliste.append(cUser)

returnval = db.internshipAdd(internshipliste)
if returnval == "NullValue":
    print(htmlWrong)
else:
    print(htmlUser.format(**locals()))
