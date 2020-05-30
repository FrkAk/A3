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
            <input type="text" id="myInput" onkeyup="searchFromTables()" placeholder="What you looking for...">
        </div>    
        <button type = "button" onclick = "window.location.href='signInUpPage.py'" > Sign In/Sign Up </button>
 """
htmltable = """
        <div class = "table-wrapper">
            <table id="{tableID}" class= "myTable" >
            <tbody>
                <tr class="myTableHeader">
                    <th>{cityname}</th>
                </tr>
                <tr class="myTableHeader">
                    <th>Software Company</th>
                    <th>Position Name</th>
                    <th>Description</th>
                    <th>Expectations</th>
                    <th>Deadline</th>
                </tr>

"""

htmlrow = """
                <tr> 
                    <td class="myTableHeader"> <a onclick = "window.location.href='companydetails.py?{i[0]}'"> {i[0]} </a></td>
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
        <script src="search.js"></script>
     </body>
</html>
"""

if not db.checkDatabesExistance():
    db.databaseInitiation()

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
tableID= "table" + str(1)
print(htmltable.format(**locals()))
if len(gazi)==0:
    print(htmlEmpty)
else:
    for i in gazi:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Girne"
tableID= "table" + str(2)
print(htmltable.format(**locals()))
if len(girne)==0:
    print(htmlEmpty)
else:
    for i in girne:
        print(htmlrow.format(**locals()))
print(htmltableEnd)


cityname= "Guzelyurt"
tableID= "table" + str(3)
print(htmltable.format(**locals()))
if len(guzelyurt)==0:
    print(htmlEmpty)
else:
    for i in guzelyurt:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Iskele"
tableID= "table" + str(4)
print(htmltable.format(**locals()))
if len(iskele)==0:
    print(htmlEmpty)
else:
    for i in iskele:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Lefke"
tableID= "table" + str(5)
print(htmltable.format(**locals()))
if len(lefke)==0:
    print(htmlEmpty)
else:
    for i in lefke:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

cityname= "Lefkosa"
tableID= "table" + str(6)
print(htmltable.format(**locals()))
if len(lefkosa)==0:
    print(htmlEmpty)
else:
    for i in lefkosa:
        print(htmlrow.format(**locals()))
print(htmltableEnd)

print(htmlend)
