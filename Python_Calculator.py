from tkinter import *

# function to read from button
def btnClick(numbers) :
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

#function to clear display
def btnClearDisplay() :
    global operator
    operator = ""
    txt_input.set("")

#function to clear display
def btnEqualsInput():

    try:
        global operator
        sumup = str(eval(operator))
        txt_input.set(sumup)
        operator = ""
    except ZeroDivisionError:
        a="Can't divided by zero"
        txt_input.set(a)
        operator=""

#function to backspace
def backspace():
        global operator
        text = txt_input.get()[:-1]
        txt_input.set(text)
        operator=""

window =Tk()
window.geometry("400x440",)
# For adding a title 'CALCULATOR'
window.title("CALCULATOR")
operator=""
window.configure(bg="#354a21")
txt_input=StringVar()
# zeroth row
txtDisplay=Entry(window, font=('arial',25,'bold'),textvariable=txt_input,relief=RIDGE,bd=20,insertwidth=4,bg="#728c69"
                 , justify="right",state=DISABLED ).grid(columnspan=4,pady=10)

# First  row
"""btn_percentage=Button(window,text="%",bg="#728c69",padx=20,bd=8,fg="black",font=('arial',19,'bold')).grid(row=1,column=0)
btn_ce=Button(window,bg="#728c69",text="CE",padx=19,bd=8,fg="black",font=('arial',18,'bold')).grid(row=1,column=1)"""

btn_clear=Button(window,bg="#728c69",text="C",padx=120,bd=8,fg="black",font=('arial',19,'bold'),command=btnClearDisplay).grid(row=1,columnspan=3)
btn_back_space=Button(window,bg="#728c69",text="⌫",padx=14,bd=8,fg="black",font=('arial',19,'bold'),command=backspace).grid(row=1,column=3)

# Second row
btn7=Button(window,text="7",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(7)).grid(row=2,column=0)
btn8=Button(window,text="8",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(8)).grid(row=2,column=1)
btn9=Button(window,text="9",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(9)).grid(row=2,column=2)
btn_add=Button(window,text="+",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',19,'bold'),command=lambda : btnClick("+")).grid(row=2,column=3)

# Third row
btn4=Button(window,text="4",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(4)).grid(row=3,column=0)
btn5=Button(window,text="5",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(5)).grid(row=3,column=1)
btn6=Button(window,text="6",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(6)).grid(row=3,column=2)
btn_sub=Button(window,text="-",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick("-")).grid(row=3,column=3)

# Fourth row
btn1=Button(window,text="1",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(1)).grid(row=4,column=0)
btn2=Button(window,text="2",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(2)).grid(row=4,column=1)
btn3=Button(window,text="3",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(3)).grid(row=4,column=2)
btn_mul=Button(window,text="*",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick("*")).grid(row=4,column=3)

# fifth row
btn_zero=Button(window,text="0",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(0)).grid(row=5,column=0)
btn_point=Button(window,text=".",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick(".")).grid(row=5,column=1)
btn_equal=Button(window,text="=",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnEqualsInput()).grid(row=5,column=2)
btn_div=Button(window,text="÷",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=lambda : btnClick("/")).grid(row=5,column=3)
window.mainloop()
