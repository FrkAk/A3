#! C:\Program Files (x86)\Python38-32\python
import random
import cgi ,sys
import http.cookies as Cookie
from Database import Database as db




def post():
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
           <button type = "button" <a onclick = "window.location.href='login.py?{internshipliste[4]}'"</a>>Back</button>
           </body>
       </html>
       """
    form = cgi.FieldStorage()
    internshipliste = []
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









form = cgi.FieldStorage()
name = form.getvalue("username")
pwd = form.getvalue('companypassword')

liste = []
liste.append(name)
liste.append(pwd)

htmlHeader = """
<html>
    <head>
        <title>Internship</title>  
        <link rel="stylesheet" href="login.css">
    </head>
    <body>
"""

htmlWrong = """
    <h3>Wrong Username or Password</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br><br>
    <button type = "button" onclick = "window.location.href='signInUpPage.py'" >Back</button>
    
"""

htmlNewPosition = """
    <h2>Post your Job</h2>
        <div class="container" id="container">
            <div class="form-container post-container">
                <form method="post">
                    <h1>Create a Job Position</h1>
                    <input type="text" placeholder="Position Name"  name="position"/>
                    <input type="text" placeholder="Description" name="description"/>
                    <input type="text" placeholder="Expectation" name="expectation"/>
                    <input type="text" placeholder="Deadline" name="deadline"/>
                    <input type="text" placeholder="Validate your Username" name="username"/>
                    <button type = "submit" id="post">Post</button><br> <br>
                    <button type = "button" onclick = "window.location.href='index.py'" >Log Out</button>
                </form>
            </div>
        </div>
"""
htmlPostionTablHeader = """
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
if len(sys.argv) == 1:
    user = db.authenticationForCompany(liste)
else:
    user= sys.argv[1]
#user = "apple"
print(htmlHeader)

if user is not None:
    print(htmlNewPosition)
    print(htmlPostionTablHeader)
    positions = db.getinternshippositionsforacompany(user)
    for i in positions:
        print(htmlrow.format(**locals()))
    print(htmlTableEnd)
    print(htmlend)
    post()


else:
    print(htmlWrong)
    print(htmlend)





def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("".format(title))


def printFooter():
    print("</body></html>")


def printBody():
    print("""
		<h2>Post your Job after Sign in/up Form</h2>
		""")


def temp():
    printHeader("Login")

    cookie = Cookie.SimpleCookie()
    cookie["session"] = random.randint(1, 1000000000)
    cookie["session"]["domain"] = "localhost"
    cookie["session"]["path"] = "/"
    session_cookie = cookie.output().replace("Set-Cookie: ", "")
    print("<script>")
    print("document.cookie = '%s';" % session_cookie)
    # print("window.location = 'deneme.py';")
    print("</script>")

    printBody()
    printFooter()
