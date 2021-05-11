from model.group import Group
#from random import randrange
import random


def test_modify_group_name(app, db, check_ui):
#    if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
    group_new = Group(name="Modified_group")
    group_new.id = group.id
#    app.group.modify_group_by_index(index, group)
    app.group.modify_group_by_id(group.id, group_new)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
#    old_groups[index] = group
    index = 0
    for i in old_groups:
        if i.id == group.id:
            old_groups[index] = group_new
            break
        else:
            index = index+1
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)