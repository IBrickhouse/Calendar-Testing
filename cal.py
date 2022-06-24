import calendar
from datetime import date
from xml.etree.ElementTree import tostring
import twiceMembers

def getMembersBirthday(member):
    birthday = twiceMembers.getTwice(member)["Birthday"]
    print(birthday)
    return birthday

def getMembersBirthdayMonth(member):
    birthday = twiceMembers.getTwice(member)["Birthday"]
    month = str(birthday)
    month = month[4:6]
    print(month)





#getMembersBirthday("Momo")
getMembersBirthdayMonth("Jihyo")