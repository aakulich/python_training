# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first", lastname="last", home="11111",
                           mobile="22222", work="33333", phone2="44444")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
 #   contact = Contact(firstname="", middlename="", lastname="", nickname="",
  #                         photo="C:\\P&P4.jpg", title="", company="", address="", home="",
   #                       mobile="", work="", fax="", email="", email2="",
   #                       email3="", homepage="", bday="", bmonth="-", byear="", aday="",
   #                       amonth="-", ayear="", address2="", phone2="",
   #                       notes="")
#   app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

