#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db

htmlheader = """
<!DOCTYPE html>
<html>
    <head>
        <title>Company Register</title>
        <style>
        html{  
            text-align: center;
            font-size: 25px; 
        }
        button{
            font-size : 20px;
            background-color:cornflowerblue;
        }
        </style>
    </head>

    <body>
        <h1>Please fill all the areas</h1>
        <form  method = "post">
            Enter Username: <input type="text" name="username"> <br/>
            Create Password: <input type="password" name="companypassword"> <br/>
            Company Name: <input type="text" name="companyname"> <br/>
            Email Address: <input type="email" name="emailaddress"> <br/>
            Telephone No: <input type="tel" name="telephone"> <br/>
            Website Name: <input type="text" name="website"> <br/>
            City Name: <input type="text" name="city"> <br/>
            Postal Address: <input type="text" name="postaladdress"> <br/>
            <button type = "button" onclick = "window.location.href='index.py'" > Back </button>
            <button type = "reset" > Clear </button>
            <button type = "submit" onclick="submit()"> Register </button>

        </form>
        
"""

print(htmlheader)
def submit():

    liste = []

    form = cgi.FieldStorage()

    liste.append(form.getvalue("username"))
    liste.append(form.getvalue('companypassword'))
    liste.append(form.getvalue('companyname'))
    liste.append(form.getvalue('emailaddress'))
    liste.append(form.getvalue('telephone'))
    liste.append(form.getvalue('website'))
    liste.append(form.getvalue('city'))
    liste.append(form.getvalue('postaladdress'))
    liste.append(12340)  # Gözden Geçirilecek

    returnval = db.registerationForCompany(liste)

    htmlbody = """
        <p>{liste},{returnval}</p>
            </body>
    </html>
    """

    print(htmlbody.format(**locals()))

