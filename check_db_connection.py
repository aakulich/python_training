import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)

try:
    l = db.get_contacts_not_in_group(Group(id="11"))
    for item in l:
        print(item)
    print(len(l))
finally:
#    connection.close()
  pass# db.destroy()
