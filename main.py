import tkinter
#window
window=tkinter.Tk()
window.title("Python Tkinter")
window.minsize(450,300)

def clickbutton():
    userinput=myEntry.get()
    print(userinput)

#Label
myLabel=tkinter.Label(text="label example", font=("Arial",30, "normal"))
#myLabel.config(bg="black", fg="white")
#myLabel.pack()
myLabel.grid(row=0, column=0)

#Button
myButton= tkinter.Button(text="Magic Button", command=clickbutton)
#myButton.pack()
myButton.grid(row=1,column=1)

#Entry
myEntry=tkinter.Entry(width=20)
#myEntry.pack()
myEntry.grid(row=2, column=2)

window.mainloop()