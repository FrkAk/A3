#! C:\Users\Psikolojik\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi

def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Company Register")
form = cgi.FieldStorage()

name = form.getvalue("username")
pwd = form.getvalue('companypassword')
companyname = form.getvalue('companyname')
email = form.getvalue('emailaddress')
telephoneno = form.getvalue('telephone')
website = form.getvalue('website')
cityname = form.getvalue('city')
postal = form.getvalue('postaladdress')

print("<p>Input name: %s </p>" % name)
print("<p>Input name: %s </p>" % pwd)
print("<p>Input name: %s </p>" % companyname)
print("<p>Input name: %s </p>" % email)
print("<p>Input name: %s </p>" % telephoneno)
print("<p>Input name: %s </p>" % website)
print("<p>Input name: %s </p>" % cityname)
print("<p>Input name: %s </p>" % postal)



printFooter()