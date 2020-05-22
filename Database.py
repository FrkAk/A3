import sqlite3


class Database():

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.name= "Database"

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
            return False
        else:
            return True

    @staticmethod
    def registerationForCompany(registrationDetails):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        for i in registrationDetails:
            if i is None:
                return "NullValue" # if return value is null value registeration will not be accepted

        keyUsername = registrationDetails[0]

        isUserExist = c.execute("SELECT username FROM SOFTWARECOMPANY "
                                "WHERE username = ?",(keyUsername,))

        user = isUserExist.fetchone()


        if user != []:
            return False

        c.execute(
            "INSERT INTO SOFTWARECOMPANY(username, pwd, website, companyname, email, telephone, address, sessionid)VALUES(?,?,?,?,?,?,?,?)",
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
            "INSERT INTO INTERNSHIPPOSITION(id, internshipname, details, expetations,deadline)VALUES(?,?,?,?,?)",liste)

        conn.commit()
        conn.close()

        return "Succesful"

    @staticmethod
    def companyDetails(companyName):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        # CİTY is missing from infos
        companyExist =c.execute("SELECT companyname,email,telephone,website,address,cityname FROM SOFTWARECOMPANY "
                                "INNER JOIN CITY ON SOFTWARECOMPANY.citycode = CITY.citycode "
                                "WHERE companyname = ? ",(companyName,))

        companyInfo = companyExist.fetchmany()
        liste = []
        for i in companyInfo[0]:
            liste.append(i)

        if companyInfo == []:
            return "Company existing error"
        else:
            return liste # add city

        conn.commit()
        conn.close()


    @staticmethod
    def checkDatabesExistance():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        flag = False

        # get the count of tables with the name
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='CITY' ''')

        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            print('Table exists.')
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
                    sessionid INTEGER,
                    citycode INTEGER,
                    FOREIGN KEY (citycode) REFERENCES CITY (citycode))
                    """)

        c.execute("""CREATE TABLE INTERNSHIPPOSITION(
                     id INTEGER PRIMARY KEY,
                     internshipname TEXT NOT NULL,
                     details TEXT NOT NULL,
                     expetations TEXT NOT NULL,
                     deadline TEXT NOT NULL)""")

        cities = [(1, 'Gazimagusa'),
                  (2, 'Girne'),
                  (3, 'Guzelyurt'),
                  (4, 'Iskele'),
                  (5, 'Lefke'),
                  (6, 'Lefkoşa')]

        companies = [('apple','apple123','apple.com','Apple','apple@apple.com','0123456','apple blv. 123 st.','123',1)]

        c.executemany("INSERT INTO CITY(citycode, cityname)VALUES(?, ?)", cities)
        c.executemany("INSERT INTO SOFTWARECOMPANY(username, pwd, website, companyname, email, telephone, address, sessionid, citycode)VALUES(?,?,?,?,?,?,?,?,?)",companies)

        conn.commit()
        conn.close()


listeintern = ["name","details","expetation","deadline"]
listecomany = ["asdf","asf","website","cname","email","tel","add","sıd"]
account = ["username","password"]
companyname = "Apple"
db = Database()
#returnval = db.internshipAdd(listeintern)
#returnval = db.registerationForCompany(listecomany)
#returnval = db.authenticationForCompany(account)
#returnval = db.companyDetails(companyname)
#print(returnval)
#db.databaseInitiation()