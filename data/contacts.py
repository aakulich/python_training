from model.contact import Contact
#import random
#import string

testdata = [
    Contact(firstname="fname1", lastname="lname1"),
    Contact(firstname="fname2", lastname="lname2")
]


#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Contact(firstname='', lastname='')] + [
#    Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20))
#    for i in range(5)
#]
