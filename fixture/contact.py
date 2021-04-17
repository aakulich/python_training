from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def select_home_tab(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0):
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
        #self.select_home_tab()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_home_tab()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # wd.find_element_by_css_selector("div.msgbox")
        self.select_home_tab()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        line_sel = wd.find_element_by_name("entry")[index]
        edit_con = line_sel.find_elements_by_tag_name('td')[7]
        edit_con.find_element_by_tag_name("a").click

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_home_tab()
        self.select_contact_by_index(index)
        # click edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_contact_form(new_contact_data)
        # select update
        wd.find_element_by_name("update").click()
        self.select_home_tab()
        self.contact_cache = None


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
        wd.find_element_by_name("modify").click()
        self.fill_contact_form(contact)
        # select update
        wd.find_element_by_name("update").click()
        self.select_home_tab()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.select_home_tab()
        return len(wd.find_elements_by_name("entry"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.select_home_tab()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                col = element.find_elements_by_tag_name('td')
                first_name = col[2].text
                last_name = col[1].text
                id = col[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = col[5].text.splitlines()
                self.contact_cache.append(Contact(id=id, lastname=last_name, firstname=first_name, home=all_phones[0],
                                                  mobile=all_phones[1], work=all_phones[2], phone2=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.select_home_tab()
        line_sel = wd.find_element_by_name("entry")[index]
        edit_con = line_sel.find_elements_by_tag_name('td')[7]
        edit_con.find_element_by_tag_name("a").click


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        home = wd.find_element_by_name('home').get_attribute("value")
        mobile = wd.find_element_by_name('mobile').get_attribute("value")
        work = wd.find_element_by_name('work').get_attribute("value")
        phone2 = wd.find_element_by_name('phone2').get_attribute("value")
        return Contact (firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work, phone2 = phone2)


