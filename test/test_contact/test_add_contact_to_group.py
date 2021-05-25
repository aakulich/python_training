from model.group import Group
import random
from model.contact import Contact



def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0 and len(db.get_group_list()) == 0:
        contact = Contact(firstname="group_cont")
        app.contact.create(contact)
        group = Group(name="group_cont")
        app.group.create(group)
        app.contact.add_contact_to_group(contact.id, group.id)
    elif len(db.get_contact_list()) == 0 and len(db.get_group_list()) > 0:
        contact = Contact(firstname="group_cont")
        app.contact.create(contact)
        group = random.choice(db.get_group_list())
        app.group.create(group)
        app.contact.add_contact_to_group(contact.id, group.id)
    elif len(db.get_contact_list()) > 0 and len(db.get_group_list()) == 0:
        group = Group(name="group_cont")
        app.group.create(group)
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    else:
        i = 0
        lg = len(orm.get_group_list())
        for g in orm.get_group_list():
            if len(orm.get_contacts_not_in_group(g)) > 0:
                contact_id = orm.get_contacts_not_in_group(g)[0].id
                group = g
                group_id = g.id
                app.contact.add_contact_to_group(contact_id, group_id)
                break
            else:
                i = i+1
                if i == lg:
                    group = Group(name="group_extra")
                    app.group.create(group)
                    contact = random.choice(db.get_contact_list())
                    app.contact.add_contact_to_group(contact.id, group.id)
                    break
    assert app.contact.check_contact_in_group(group_id) == len(orm.get_contacts_in_group(group))
    assert len(orm.get_contacts_in_group(group)) > 0





#def test_add_contact_to_group(app, db, orm):
#    if len(db.get_group_list()) == 0:
#        group = Group(name="group_cont")
#        app.group.create(group)
#    else:
#        group = random.choice(db.get_group_list())
#    group_id = group.id
#    if len(db.get_contact_list()) == 0:
#        contact = Contact(firstname="group_cont")
#        app.contact.create(contact)
#    else:
#        contact = random.choice(db.get_contact_list())
#    contact_id = contact.id
#    app.contact.add_contact_to_group(contact_id, group_id)
#    assert app.contact.check_contact_in_group(group_id) == len(orm.get_contacts_in_group(group))
#    assert len(orm.get_contacts_in_group(group)) > 0
