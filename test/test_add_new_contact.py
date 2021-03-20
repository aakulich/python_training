# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
                           photo="C:\\P&P4.jpg", title="my_title", company="my_company", address="my_address", home="my_home",
                           mobile="my_mobile", work="my_work", fax="my_fax", email="my_email", email2="my_email2",
                           email3="my_email3", homepage="my_homepage", bday="1", bmonth="January", byear="1985", aday="1",
                           amonth="January", ayear="1985", address2="second_address", phone2="second_home",
                           notes="my_notes"))
    app.select_home_tab()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                           photo="C:\\P&P4.jpg", title="", company="", address="", home="",
                          mobile="", work="", fax="", email="", email2="",
                          email3="", homepage="", bday="", bmonth="-", byear="", aday="",
                          amonth="-", ayear="", address2="", phone2="",
                          notes=""))
    app.select_home_tab()
    app.session.logout()

