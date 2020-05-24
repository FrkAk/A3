#! C:\Program Files (x86)\Python38-32\python
import random
import cgi
import sys
import http.cookies as Cookie
from Database import Database as db



internshipliste = []
htmlWrong = """
<html>
        <head>
            <title>Post Error</title>  
            <link rel="stylesheet" href="login.css">
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
       <h3>Succesfully Posted</h3>
       <button type = "button" <a onclick = "window.location.href='login.py?{internshipliste[4]}'">Back</a></button>
       </body>
   </html>
   """

form = cgi.FieldStorage()


internshipliste.append(form.getvalue("position"))
internshipliste.append(form.getvalue('description'))
internshipliste.append(form.getvalue('expectation'))
internshipliste.append(form.getvalue('deadline'))
internshipliste.append(form.getvalue('username'))


returnval = db.internshipAdd(internshipliste)
if returnval == "NullValue":
    print(htmlWrong)
else:
    print(htmlPost)
