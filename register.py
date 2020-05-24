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

# companies = ['google', 'google123', 'GOOGLE', 'google@gmail.com', '0123456', 'google.com' ,'Girne','USA', '2131']
# print(type(companies))
returnval = db.registerationForCompany(liste)

htmlheader = """
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
        <form action="" method="post">
            Enter Username: <input type="text" name="username"> <br/>
            Create Password: <input type="password" name="companypassword"> <br/>
            Company Name: <input type="text" name="companyname"> <br/>
            Email Address: <input type="email" name="emailaddress"> <br/>
            Telephone No: <input type="tel" name="telephone"> <br/>
            Website Name: <input type="text" name="website"> <br/>
            City Name: <input type="text" name="city"> <br/>
            Address: <input type="text" name="address"> <br/>
            <button type = "button" onclick = "window.location.href='index.py'" > Back </button>
            <button type = "reset"> Clear </button>
            <button type = "submit" id=signUp> Register </button>

        </form>
        </body>
</html>

"""

htmlRedirectIndex = """
<html>
    <head>
    <title>Confirm</title>
    </head>

    <body>
    <h3>Succesfully Registered</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button>
    </body>
</html>

"""

print(htmlRedirectIndex)

#print(htmlheader)
