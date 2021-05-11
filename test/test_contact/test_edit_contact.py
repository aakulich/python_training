from model.contact import Contact
#from random import randrange
import random


def test_edit_contact(app, db, check_ui):
#    if app.contact.count() == 0:
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
#    index = randrange(len(old_contacts))
    contact_new = Contact(firstname="new", lastname="new_")
    contact_new.id = contact.id
    #contact.firstname = old_contacts[index].firstname
    #contact.lastname = old_contacts[index].lastname
#    app.contact.edit_contact_by_index(index, contact)
    app.contact.edit_contact_by_id(contact.id, contact_new)
#    new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = 0
    for i in old_contacts:
        if i.id == contact.id:
            old_contacts[index] = contact_new
            break
        else:
            index = index + 1
#    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)