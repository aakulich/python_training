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


def proper_group_to_remove_contact(app, db, orm):
    # возвращает группу, из которой можно удалить контакт
    i = 0
    lg = len(orm.get_group_list())
    group = object


    for g in orm.get_group_list():

        if len(orm.get_contacts_in_group(g)) > 0:  # проверяем есть ли такие контакты, которые добавлены в эту группу
            group = g
            break
        else:
            i = i + 1
            if i == lg:  # если групп с добавленными контактами нет, то берем любую и добавляем любой контакт
                group = random.choice(db.get_group_list())
                contact = random.choice(db.get_contact_list())
                app.contact.add_contact_to_group(contact.id, group.id)
                break

    return group


def test_remove_contact_from_group(app, db, orm):
    check_contact_and_group_present(app, db)
    old_contacts_in_groups = db.get_contact_with_group_list()
    group = proper_group_to_remove_contact(app, db, orm)
    group_id = group.id
    contact_id = app.contact.remove_contact_from_group(group_id)
    new_contacts_in_groups = db.get_contact_with_group_list()
    assert len(old_contacts_in_groups) - 1 == len(new_contacts_in_groups)
    assert app.contact.check_contact_not_in_group(group_id) == len(orm.get_contacts_not_in_group(group))
    assert len(orm.get_contacts_not_in_group(group)) > 0







