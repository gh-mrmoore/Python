from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Listing Example')

frame = Frame(window)

book = StringVar()

radio_1 = Radiobutton(frame, text = 'HTML5', \
    variable=book, value='HTML5 in easy steps')

radio_2 = Radiobutton(frame, text = 'CSS3', \
    variable=book, value='CSS3 in easy steps')

radio_3 = Radiobutton(frame, text = 'JavaScript', \
    variable=book, value='JavaScript in easy steps')

radio_1.select()


listbox = Listbox(frame)
listbox.insert(1 , 'HTML5 in easy steps')
listbox.insert(2 , 'CSS3 in easy steps')
listbox.insert(3 , 'JavaScript in easy steps')

def list_dialog():
    box.showinfo('Selection', 'Your Choice: ' + \
    listbox.get(listbox.curselection()))

def radio_dialog():
    box.showinfo('Selection', \
    'Your Choice: \n' + book.get())

btn = Button(frame, text = 'List Choose:', command=list_dialog)
btn_radio = Button(frame, text = 'Radio Choose:', command=list_dialog)

btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx=30, pady=30)

btn_radio.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)

window.mainloop()