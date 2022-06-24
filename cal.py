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
        return int(bdayMonth)
    else:
        return int(bdayMonth)

def showBdayMonCal(member):
    monCal = calendar.month(currentYear, int(getMembersBirthdayMonth(member)))
    return monCal


# showBdayMonCal("Nayeon")
# showBdayMonCal("Jeongyeon")
# showBdayMonCal("Momo")
# showBdayMonCal("Sana")
# showBdayMonCal("Jihyo")
# showBdayMonCal("Mina")
# showBdayMonCal("Dahyun")
# showBdayMonCal("Chaeyoung")
# showBdayMonCal("Tzuyu")