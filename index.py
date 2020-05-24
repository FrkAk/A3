#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db


htmltable ="""
<html>
    <head>
        <title>Northern Cyprus Internship Positions</title>
        <style>
        html{
            text-align: center;  
            font-size: 25px; 
        }
        button{
            font-size : 20px;
            background-color:cornflowerblue;
        }
        table, th, td {
            border: 1px solid black;
            background-color:darkgray;
        }
        </style>
    </head>
    <body>
        <h1>Welcome to Northern Cyprus Internship Website</h1>
        <p>Please Select what you want to do</p>
       
        <button type = "button" onclick = "window.location.href='register.py'" > Register </button>

        <button type = "button" onclick = "window.location.href='login.html'"> Login </button> <br/> <br/>
<table style="width:50%; margin-left:auto;margin-right:auto;">
            <tr>
              <th>Software Company</th>
              <th>Position Name</th>
              <th>Description</th>
              <th>Expectations</th>
              <th>Deadline</th>
            </tr>
           
"""
print(htmltable)
i = 0
positions = db.getinternshippositions()
htmlrow = """
         <tr> 
                <td > <a onclick = "window.location.href='companydetails.py?{i[0]}'"> {i[0]} </a></td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
                <td>{i[3]}</td>
                <td>{i[4]}</td>
            </tr>
"""

htmlend = """
        </table>
        </body>
</html>
"""

size = db.countRow("INTERNSHIPPOSITION")
for i in positions:
    print(htmlrow.format(**locals()))
    
print(htmlend)





