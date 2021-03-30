from model import contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def select_home_tab(self):
        wd = self.app.wd
        wd.find_element_by_id("header").click()
        wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        self.select_home_tab()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name2, text2):
        wd = self.app.wd
        if text2 is not None:
            wd.find_element_by_name(field_name2).click()
            wd.find_element_by_name(field_name2).clear()
            wd.find_element_by_name(field_name2).send_keys(text2)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_home_tab()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.select_home_tab()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_home_tab()
        self.select_first_contact()
        # click edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_contact_form(contact)
        # select update
        wd.find_element_by_name("update").click()
        self.select_home_tab()


    def view_first_contact_details(self):
        wd = self.app.wd
        self.select_home_tab()
        self.select_first_contact()
        # click Details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        self.select_home_tab()


    def modify_first_contact_details(self, contact):
        wd = self.app.wd
        self.select_home_tab()
        self.select_first_contact()
        # click Details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact)
        # select update
        wd.find_element_by_name("update").click()
        self.select_home_tab()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()




