import sqlite3


def CleanEmailsDB():
    con = sqlite3.connect('./emails.db', isolation_level=None)  # autocommit
    cur = con.cursor()

    cur.execute("""
        DELETE FROM emailsTable 
        WHERE email IS NULL 
           OR email = '' 
           OR email LIKE '%.jpg' 
           OR email LIKE '%.jpeg' 
           OR email LIKE '%.png' 
           OR email LIKE '%.gif' 
           OR email LIKE '%.svg' 
           OR email LIKE '%.webp'
    """)

    return "Cleaned"
def databaseCreate():
    con = sqlite3.connect('./emails.db', isolation_level=None)  # autocommit
    cur = con.cursor()
    cur.execute("""DROP TABLE emailsTable """)
    cur.execute(""" CREATE TABLE "emailsTable" ("email"	TEXT,"domain"	TEXT);""")
    return "Database and table created"

    #useJsonContainCompanyNames("data.json")
