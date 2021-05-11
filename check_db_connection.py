import mysql.connector
from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
#    connection.close()
    db.destroy()