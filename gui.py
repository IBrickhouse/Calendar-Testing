#Import statements
from tkinter import *
import calendar
from datetime import date
import twiceMembers
import cal

window = Tk()

window.title("Month Calendar")
window.geometry("150x150")
#window.configure(bg='red')
window.configure(bg=str(twiceMembers.twice["Color"]))

# make page content
#content = calendar.month(currentYear,currentMonth)
userContent = input("Member Name: ")
content = cal.showBdayMonCal(userContent)
window.configure(bg=str(twiceMembers.getTwice(userContent)["Color"]))

# ceate a label widget
moncal = Label(window, text=content)
moncal.pack()
#moncal.grid(row=0, column=0)

# event loop
window.mainloop()
