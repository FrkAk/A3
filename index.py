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

print(htmlHeader)
i = 0
positions = db.getinternshippositions()
htmlrow = """
                <tr> 
                    <th scope="row"> <a onclick = "window.location.href='companydetails.py?{i[0]}'"> {i[0]} </a></th>
                    <td>{i[2]}</td>
                    <td>{i[3]}</td>
                    <td>{i[4]}</td>
                    <td>{i[5]}</td>
                </tr>
"""

htmlend = """
                </tbody>
            </table>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js"></script>
        <script src="search.js"></script>
     </body>
</html>
"""
print(htmltable)
for i in positions:
    print(htmlrow.format(**locals()))

print(htmlend)
