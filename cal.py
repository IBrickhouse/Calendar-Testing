# import statements
import calendar
from datetime import date
from xml.etree.ElementTree import tostring
import twiceMembers

# varablie definitions
currentYear = date.today().year

def getMembersBirthday(member):
    birthday = twiceMembers.getTwice(member)["Birthday"]
    print(birthday)
    return birthday

def getMembersBirthdayMonth(member):
    birthday = twiceMembers.getTwice(member)["Birthday"]
    bdayMonth = str(birthday)
    bdayMonth = bdayMonth[4:6]
    if bdayMonth[0] == '0':
        bdayMonth = bdayMonth[1]
        print(int(bdayMonth))
        return int(bdayMonth)
        #print(type(bdayMonth))
    else:
        print(int(bdayMonth))
        return int(bdayMonth)
        #print(type(bdayMonth))

def showBdayMonCal(member):
    monCal = calendar.month(currentYear,int(getMembersBirthdayMonth(member)))
    print(monCal)


#getMembersBirthday("Momo")
#getMembersBirthdayMonth("Jihyo")
showBdayMonCal("Jihyo")

#calendar.month(00,)