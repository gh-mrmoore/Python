from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Label Example - Button Example - Message Box Example - Entry/Response Example')

def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    if var == 1:
        box.showinfo('Yes Box', 'Proceeding...')
    else:
        box.showwarning('No Box', 'Cancelling...')

def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'gray')
    else:
        window.configure(bg = 'yellow')

def talkback():
    box.showinfo('Greetings', 'Welcome ' + entry.get())

frame = Frame(window)
entry = Entry(frame)


btn_name = Button(window, text='Enter Name', command=talkback)
btn_tog = Button(window, text='Switch', command=tog)
btn_end = Button(window, text='Close', command=exit)
btn_msg = Button(window, text='Message', command=dialog)
label = Label(window, text='Hello World!')

label.pack(padx = 200, pady=25)
btn_tog.pack(padx = 200, pady=25)
btn_end.pack(padx=200, pady=25)
btn_msg.pack(padx=200, pady=25)
btn_name.pack(side = RIGHT)
entry.pack(side = LEFT)
frame.pack(padx=200, pady=25)


window.mainloop()