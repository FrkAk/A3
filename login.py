#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db


#Testingggggg


import random
import cgi
import http.cookies as Cookie
from Database import Database as db
# tesssttt GİTTTT
def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title><link rel=\"stylesheet\" href=\"login.css\"></head><body>".format(title))



def printFooter():
    print("</body></html>")

def printBody():
     print("""
		<h2>Post your Job after Sign in/up Form</h2>
		<div class="container" id="container">
			<div class="form-container sign-up-container">
				<form>
					<h1>Create Account</h1>
					<span>with your email for registration</span>
					<input type="text" placeholder="Company Name" />
					<input type="text" placeholder="Username" />
					<input type="tel" placeholder="Phone XXX-XXX-XX-XX" id="phone" name="Phone" 
					 		pattern="[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}">
					<input type="text" placeholder="City" />
					<input type="text" placeholder="Website" />
					<input type="email" placeholder="Email" />
					<input type="password" placeholder="Password" />
					<button id="signUpNow" onclick="runPythonforAuthentication()">Sign Up</button>
				</form>
			</div>
		<div class="form-container sign-in-container">
			<form>
				<h1>Sign in</h1>
				<span>or use your account</span>
				<input type="email" placeholder="Email" />
				<input type="password" placeholder="Password" />
				<a href="login.py">Forgot your password?</a>
				<button id="signInNow" >Sign In</button>
			</form>
		</div>
		<div class="overlay-container">
			<div class="overlay">
				<div class="overlay-panel overlay-left">
					<h1>Welcome Back!</h1>
					<p>To keep connected with us please login with your company info</p>
					<button class="ghost" id="signIn">Sign In</button>
				</div>
				<div class="overlay-panel overlay-right">
					<h1>Hello!</h1>
					<p>Enter your Company details and Post your Job</p>
					<button class="ghost" id="signUp">Sign Up</button>
				</div>
			</div>
		</div>
	</div>
	<script src="login.js"></script>
    """)
   


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
    #print("window.location = 'deneme.py';")
    print("</script>")

else:
    print("<p> Wrong Username or Password</p>")

printBody()
printFooter()
