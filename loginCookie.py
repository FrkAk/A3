#! C:\Program Files (x86)\Python38-32\python
import http.cookies as Cookie
from Database import Database as db
import random
import cgi
import os


def cokieSetter(user):
    cookie = Cookie.SimpleCookie()
    cookie["session"] = random.randint(1, 1000000000)
    cookie["session"]["domain"] = "localhost/"
    cookie["session"]["path"] = "/"
    cookie["username"] = user
    print("Content-type: text/html")
    print("{}".format(cookie.output()))

def cookieReset():
    if "HTTP_COOKIE" in os.environ:
        tempUser = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        tempUser.clear()


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
    <button type = "button" onclick = "window.location.href='signInUpPage.py'">Back</button>



"""


htmlNewPosition = """
    <h2>Post your Job</h2>
            <div class="form-container table-wrapper">
                <form action="post.py" method="post">
                    <h2>Create a Job Position</h2>
                    <span>Fill the blanks</span>
                    <input type="text" placeholder="Position Name"  name="position"/>
                    <input type="text" placeholder="Description" name="description"/>
                    <input type="text" placeholder="Expectation" name="expectation"/>
                    <input type="date" placeholder="Deadline" name="deadline"/>
                    <button type = "submit" id="post">Post</button><br>
                    <button type = "button" onclick = "window.location.href='index.py'">Log Out</button>
                </form>
        </div>
"""

htmltable = """
        <br><br><div class="table-wrapper">
            <span class="counter pull-right"></span>
            <table class="fl-table table table-hover table-bordered results">
                <thead>
                <tr>
                    <th>{userN}</th>
                </tr>
                <tr>
                    <th>Position Name</th>
                    <th>Description</th>
                    <th>Expectations</th>
                    <th>Deadline</th>
                </tr>
                </thead>
                <tbody>
"""

htmlrow = """
            <tr> 
                <td>{i[0]}</td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
                <td>{i[3]}</td>
            </tr>
"""

htmlEmpty= """
                <tr> 
                    <th>There is no offer</th  >
                </tr>
"""
htmltableEnd= """
            </tbody>
        </table>
    </div>
"""


htmlend = """
        </body>
</html>
"""

form = cgi.FieldStorage()
name = form.getvalue("username")
pwd = form.getvalue('companypassword')
liste = [name, pwd]

user = db.authenticationForCompany(liste)

#user = "apple"

if user is not None:
    cokieSetter(user)
    print(htmlHeader)

    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        cUser = cookie["username"].value
        print(htmlNewPosition)
        userN = user.capitalize()
        print(htmltable.format(**locals()))
        position = db.getinternshippositionsforacompany(user)
        if len(position) == 0:
            print(htmlEmpty)
        else:
            for i in position:
                print(htmlrow.format(**locals()))
        print(htmltableEnd)
        print(htmlend)


    else:
        print("<p>Login Required!</p>")
        print(htmlend)


else:
    print(htmlHeader)
    print(htmlWrong)

