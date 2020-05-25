#! C:\Program Files (x86)\Python38-32\python
import cgi
from Database import Database as db


htmltable ="""
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
       
        
        <div class="table-wrapper">
            <span class="counter pull-right"></span>
            <table class="fl-table table table-hover table-bordered results">
                <thead>
                <tr>
                    <th class="col-md-5 col-xs-5">Software Company</th>
                    <th class="col-md-4 col-xs-4">Position Name</th>
                    <th class="col-md-3 col-xs-3">Description</th>
                    <th class="col-md-2 col-xs-2">Expectations</th>
                    <th class="col-md-1 col-xs-1">Deadline</th>
                </tr>
                <tr class="warning no-result">
                    <td colspan="4"><i class="fa fa-warning"></i> No result</td>
                 </tr>
                </thead>
                <tbody>
           
"""
print(htmltable)
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
        <tbody>
        </table>
        <script src="search.js"></script>
        </body>
</html>
"""

for i in positions:
    print(htmlrow.format(**locals()))
    
print(htmlend)





