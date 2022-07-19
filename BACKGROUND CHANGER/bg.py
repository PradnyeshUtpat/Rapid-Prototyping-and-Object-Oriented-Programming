from tkinter import *  

win = Tk()   #Create an instance of tkinter frame or window
win.geometry('750x450')   #Set the geometry of tkinter frame

label1=Label(win, text="Pradnyesh Utpat", font=("Times",30), bg='blue')
label1.pack(padx=50)

label2=Label(win, text="112003147", font=("Times",30) , bg='cyan')
label2.pack(pady=50)

win.config(bg='turquoise')
win.mainloop()