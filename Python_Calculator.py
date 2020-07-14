from tkinter import *
def btn_click() :
    print("Akhila")
window =Tk()
window.geometry("400x440",)
# For adding a title 'CALCULATOR'
window.title("CALCULATOR")
window.configure(bg="#354a21",)
txt_input=StringVar()
# zeroth row
txtDisplay=Entry(window, font=('arial',25,'bold'),textvariable=txt_input,relief=RIDGE,bd=20,insertwidth=4,bg="#728c69", justify="right" ).grid(columnspan=4,pady=10)
# First  row
btn_percentage=Button(window,text="%",bg="#728c69",padx=20,bd=8,fg="black",font=('arial',19,'bold')).grid(row=1,column=0)
btn_ce=Button(window,bg="#728c69",text="CE",padx=19,bd=8,fg="black",font=('arial',18,'bold')).grid(row=1,column=1)
btn_c=Button(window,bg="#728c69",text="C",padx=20,bd=8,fg="black",font=('arial',19,'bold')).grid(row=1,column=2)
btn_back_space=Button(window,bg="#728c69",text="⌫",padx=14,bd=8,fg="black",font=('arial',19,'bold')).grid(row=1,column=3)
# Second row
btn7=Button(window,text="7",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold'),command=btn_click()).grid(row=2,column=0)
btn8=Button(window,text="8",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=2,column=1)
btn9=Button(window,text="9",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=2,column=2)
btn_add=Button(window,text="+",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',19,'bold')).grid(row=2,column=3)
# Third row
btn4=Button(window,text="4",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=3,column=0)
btn5=Button(window,text="5",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=3,column=1)
btn6=Button(window,text="6",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=3,column=2)
btn_sub=Button(window,text="-",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=3,column=3)
# Fourth row
btn1=Button(window,text="1",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=4,column=0)
btn2=Button(window,text="2",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=4,column=1)
btn3=Button(window,text="3",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=4,column=2)
btn_mul=Button(window,text="*",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=4,column=3)
# fifth row
btn_zero=Button(window,text="0",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=5,column=0)
btn_point=Button(window,text=".",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=5,column=1)
btn_equal=Button(window,text="=",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=5,column=2)
btn_div=Button(window,text="/",padx=20,bd=8,fg="black",bg="#728c69",font=('arial',20,'bold')).grid(row=5,column=3)
window.mainloop()