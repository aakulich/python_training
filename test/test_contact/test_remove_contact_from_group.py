from model.group import Group
import random
from model.contact import Contact




def test_remove_contact_from_group(app, db, orm):
    if len(orm.get_contact_list()) > 0 and len(orm.get_group_list()) > 0:
        contact_id = random.choice(orm.get_contact_list()).id
        group = random.choice(orm.get_group_list())
        group_id = group.id
        app.contact.add_contact_to_group(contact_id, group_id)
    elif len(orm.get_contact_list()) == 0 and len(orm.get_group_list()) > 0:
        contact_id = app.contact.create(Contact(firstname="group_cont")).id
        group = random.choice(orm.get_group_list())
        group_id = group.id
        app.contact.add_contact_to_group(contact_id, group_id)
    else:
        contact_id = app.contact.create(Contact(firstname="group_cont")).id
        group = app.group.create(Group(name="group_cont"))
        group_id = group.id
        app.contact.add_contact_to_group(contact_id, group_id)
    app.contact.remove_contact_from_group(group_id)
    assert app.contact.check_contact_in_group(group_id) == len(orm.get_contacts_in_group(group))








