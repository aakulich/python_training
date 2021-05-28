from model.group import Group
import random
from model.contact import Contact



def check_contact_and_group_present(app, db):
    # проверяем что существует хотя бы 1 контак, если нет, то создаем
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="check_contact_and_group_present")
        app.contact.create(contact)
    else:
        pass
    # проверяем что существует хотя бы 1 группа, если нет, то создаем
    if len(db.get_group_list()) == 0:
        group = Group(name="check_contact_and_group_present")
        app.group.create(group)
    else:
        return True

def list_contact_id(db):
    # список id всех контактов
    lid = []
    i = 0

    while i < len(db.get_contact_list()):
        c = db.get_contact_list()[i]
        lid.append(c.id)
        i = i + 1

    return lid

def list_contact_with_group_id(db, group_id):
    # список id всех контактов, которые добавлены уже в конкретную группу
    lgid = []
    i = 0

    while i < len(db.get_contact_with_group_list()):
        c = db.get_contact_with_group_list()[i]
        if c.group_id == group_id:
            lgid.append(c.id)
            i = i + 1
        else:
            i = i + 1

    return lgid

def res_contact_list(db, group_id):
    # из списка id всех контактов удалены id контактов, которые уже добавлены в конкретную группу
    a = list_contact_id(db)
    b = list_contact_with_group_id(db, group_id)

    for i in b:
        for j in a:
            if i == j:
                a.remove(i)

            else:
                pass
    return a


def proper_couple_to_add(app, db, orm):
    # возвращает пару контакт-группа, которую можно использовать для теста
    i = 0
    lg = len(orm.get_group_list())
    couple = []
    contact = object

    for g in db.get_group_list():
        if len(orm.get_contacts_not_in_group(g)) > 0:
            group = g
            group_id = g.id
            contact_id = random.choice(res_contact_list(db, group_id))
            for c in db.get_contact_list():
                if str(c.id) == contact_id:
                    contact = c
                    break
                else:
                    pass
            couple.append(contact)
            couple.append(group)
            break
        else:
            i = i+1
            if i == lg:
                group = Group(name="the_only_without_contacts")
                app.group.create(group)
                contact = random.choice(db.get_contact_list())
                group = random.choice(db.get_group_list())
                couple.append(contact)
                couple.append(group)
                break
    return couple


def test_add_contact_to_group(app, db, orm):
    check_contact_and_group_present(app, db)

    list = proper_couple_to_add(app, db, orm)
    contact = list[0]
    contact_id = contact.id
    group = list[1]
    group_id = group.id
    old_contacts_in_groups = db.get_contact_with_group_list()
    app.contact.add_contact_to_group(contact_id, group_id)
    new_contacts_in_groups = db.get_contact_with_group_list()
    assert app.contact.check_contact_in_group(group_id) == len(orm.get_contacts_in_group(group))
    assert len(orm.get_contacts_in_group(group)) > 0
    for c in db.get_contact_with_group_list():
        if str(c.id) == contact_id and str(c.group_id) == group_id:
            contact = c
            break
        else:
            pass
    old_contacts_in_groups.append(contact)
    assert sorted(sorted(old_contacts_in_groups, key=Contact.id_or_max), key=Contact.id_gr_or_max) == sorted(sorted(new_contacts_in_groups, key=Contact.id_or_max), key=Contact.id_gr_or_max)