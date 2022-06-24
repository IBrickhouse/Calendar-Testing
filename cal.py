# import statements
import calendar
from datetime import date
from xml.etree.ElementTree import tostring
import twiceMembers

# varable definitions
currentYear = date.today().year

# currentDay = date.today().day
# currentMonth = date.today().month
# currentYear = date.today().year

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
        #print(int(bdayMonth))
        return int(bdayMonth)
        #print(type(bdayMonth))
    else:
        #print(int(bdayMonth))
        return int(bdayMonth)
        #print(type(bdayMonth))

def showBdayMonCal(member):
    monCal = calendar.month(currentYear,int(getMembersBirthdayMonth(member)))
    #print(monCal)
    return monCal


# getMembersBirthday("Momo")
# getMembersBirthdayMonth("Jihyo")
# showBdayMonCal("Nayeon")
# showBdayMonCal("Jeongyeon")
# showBdayMonCal("Momo")
# showBdayMonCal("Sana")
# showBdayMonCal("Jihyo")
# showBdayMonCal("Mina")
# showBdayMonCal("Chaeyoung")
# showBdayMonCal("Tzuyu")

#calendar.month(00,)