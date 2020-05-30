import sqlite3
from datetime import date


class Database():

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.name= "Database"

    @staticmethod
    def getinternshippositions():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        today = date.today()
        internshipdetail = c.execute("SELECT SOFTWARECOMPANY.companyname, INTERNSHIPPOSITION.* ,SOFTWARECOMPANY.citycode "
                                     "FROM INTERNSHIPPOSITION "
                                     "INNER JOIN SOFTWARECOMPANY ON SOFTWARECOMPANY.username = INTERNSHIPPOSITION.companyusername "
                                     "WHERE INTERNSHIPPOSITION.deadline >= ?"
                                     "ORDER BY  deadline DESC", (today,))

        internships = internshipdetail.fetchall()
        conn.commit()
        conn.close()
        liste = []
        if internships == []:
            return liste
        else:
            for i in  internships:
                liste.append(i)
            return liste

    @staticmethod
    def getinternshippositionsforacompany(user):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        internshipdetail = c.execute(
            "SELECT internshipname,details,expectations,deadline FROM INTERNSHIPPOSITION "
            "WHERE companyusername = ? ORDER BY  deadline DESC",(user,))

        internships = internshipdetail.fetchall()

        conn.commit()
        conn.close()
        liste = []
        if internships == []:
            return liste
        else:
            for i in internships:
                liste.append(i)
            return liste

    @staticmethod 
    def authenticationForCompany(account):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        #accoun is not none
        keyUsername = account[0]
        keyPassword = account[1]

        ACCOUNT = c.execute("SELECT username,pwd FROM SOFTWARECOMPANY WHERE username = ? AND pwd = ?",
                             (keyUsername, keyPassword,))
        ID = ACCOUNT.fetchall()

        conn.commit()
        conn.close()

        if ID == []:
            return None
        else:
            return ID[0][0]

    @staticmethod
    def registerationForCompany(registrationDetails):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        for i in registrationDetails:
            if i is None:
                return False # if return value is null value registeration will not be accepted

        keyUsername = registrationDetails[0]

        isUserExist = c.execute("SELECT username FROM SOFTWARECOMPANY "
                                "WHERE username = ?",(keyUsername,))

        user = isUserExist.fetchone()


        if user != None:
            return False
        citycode = c.execute("SELECT citycode FROM CITY WHERE cityname = ?",(registrationDetails[6],))
        city = citycode.fetchone()
        registrationDetails[6] = city[0]
        c.execute(
            "INSERT INTO SOFTWARECOMPANY(username, pwd, companyname, email, telephone,website, citycode, address)VALUES(?,?,?,?,?,?,?,?)",
            registrationDetails)

        conn.commit()
        conn.close()
        return True

    @staticmethod
    def internshipAdd(intershipDetails):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        for i in intershipDetails:
            if i is None:
                return "NullValue"


        id = c.execute("SELECT MAX(ID) FROM INTERNSHIPPOSITION")

        biggestID = id.fetchone()
        biggest = biggestID[0]
        if biggestID[0] == None:
            biggest = 1
        else:
            biggest = biggest+1
        liste = []
        liste.append(biggest)
        liste.extend(intershipDetails)

        c.execute(
            "INSERT INTO INTERNSHIPPOSITION(id, internshipname, details, expectations,deadline,companyusername)VALUES(?,?,?,?,?,?)",liste)

        conn.commit()
        conn.close()

        return "Succesful"
    

    @staticmethod
    def companyDetails(companyName):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        companyExist =c.execute("SELECT companyname,email,telephone,website,address,cityname FROM SOFTWARECOMPANY "
                                "INNER JOIN CITY ON SOFTWARECOMPANY.citycode = CITY.citycode "
                                "WHERE companyname = ? ",(companyName,))

        companyInfo = companyExist.fetchmany()
        liste = []
        for i in companyInfo[0]:
            liste.append(i)

        conn.commit()
        conn.close()

        if companyInfo == []:
            return "Company existing error"
        else:
            return liste

    @staticmethod
    def addLog(sesionID,username):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO LOG(sessionID, username)VALUES(?,?)",(sesionID,username,))

        conn.commit()
        conn.close()

    @staticmethod
    def getSessionUsername(sesionID):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        user = c.execute(
            "SELECT DISTINCT username FROM LOG WHERE sessionID = ?", (sesionID,))

        sesionUsername = user.fetchone()
        conn.commit()
        conn.close()
        if sesionUsername is not None:
            return sesionUsername[0]
        else:
            return None


    @staticmethod
    def updateLogStatus(sesionID,statusValue):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "UPDATE LOG SET status = ? WHERE sessionID = ?",(statusValue,sesionID,))

        conn.commit()
        conn.close()

    @staticmethod
    def getLogStatus(sesionID):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        status = c.execute(
            "SELECT status FROM LOG WHERE sessionID = ?", (sesionID,))

        sesionStatus = status.fetchone()

        conn.commit()
        conn.close()
        if sesionStatus is not None:
            return sesionStatus[0]
        else:
            return None

    @staticmethod
    def checkDatabesExistance():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        flag = False

        # get the count of tables with the name
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='CITY' ''')

        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            flag = True

        # commit the changes to db
        conn.commit()
        # close the connection
        conn.close()
        return flag
   
    @staticmethod
    def databaseInitiation():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE CITY (
                    citycode INTEGER PRIMARY KEY,
                    cityname TEXT NOT NULL)""")

        c.execute("""CREATE TABLE SOFTWARECOMPANY(
                    username TEXT NOT NULL PRIMARY KEY,
                    pwd TEXT NOT NULL,
                    website TEXT NOT NULL,
                    companyname TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telephone INTEGER,
                    address TEXT NOT NULL,
                    citycode INTEGER,
                    FOREIGN KEY (citycode) REFERENCES CITY (citycode))
                    """)

        c.execute("""CREATE TABLE INTERNSHIPPOSITION(
                     id INTEGER PRIMARY KEY,
                     internshipname TEXT NOT NULL,
                     details TEXT NOT NULL,
                     expectations TEXT NOT NULL,
                     deadline DATE NOT NULL,
                     companyusername TEXT NOT NULL,
                     FOREIGN KEY (companyusername) REFERENCES SOFTWARECOMPANY (username))""")

        c.execute("""CREATE TABLE LOG(
                     sessionID TEXT PRIMARY KEY,
                     username TEXT NOT NULL,
                     status INTEGER DEFAULT 0)""")

        cities = [(1, 'Gazimagusa'),
                  (2, 'Girne'),
                  (3, 'Guzelyurt'),
                  (4, 'Iskele'),
                  (5, 'Lefke'),
                  (6, 'Lefkosa')]

        companies = [('apple', 'apple123', 'apple.com', 'Apple', 'apple@apple.com', '0123456', 'apple blv. 123 st.', 1),
                     ('google', 'google123', 'google.com', 'Google', 'google@google.com', '14785239',
                      'google blv. 456 st.',
                      2),
                     ('twitter', 'twit123', 'twitter.com', 'Twitter', 'twitter@twitter.com', '1518468',
                      'twitter blv. 789 st.', 3),
                     ('facebook', 'feys123', 'facebook.com', 'Facebook', 'facebook@facebook.com', '14785236',
                      'facebook blv. 1234 st.', 4),
                     ('reddit', 'red123', 'reddit.com', 'Reddit', 'reddit@reddit.com', '14782536',
                      'reddit blv. 4125 st.',
                      5),
                     ('github', 'git123', 'github.com', 'GitHub', 'github@git.com', '146589465', 'github blv. 254 st.',
                      6)]

        intership = [(1, 'Apple Summer Intern', 'C/C++ Intern', 'Knowing C/C++, Java is a Plus', '2020-06-14', 'apple'),
                     (2, 'Google Summer Intern', 'Python Open Source Developer', 'Scripting Language is a must',
                      '2020-06-18', 'google'),
                     (3, 'Twitter Summer Intern', 'React Developer Intern', 'React Frame is a must', '2020-07-18',
                      'twitter')]

        c.executemany("INSERT INTO CITY(citycode, cityname)VALUES(?, ?)", cities)
        c.executemany(
            "INSERT INTO SOFTWARECOMPANY(username, pwd, website, companyname, email, telephone, address, citycode)VALUES(?,?,?,?,?,?,?,?)",
            companies)
        c.executemany(
            "INSERT INTO INTERNSHIPPOSITION(id,internshipname, details, expectations, deadline, companyusername)VALUES(?,?,?,?,?,?)",
            intership)


        conn.commit()
        conn.close()


