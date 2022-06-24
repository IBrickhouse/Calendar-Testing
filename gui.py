#Import statements
from tkinter import *
import calendar
from datetime import date
import twiceMembers
import cal

window = Tk()

window.title("Birthday Month Calendar")
window.geometry("150x150")
#window.configure(bg='red')
window.configure(bg=str(twiceMembers.twice["Color"]))

# make page content
#content = calendar.month(currentYear,currentMonth)
userContent = input("Member Name: ")
content = cal.showBdayMonCal(userContent)
window.configure(bg=str(twiceMembers.getTwice(userContent)["Color"]))

# ceate a label widget
moncal = Label(window, justify=LEFT, text=content)
moncal.pack()

# event loop
window.mainloop()
