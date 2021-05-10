from model.contact import Contact
#from random import randrange
import random

def test_delete_some_contact(app, db):
#    if app.contact.count() == 0:
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test2"))
#    old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
#    index = randrange(len(old_contacts))
#    app.contact.delete_contact_by_index(index)
    app.contact.delete_contact_by_id(contact.id)
#    new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts