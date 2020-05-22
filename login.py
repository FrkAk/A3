#! C:\Users\Psikolojik\AppData\Local\Programs\Python\Python38-32\python.exe


#Testingggggg

import random
import cgi
import http.cookies as Cookie
from Database import Database as db
# tesssttt GİTTTT
def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))



def printFooter():
    print("</body></html>")

printHeader("Login")

form = cgi.FieldStorage()
name = form.getvalue("username")
pwd = form.getvalue('companypassword')

liste = []
liste.append(name)
liste.append(pwd)

if db.authenticationForCompany(liste):
    print("<p>Login successful</p>")
    cookie = Cookie.SimpleCookie()
    cookie["session"] = random.randint(1, 1000000000)
    cookie["session"]["domain"] = "localhost"
    cookie["session"]["path"] = "/"
    session_cookie = cookie.output().replace("Set-Cookie: ", "")
    print("<script>")
    print("document.cookie = '%s';" % session_cookie)
    print("window.location = 'deneme.py';")
    print("</script>")

else:
    print("<p> Wrong Username or Password</p>")


printFooter()
