#! C:\Program Files (x86)\Python38-32\python
import cgi
import http.cookies as Cookie
from Database import Database as db
import os

htmlSignInUP = """
<html>
    <head>
        <title>Internship Sign In Page</title>
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
        <h2>Post your Job after Sign in</h2>
            <div class="form-container">
                <form  action="cookieCreator.py" method="post">
                    <h1>Sign in</h1>
                    <span>use your account</span>
                    <input type="text" placeholder="Username" name="username"/>
                    <input type="password" placeholder="Password" name="companypassword"/>
                    <button type = "submit" id="signInNow" >Sign In</button>
                </form>
            </div>
   <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    <script src="login.js"></script>
    </body>
</html>
"""


print(htmlSignInUP)
if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = db.getSessionUsername(cookie["sessionID"].value)
    db.updateLogStatus(cookie["sessionID"].value,-1)
