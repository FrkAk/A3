#! C:\Program Files (x86)\Python38-32\python
import http.cookies as Cookie
from Database import Database as db
import random
import cgi
import string




def randomID():
    string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choiceStr = ""
    for i in range(3):
        choiceStr = choiceStr + random.choice(string.ascii_letters)
    number = random.randint(1000000, 9999999)
    ID = str(number) + choiceStr
    return ID


htmlHeader = """
<html>
    <head>
        <title>Internship</title>  
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
"""




htmlWrong = """
    <h3 style="align: center">Wrong Username or Password</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='signIn.py'">Back</button>
"""

htmlSucces = """
    <script type="text/javascript">
        window.location = "http://localhost/northcyprusswinterns/loginCookie.py";
    </script>
"""





form = cgi.FieldStorage()
name = form.getvalue("username")
pwd = form.getvalue('companypassword')
liste = [name, pwd]

user = db.authenticationForCompany(liste)
sessionID = randomID()
if user is not None:

    cookie = Cookie.SimpleCookie()
    cookie["session"] = sessionID
    cookie["session"]["domain"] = "localhost/"
    cookie["session"]["path"] = "/"
    cookie["sessionID"] = sessionID
    print("Content-type: text/html")
    print("{}".format(cookie.output()))
    print(htmlHeader)
    print(htmlSucces)
    db.addLog(sessionID,user)

else:
    print(htmlHeader)
    print(htmlWrong)
print("</body></html>")

