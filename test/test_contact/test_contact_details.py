from model.contact import Contact

def test_view_first_contact_details(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.view_first_contact_details()

def test_modify_first_contact_details(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact_details(Contact(firstname="first_updated", middlename="middle_updated", lastname="last_updated", nickname="nick_updated",
                           photo="C:\\updated.jpg", title="my_title_updated", company="my_company_updated", address="my_address_updated", home="my_home_updated",
                           mobile="my_mobile_updated", work="my_work_updated", fax="my_fax_updated", email="my_email_updated", email2="my_email2_updated",
                           email3="my_email3_updated", homepage="my_homepage_updated", bday="30", bmonth="June", byear="1990", aday="30",
                           amonth="June", ayear="1990", address2="second_address_updated", phone2="second_home_updated",
                           notes="my_notes_updated"))




