#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db
import sys

a = ('Number of arguments: %d' % len(sys.argv))
b = ('Argument List:' + str(sys.argv))
if len(sys.argv) == 1:
    print("Error")
else:
    details = db.companyDetails(sys.argv[1])
htmlheader = """
<html>
    <head>
        <title>Company</title>
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
    <h1>Company Details</h1>
    
    <div class="tableBox">
        <table id="{tableID}" class="tableVisual">
        <tbody>
            <tr class="header">
              <th>Software Company</th>
              <th>Email</th>
              <th>Telephone</th>
              <th>Website</th>
              <th>Address</th>
              <th>City</th>
            </tr>
            
"""
htmlrow = """
         <tr> 
                <td class="myTableHeader">{details[0]} </td>
                <td>{details[1]}</td>
                <td>{details[2]}</td>
                <td>{details[3]}</td>
                <td>{details[4]}</td>
                <td>{details[5]}</td>
            </tr>
"""

htmlfootter = """
          </tbody>
      </table>
    </div>
    <button type = "button" onclick = "window.location.href='index.py'" > Back</button>
  </body>
</html>
"""
print(htmlheader)
tableID= "tableComp" + str(1)
print(htmlrow.format(**locals()))
print(htmlfootter)
