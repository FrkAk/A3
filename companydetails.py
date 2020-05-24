#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db
import sys

a =  ('Number of arguments: %d' % len(sys.argv))
b =  ('Argument List:'+ str(sys.argv))
if len(sys.argv) == 1:
  print("Error")
else:
  details = db.companyDetails(sys.argv[1])
htmlheader = """
<html>
    <head>
        <title>Company</title>
        <style>
          table, th, td {
            border: 1px solid black;
            background-color:darkgray;
          }
        </style>
    </head>
    <body>
        <table style="width:50%; margin-left:auto;margin-right:auto;">
            <tr>
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
                <td >{details[0]} </td>
                <td>{details[1]}</td>
                <td>{details[2]}</td>
                <td>{details[3]}</td>
                <td>{details[4]}</td>
                <td>{details[5]}</td>
            </tr>
"""
htmlfootter = """
</body></html>
"""
print(htmlheader)
print(htmlrow.format(**locals()))
print(htmlfootter)