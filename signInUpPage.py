#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db

htmlSignInUP = """
<html>
	<head>
		<title>Intership Job</title>
		<link rel="stylesheet" href="login.css">
	</head>
	<body>
		<h2>Post your Job after Sign in/up Form</h2>
		<div class="container" id="container">
			<div class="form-container sign-up-container">
				<form action="register.py" method="post">
					<h1>Create Account</h1>
					<span>with your email for registration</span>
					<input type="text" placeholder="Company Name"  name="companyname"/>
					<input type="text" placeholder="Username" name="username"/>
					<input type="tel" placeholder="Phone Number" id="phone" name="telephone">
					<input type="text" placeholder="City" name="city"/>
					<input type="text" placeholder="Postal Address" name="address"/>
					<input type="text" placeholder="Website" name="website"/>
					<input type="email" placeholder="Email"  name="emailaddress"/>
					<input type="password" placeholder="Password" name="companypassword"/>
					<button type = "submit" id="signUpNow">Sign Up</button>
				</form>
			</div>
		    <div class="form-container sign-in-container">
			<form  action="login.py" method="post">
				<h1>Sign in</h1>
				<span>or use your account</span>
				<input type="text" placeholder="Username" name="username"/>
				<input type="password" placeholder="Password" name="companypassword"/>
				<button type = "submit" id="signInNow" >Sign In</button>
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
	</body>
</html>
"""


print(htmlSignInUP)
