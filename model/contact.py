from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, address=None, home=None, mobile=None, work=None, email=None,
                 email2=None, email3=None, phone2=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 group_name=None, group_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.phone2 = phone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.group_name = group_name
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.group_id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def id_gr_or_max(self):
            if self.group_id:
                return int(self.group_id)
            else:
                return maxsize

