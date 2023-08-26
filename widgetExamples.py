from tkinter import *

window= Tk()
window.title("widgetExamples.py")
window.minsize(width=600, height=600)
window.config(pady=20,padx=20)

mylabel= Label(text=" My label")
mylabel.config(bg="light blue", fg="dark blue")
style=("Arial",25)
mylabel.config(font=style, padx=15, pady=15)
mylabel.pack()

def buttonfuc():
    print("button clicked")
    txt1=mytext.get("1.0", END)
    print(txt1)
mybutton=Button(text="CLICK ME", command=buttonfuc)
mybutton.config(padx=15,pady=15)
mybutton.pack()

myentry= Entry(width=20)
myentry.pack()

mytext=Text(width=30, height=10)
mytext.pack()

def scalefunc(value):
    print(value)
myScale= Scale(from_=0, to=50, command=scalefunc)
myScale.pack()

def checkbuttonfunc():
    print(check_state.get())
check_state= IntVar()
mycheckbutton= Checkbutton(text="check",variable=check_state, command=checkbuttonfunc)
mycheckbutton.pack()

def radiobuttonfunc():
    print(radioButton_state.get())
radioButton_state= IntVar()
myRadioButton= Radiobutton(text="10", value=10,variable=radioButton_state,command=radiobuttonfunc)
myRadioButton2= Radiobutton(text="20", value=20,variable=radioButton_state,command=radiobuttonfunc)
myRadioButton.pack()
myRadioButton2.pack()


def listboxfunc(event):
    print(myListBox.get(myListBox.curselection()))
myListBox= Listbox()
mylist=["Uganda","Kenya","Libya", "Somali"]
for i in range(len(mylist)):
    myListBox.insert(i,mylist[i])
myListBox.bind('<<ListboxSelect>>',listboxfunc)
myListBox.pack()

window.mainloop()