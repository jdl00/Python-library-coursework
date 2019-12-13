from tkinter import *
from bookcheckout import *
from bookreturn import *
from booksearch import *
def call_checkout():
        text_1.delete('1.0', END)
        status_code = checkout_book(entry_1.get(),entry_2.get())
        text_1.insert(END,status_code+"\n")
                

def call_return():
        text_1.delete('1.0', END)
        status_code = return_book(entry_1.get(),entry_2.get())
        text_1.insert(END,status_code+"\n")


def call_search():
        text_1.delete('1.0', END)
        text_to_print = []
        text_to_print = query_database_by_text(entry_3.get())
        for x in text_to_print:
                text_1.insert(END,x+"\n")

def display_popular():
        print("hey")
                 
        



window = Tk()
window.title("Library Program")
window.geometry('1000x700')


label_1 = Label(window,text = "welcome to the library system")
label_2 = Label(window,text = "enter member id")
label_3 = Label(window,text = "enter book id")
label_4 = Label(window,text = "enter book title")

entry_1 = Entry(window)
entry_2 = Entry(window)
entry_3 = Entry(window)

button_1 = Button(window,text = "checkout",command = call_checkout)
button_2 = Button(window,text = "return",command = call_return)
button_3 = Button(window,text = "search",command = call_search)
button_4 = Button(window,text = "display popular books",command = display_popular)

text_1 = Text(window)


#text
text_1.grid(row=8,column=1)

#entry forms
entry_1.grid(row=5,column=1)
entry_2.grid(row=6,column=1)
entry_3.grid(row=7,column=1)
#buttons
button_1.grid(row=5,column=1000)
button_2.grid(row=6,column=1000)
button_3.grid(row=7,column=1000)
button_4.grid(row =4,column=1)
#labels
label_1.grid(row=0,column=0)
label_2.grid(row=5, column=0)
label_3.grid(row=6, column=0)
label_4.grid(row=7,column=0)


        
window.mainloop()

