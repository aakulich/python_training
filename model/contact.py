from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, home=None, mobile=None, work=None,
                            phone2=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize