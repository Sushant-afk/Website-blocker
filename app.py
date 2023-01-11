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
button1 = Button(window, text="Add", command=lambda: handleBlock())
button1.place(x=5,y=53)

frame = LabelFrame(window, text="Blocked website list", padx=4, pady=4)
frame.place(x=5,y=85)

labels_reference = []
button_reference = []

def showBlockedWebsites():
    r = 0
    websiteList = getBlockedWebsites()
    for website in websiteList:
        temp_label = Label(frame, text=website)
        temp_label.grid(row=r,column=0)
        temp_button = Button(frame, text='unblock', command=lambda m=website:handleUnblock(m))
        temp_button.grid(row=r,column=1)
        labels_reference.append(temp_label)
        button_reference.append(temp_button)
        r = r + 1

def handleBlock():
    blockWebsite(input1.get(1.0, END))
    showBlockedWebsites()

def handleUnblock(website):
    if len(labels_reference) and len(button_reference):
        for label_ref in labels_reference:
            label_ref.destroy()
        for button_ref in button_reference:
            button_ref.destroy()
        del labels_reference[:]
        del button_reference[:]
        removeFromBlocklist(website)
        showBlockedWebsites()

showBlockedWebsites()

if __name__ == '__main__':
    mainloop()
