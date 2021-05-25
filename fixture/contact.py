from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select
import random



class ContactHelper:

    def __init__(self, app):
        self.app = app


    def select_home_tab(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_id("header")
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
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("phone2", contact.phone2)

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
        self.select_home_tab()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_home_tab()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.select_home_tab()
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name('td')[7]
        cells.find_element_by_tag_name("a").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        i = 0
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name('td')
            id_v = cells[0].find_element_by_tag_name("input").get_attribute("value")
            if id_v == id:
                cells[7].find_element_by_tag_name("a").click()
                break
            else:
                i = i+1



   # def edit_first_contact(self, contact):
    #    wd = self.app.wd
   #     self.edit_contact_by_index(0)


    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_home_tab()
        self.select_contact_by_index(index)
        # click edit
        #wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_contact_form(new_contact_data)
        # select update
        wd.find_element_by_name("update").click()
        self.select_home_tab()
        self.contact_cache = None


    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.select_home_tab()
        self.select_contact_by_id(id)
        # click edit
        #wd.find_element_by_xpath("//img[@alt='Edit']").click()
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
        #click Details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        self.select_home_tab()


    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.select_home_tab()
        # select contact
        self.check_contact_by_id(contact_id)
        self.select_group_to_add(group_id)
        wd.find_element_by_name("add").click()
        #self.return_to_home_page()
        self.contact_cache = None


    def check_contact_by_id(self, id):
        wd = self.app.wd
        i = 0
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name('td')
            id_v = cells[0].find_element_by_tag_name("input").get_attribute("value")
            if id_v == id:
                cells[0].find_element_by_name("selected[]").click()
                break
            else:
                i = i+1



    def select_group_to_add(self, group_id):
        wd = self.app.wd
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)

    def check_contact_in_group(self, group_id):
        wd = self.app.wd
        self.select_home_tab()
        self.select_group_from_dropdown(group_id)
        i = len(wd.find_elements_by_name("entry"))
        return i

    def check_contact_not_in_group(self, group_id):
        wd = self.app.wd
        self.select_home_tab()
        Select(wd.find_element_by_name("group")).select_by_value('')
        a = len(wd.find_elements_by_name("entry"))
        self.select_group_from_dropdown(group_id)
        b = len(wd.find_elements_by_name("entry"))
        i = a - b
        return i


    def select_group_from_dropdown(self, group_id):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_value(group_id)


    def remove_contact_from_group(self, group_id):
        wd = self.app.wd
        self.select_home_tab()
        self.select_group_from_dropdown(group_id)
        row = random.choice(wd.find_elements_by_name("entry"))
        cells = row.find_elements_by_tag_name('td')
        cells[0].find_element_by_name("selected[]").click()
        wd.find_element_by_name("remove").click()
        return group_id



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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute("value")
        home = wd.find_element_by_name('home').get_attribute("value")
        mobile = wd.find_element_by_name('mobile').get_attribute("value")
        work = wd.find_element_by_name('work').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        phone2 = wd.find_element_by_name('phone2').get_attribute("value")
        return Contact (firstname=firstname, lastname=lastname, id=id, address=address, home=home, mobile=mobile, work=work, email=email,
                        email2=email2, email3=email3, phone2 = phone2)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.select_home_tab()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name('td')[7]
        cells.find_element_by_tag_name("a").click()



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.select_home_tab()
        line_sel = wd.find_elements_by_name("entry")[index]
        edit_con = line_sel.find_elements_by_tag_name('td')[6]
        edit_con.find_element_by_tag_name("a").click()


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work,
                       phone2=phone2)
