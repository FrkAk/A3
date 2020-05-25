#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db

htmlHeader = """
<html>
    <head>
        <title>Northern Cyprus Internship Positions</title>
        <link rel="stylesheet" href="common.css">
        
    </head>
    <body>
        <h1>Welcome to Northern Cyprus Internship Website</h1>
        <div class="form-group pull-right">
            <input type="text" class="search form-control" placeholder="What you looking for?">
        </div>    
        <button type = "button" onclick = "window.location.href='signInUpPage.py'" > Sign In/Sign Up </button>
 """
htmltable = """
        <div class="table-wrapper">
            <span class="counter pull-right"></span>
            <table class="fl-table table table-hover table-bordered results">
                <thead>
                <tr>
                    <th>{cityname}</th>
                </tr>
                <tr>
                    <th>Software Company</th>
                    <th>Position Name</th>
                    <th>Description</th>
                    <th>Expectations</th>
                    <th>Deadline</th>
                </tr>
               <tr class="warning no-result">
                    <td colspan="4"><i class="fa fa-warning"></i>No active internship position found</td>
                </tr>
                </thead>
                <tbody>
"""

htmlrow = """
                <tr> 
                    <th scope="row"> <a onclick = "window.location.href='companydetails.py?{i[0]}'"> {i[0]} </a></th>
                    <td>{i[2]}</td>
                    <td>{i[3]}</td>
                    <td>{i[4]}</td>
                    <td>{i[5]}</td>
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
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js"></script>
        <script src="search.js"></script>
     </body>
</html>
"""


i = 0
positions = db.getinternshippositions()

gazi=[]
girne=[]
guzelyurt= []
iskele= []
lefke= []
lefkosa= []

for i in positions:
    if i[-1] == 1:
        gazi.append(i)
    elif i[-1] == 2:
        girne.append(i)
    elif i[-1] == 3:
        guzelyurt.append(i)
    elif i[-1] == 4:
        iskele.append(i)
    elif i[-1] == 5:
        lefke.append(i)
    elif i[-1] == 6:
        lefkosa.append(i)


print(htmlHeader)

cityname= "Gazimagusa"
print(htmltable.format(**locals()))
if len(gazi)==0:
    print(htmlEmpty)
else:
    for i in gazi:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Girne"
print(htmltable.format(**locals()))
if len(girne)==0:
    print(htmlEmpty)
else:
    for i in girne:
        print(htmlrow.format(**locals()))
print(htmltableEnd)


cityname= "Guzelyurt"
print(htmltable.format(**locals()))
if len(guzelyurt)==0:
    print(htmlEmpty)
else:
    for i in guzelyurt:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Iskele"
print(htmltable.format(**locals()))
if len(iskele)==0:
    print(htmlEmpty)
else:
    for i in iskele:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Lefke"
print(htmltable.format(**locals()))
if len(lefke)==0:
    print(htmlEmpty)
else:
    for i in lefke:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Lefkosa"
print(htmltable.format(**locals()))
if len(lefkosa)==0:
    print(htmlEmpty)
else:
    for i in lefkosa:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

print(htmlend)
