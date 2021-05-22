from model.group import Group
import random
from model.contact import Contact



def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        group = Group(name="group_cont")
        app.group.create(group)
    else:
        group = random.choice(db.get_group_list())
    group_id = group.id
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="group_cont")
        app.contact.create(contact)
    else:
        contact = random.choice(db.get_contact_list())
    contact_id = contact.id
    app.contact.add_contact_to_group(contact_id, group_id)
    assert app.contact.check_contact_in_group(group_id) == len(orm.get_contacts_in_group(group))
    assert len(orm.get_contacts_in_group(group)) > 0
