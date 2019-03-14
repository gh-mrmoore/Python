from tkinter import *

def talkback():
    box.showinfo('Greetings', 'Welcome ' + entry.get())

def check_dialog():
    str = 'Your Choice: '
    if var_1.get() == 1:
        str += '\nHTML5 in easy steps'
    if var_2.get() == 1:
        str += '\nCSS3 in easy steps'
    if var_3.get() == 1:
        str += '\nJavaScript in easy steps'
    box.showinfo('Selection: ', str)

#btn = Button(frame, text='Choose', command=check_dialog)

def main():
    #create my initial window and ask for the user's name

    window = Tk()
    window.title('My Own Application Demo')
    
    frame = Frame(window)
    entry = Entry(frame)
    btn_name = Button(window, text='Enter Name', command=talkback)

    frame.pack(padx=200, pady=25)
    entry.pack(side = LEFT)
    btn_name.pack(side = RIGHT)

    window.mainloop()

    #greet the user by name and ask them to select some things using check boxes

#    var_1 = IntVar()
#    var_2 = IntVar()
#    var_3 = IntVar()

#    book_1 = Checkbutton(frame, text = 'HTML5', \
#        variable=var_1, onvalue=1, offvalue=2)

#    book_2 = Checkbutton(frame, text = 'CSS3', \
#        variable=var_2, onvalue=1, offvalue=2)

#    book_3 = Checkbutton(frame, text = 'JavaScript', \
#        variable=var_3, onvalue=1, offvalue=2)
                        
if __name__ == "__main__":
    main()