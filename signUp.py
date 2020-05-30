#! C:\Program Files (x86)\Python38-32\python
import cgi
import http.cookies as Cookie
from Database import Database as db
import os

htmlSignUP = """
<html>
    <head>
        <title>Internship Sign Up Page</title>
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
        <h2>Post your Job after Sign Up Form</h2>
        <div class="form-container">
                <form action="register.py" method="post">
                    <h1>Create Account</h1>
                    <span>with your email for registration</span>
                    <input type="text" placeholder="Company Name"  name="companyname"/>
                    <input type="text" placeholder="Username" name="username"/>
                    <input type="text" placeholder="Website" name="website"/>
                    <input type="email" placeholder="Email"  name="emailaddress"/>
                    <input type="tel" placeholder="Telephone"  name="telephone"/>
                    <input type="password" placeholder="Password" name="companypassword"/>         
                    <input type="text" placeholder="Postal Address" name="address"/>
                    <select name="city" id="city">
                            <option value="Gazimagusa">Gazimagusa</option>
                            <option value="Girne">Girne</option>
                            <option value="Guzelyurt">Guzelyurt</option>
                            <option value="Iskele">Iskele</option>
                            <option value="Lefke">Lefke</option>
                            <option value="Lefkosa">Lefkosa</option>
                    </select><br>
                    <button type = "submit" id="signUpNow">Sign Up</button>
                </form>
            </div>
   <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    <script src="login.js"></script>
    </body>
</html>
"""


print(htmlSignUP)
if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = db.getSessionUsername(cookie["sessionID"].value)
    db.updateLogStatus(cookie["sessionID"].value,-1)
