# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
#                           photo="C:\\P&P4.jpg", title="my_title", company="my_company", address="my_address", home="my_home",
#                           mobile="my_mobile", work="my_work", fax="my_fax", email="my_email", email2="my_email2",
#                           email3="my_email3", homepage="my_homepage", bday="1", bmonth="January", byear="1985", aday="1",
#                           amonth="January", ayear="1985", address2="second_address", phone2="second_home",
#                           notes="my_notes")
    contact = Contact(firstname="fn", lastname="ln")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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

