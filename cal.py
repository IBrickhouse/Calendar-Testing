import calendar
from datetime import date
import twiceMembers

def getMembersBirthday(member):
    print(twiceMembers.getTwice(member)["Birthday"])

getMembersBirthday("Momo")