#! C:\Program Files (x86)\Python38-32\python
from Database import Database as db
import cgi


htmlRedirectIndex = """
<html>
    <head>
    <title>Confirm</title>
    <link rel="stylesheet" href="common.css">
    </head>

    <body>
    <h3>Successfully Registered</h3>
    <button type = "button" onclick = "window.location.href='signInUpPage.py'" >Home Page </button>
    </body>
</html>

"""
htmlRedirectIndexWithError = """
<html>
    <head>
    <title>Confirm</title>
    <link rel="stylesheet" href="common.css">
    </head>

    <body>
    <h2>Register Error</h2>
    <h3>Please Check Your Value</h3>
    <button type = "button" onclick = "window.location.href='signInUpPage.py'" >Back</button>
    </body>
</html>

"""

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



if db.registerationForCompany(liste):
    print(htmlRedirectIndex)
else:
    print(htmlRedirectIndexWithError)






