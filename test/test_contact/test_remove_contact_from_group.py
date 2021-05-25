from model.group import Group
import random
from model.contact import Contact




def test_remove_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0 and len(db.get_group_list()) == 0:
        contact = Contact(firstname="group_cont")
        app.contact.create(contact)
        group = Group(name="group_cont")
        app.group.create(group)
        group = random.choice(db.get_group_list())
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    elif len(db.get_contact_list()) == 0 and len(db.get_group_list()) > 0:
        contact = Contact(firstname="group_cont")
        app.contact.create(contact)
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    elif len(db.get_contact_list()) > 0 and len(db.get_group_list()) == 0:
        group = Group(name="group_cont")
        app.group.create(group)
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group(contact.id, group.id)

    i = 0
    lg = len(orm.get_group_list())
    for g in orm.get_group_list():
        if len(orm.get_contacts_in_group(g)) > 0:
            #contact_id = orm.get_contacts_in_group(g)[0].id
            group = g
            group_id = g.id
            app.contact.remove_contact_from_group(group_id)
            break
        else:
            i = i + 1
            if i == lg:
                group = g
                group_id = g.id
                contact = random.choice(db.get_contact_list())
                app.contact.add_contact_to_group(contact.id, group_id)
                app.contact.remove_contact_from_group(group_id)
                break
    assert app.contact.check_contact_not_in_group(group_id) == len(orm.get_contacts_not_in_group(group))
    assert len(orm.get_contacts_not_in_group(group)) > 0









