from tkinter import *
from utils import *

window = Tk()

window.geometry("500x350")
window.maxsize(500, 350)
window.minsize(500, 350)

window.title("Website blocker")

label1 = Label(window, text="Add website")
label1.place(x=5,y=20)
input1 = Text(window, font='Arial', height=1, width=40)
input1.place(x=90,y=20)
button1 = Button(window, text="Add", command=lambda: blockWebsite(input1.get(1.0, END)))
button1.place(x=5,y=53)

frame = LabelFrame(window, text="Blocked website list", padx=4, pady=4)
frame.place(x=5,y=85)

def showBlockedWebsites():
    r = 0
    websiteList = getBlockedWebsites()
    for website in websiteList:
        Label(frame, text=website).grid(row=r,column=0)
        Button(frame, text='unblock').grid(row=r,column=1)
        r = r + 1

showBlockedWebsites()

if __name__ == '__main__':
    mainloop()
