#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db


liste = []
form = cgi.FieldStorage()

liste.append(form.getvalue("username"))
liste.append(form.getvalue('companypassword'))
liste.append(form.getvalue('companyname'))
liste.append(form.getvalue('emailaddress'))
liste.append(form.getvalue('telephone'))
liste.append(form.getvalue('website'))
liste.append(form.getvalue('city'))
liste.append(form.getvalue('address'))
liste.append(0)  # Gözden Geçirilecek


returnval = db.registerationForCompany(liste)


htmlRedirectIndex = """
<html>
    <head>
    <title>Confirm</title>
    <link rel="stylesheet" href="common.css">
    </head>

    <body>
    <h3>Successfully Registered</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button>
    </body>
</html>

"""

print(htmlRedirectIndex)


