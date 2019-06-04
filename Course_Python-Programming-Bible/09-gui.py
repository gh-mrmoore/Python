import tkinter
from tkinter import *

window = tkinter.Tk()
"""buttons"""
#def PopupFunction():
#    msg = messagebox.showinfo("popup title", "message")

#buttonWidget = tkinter.Button(window, text="Click Here", command = PopupFunction)
#buttonWidget.place(x = 5, y = 5)

"""canvas"""
#canvasWidget = tkinter.Canvas(window, bg="yellow", height = 512, width = 512)
#coord = 25, 50, 512, 512
#arcObject = canvasWidget.create_arc(coord, start = 0, extent = 270, fill = "white")
#lineObject = canvasWidget.create_line(75, 10, 20, 150, fill = "black")
#canvasWidget.pack()

"""checkbutton"""
#cv = IntVar()
#cb = CheckButton(window, text = "Check", variable = cv, onvalue = 1, offvalue = 0, height = 40, width = 30)
#cb.pack()

"""entry"""
#entr = Entry(window, bd = 3)
#entr.pack(side = RIGHT)

"""frame"""
#frame = Frame(window)
#frame.pack()

#btn = Button(frame, text = "Hello")
#btn.pack(side = LEFT)
#cv = IntVar()
#cb = Checkbutton(frame, text = "Here", variable = cv, onvalue = 1, offvalue = 0, height = 40, width = 40)
#cb.pack()


"""label"""
#stringVar = StringVar()
#lbl = Label(window, textvariable = stringVar)

#stringVar.set("Label Text!")
#lbl.pack()

"""listbox"""
#lbox = Listbox(window)
#lbox.insert(1, "item1")
#lbox.insert(2, "item2")
#lbox.pack()

"""menubutton"""
#mButton = Menubutton(window, text = "Click Menu")
#mButton.grid()
#mButton.menu = Menu(mButton)
#mButton["menu"] = mButton.menu

#mButton.menu.add_checkbutton(label = "Item1")
#mButton.menu.add_checkbutton(label = "Item2")
#mButton.menu.add_checkbutton(label = "Item3")
#mButton.menu.add_checkbutton(label = "Item4")
#mButton.menu.add_checkbutton(label = "Item5")

"""menu"""
#menubar = Menu(window)

#menu1 = Menu(menubar)
#menu1.add_command(label = "Python")
#menu1.add_separator()
#menu1.add_command(label = "Java")
#menu1.add_command(label = "Exit", command = window.quit)
#menubar.add_cascade(label = "Section 1", menu = menu1)

#menu2 = Menu(menubar)
#menu2.add_command(label = "JavaScript")
#menu2.add_command(label = "CSS")
#menubar.add_cascade(label = "Section 2", menu = menu2)

#window.config(menu = menubar)

"""message"""
#string = StringVar()
#msg = Message(window, textvariable = string)

#string.set("A long string of text that may run over to multiple lines")
#msg.pack()

"""radiobutton"""
#var = IntVar()

#def select():
#    selection = "Option chosen: " + str(var.get())
#    label.config(text = selection)

#radio1 = Radiobutton(window, text = "Option 1", variable = var, value = 1, command = select)
#radio1.pack(anchor = W)

#radio2 = Radiobutton(window, text = "Option 2", variable = var, value = 2, command = select)
#radio2.pack(anchor = W)

#radio3 = Radiobutton(window, text = "Option 3", variable = var, value = 3, command = select)
#radio3.pack(anchor = W)

#radio4 = Radiobutton(window, text = "Option 4", variable = var, value = 4, command = select)
#radio4.pack(anchor = W)

#label = Label(window)
#label.pack()

"""scale"""
#def getValue():
#    selection = "Value: " + str(var.get())
#    label.config(text = selection)

#var = DoubleVar()
#scale = Scale(window, variable = var)
#scale.pack()

#button = Button(window, text = "Retrieve value", command = getValue)
#button.pack()

#label = Label(window)
#label.pack()

"""scrollbar"""
#scrollBar = Scrollbar(window)
#scrollBar.pack(side = RIGHT, fill = Y)

#scrollList = Listbox(window, yscrollcommand = scrollBar.set)

#for line in range(1000):
#    scrollList.insert(END, "Row: " + str(line + 1))

#scrollList.pack()
#scrollBar.config(command = scrollList.yview)

"""text"""
#text = Text(window)
#text.insert(INSERT, "Hello World")
#text.insert(END, "Lovely Day")
#text.pack()

#text.tag_add("here", "1.0", "1.4")
#text.tag_add("start", "1.8", "1.13")
#text.tag_config("here", background = "green", foreground = "black")
#text.tag_config("start", background = "black", foreground = "green")

"""toplevel"""
#window.title("Master")
#topL = Toplevel()
#topL.title("Child")
#topL.mainloop()   #use this instead of window.mainloop()

"""spinbox"""
#sbox = Spinbox(window, from_ = 0, to = 5)
#sbox.pack()

"""panedwindow"""
#m1 = PanedWindow(window)
#m1.pack(fill = BOTH, expand = 1)

#left = Entry(m1, bd = 5)
#m1.add(left)

#m2 = PanedWindow(window, orient = VERTICAL)
#m1.add(m2)

#top = Scale(m2, orient = HORIZONTAL)
#m2.add(top)

#btn = Button(m2, text = "OK")
#m2.add(btn)

"""messagebox"""
#from tkinter import messagebox

#def msg_func():
#    messagebox.showinfo("Title", "Message")

#btn = Button(window, text = "Click Here", command = msg_func)
#btn.place(x = 5, y = 5)

"""labelframe"""
labelFrame = LabelFrame(window, text = "This is a label frame")
labelFrame.pack(fill = "both", expand = "yes")

left = Label(labelFrame, text="Inside the label frame")
left.pack()

window.mainloop()
