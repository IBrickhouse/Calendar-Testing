#Import statements
from tkinter import *
import calendar
from datetime import date
import twiceMembers
import cal

window = Tk()

window.config(background ='white')
# ceate a label widget
window.title("Month Calendar")
window.geometry("150x150")
window.configure(bg='blue')

#content = calendar.month(currentYear,currentMonth)
content = cal.showBdayMonCal("Chaeyoung")

moncal = Label(window, text=content)
moncal.pack()
#moncal.grid(row=0, column=0)

# event loop
window.mainloop()
