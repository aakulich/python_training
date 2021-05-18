import re
from fixture.contact import Contact


def test_phones_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = home_edit_page_data(app)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def home_edit_page_data(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    return contact_from_edit_page, contact_from_home_page


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.work == contact_from_edit_page.work
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2



def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address



def test_names_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_compare_names_address_phones_emails_on_home_page_and_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    i = 0
    for contact in contact_from_home_page:
        assert contact.firstname.strip() == contact_from_db[i].firstname.strip()
        assert contact.lastname.strip() == contact_from_db[i].lastname.strip()
        assert contact.address == contact_from_db[i].address
        assert contact.all_emails_from_home_page.strip() == merge_emails_like_on_home_page(contact_from_db[i]).strip()
        assert contact.all_phones_from_home_page.strip() == merge_phones_like_on_home_page(contact_from_db[i]).strip()
        i=i+1

#    assert contact_from_home_page.address == contact_from_db.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))




def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))