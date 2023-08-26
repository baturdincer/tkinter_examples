from tkinter import *

bmi_result=""
bmi=-1

window= Tk()
window.minsize(height=300,width=300)
window.title("BMI Calculator")
window.config(pady=25,padx=20)

weight_txt=Label(text="Enter Your Weight(kg)")
weight_txt.config(pady=15)
weight_txt.pack()
weight_entry=Entry(width=20)
weight_entry.pack()

height_txt=Label(text="Enter Your Height(m)", pady=15)
height_txt.pack()
height_entry=Entry(width=20)
height_entry.pack()

def bmifunc():
    global bmi_result
    global bmi
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi=weight/(height**2)
        if bmi<18.5 and bmi>0:
            bmi_result=f"Your bmi is {bmi}. You are underweight"
        elif bmi<25 and bmi>0:
            bmi_result=f"Your bmi is {bmi}. You are healthy"
        elif bmi<30 and bmi>0:
            bmi_result=f"Your bmi is {bmi}. You are overweight"
        elif bmi>=30:
            bmi_result=f"Your bmi is {bmi}. You are obese"
        else:
            bmi_result="Please enter positive integer numbers for your weight and height"
    except:
        bmi_result="Please enter positive integer numbers for your weight and height"
    print(bmi_result)
    result_txt.config(text=bmi_result)

padlabel=Label(pady=5)
padlabel.pack()

calculate_button= Button(text="Calculate", command=bmifunc)
calculate_button.pack()

padlabel=Label(pady=5)
padlabel.pack()

result_txt=Label()
result_txt.pack()

window.mainloop()