from tkinter import *

import calendar

from datetime import date

window = Tk()

window.config(background ='white')
# ceate a label widget
window.title("Month Calendar")

window.geometry("200x200")

currentDay = date.today().day
currentMonth = date.today().month
currentYear = date.today().year

content = calendar.month(currentYear,currentMonth)

moncal = Label(window, text=content)
moncal.grid(row=5, column=1)

# event loop
window.mainloop()

