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
    <h3>Wrong Username or Password</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br><br>
    <button type = "button" onclick = "window.location.href='signInUpPage.py'">Back</button>



"""

htmlTemp = """
    <h3>Hello</h3>
    <p>Login successful</p>
"""

htmlNewPosition = """
    <h2>Post your Job</h2>
        <div class="container" id="container">
            <div class="form-container post-container">
                <form action="post.py" method="post">
                    <h1>Create a Job Position</h1>
                    <input type="text" placeholder="Position Name"  name="position"/>
                    <input type="text" placeholder="Description" name="description"/>
                    <input type="text" placeholder="Expectation" name="expectation"/>
                    <input type="text" placeholder="Deadline" name="deadline"/>
                    <button type = "submit" id="post">Post</button><br> <br>
                    <button type = "button" onclick = "window.location.href='index.py'">Log Out</button>
                </form>
            </div>
        </div>
"""

htmlPositionTabHeader = """
    <br><br><table>
            <tr>
              <th>Position Name</th>
              <th>Description</th>
              <th>Expectations</th>
              <th>Deadline</th>
            </tr>

"""

htmlrow = """
        <tr> 
                <td>{i[0]}</td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
                <td>{i[3]}</td>
        </tr>
"""

htmlTableEnd = """
</table>
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
    print(htmlTemp)
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        cUser = cookie["username"].value
        print(htmlNewPosition)
        print("<p>Username= {cUser}</p>".format(**locals()))
        print(htmlend)

    else:
        print("<p>Login Required!</p>")
        print(htmlend)


else:
    print(htmlHeader)
    print(htmlWrong)

