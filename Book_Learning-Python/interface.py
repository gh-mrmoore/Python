from tkinter import *

window = Tk()

window.title('Label Example')
window.bg = 'yellow'

def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'gray')
    else:
        window.configure(bg = 'yellow')

label = Label(window, text = 'Hello World!')

btn_switch = Button(window, text = "Switch", command=tog)
btn_end = Button(window, text = "Close", command=exit)

label.pack(padx = 200, pady = 50)

btn_end.pack(padx = 200, pady = 50)
btn_switch.pack(padx = 200, pady = 50)

window.mainloop()