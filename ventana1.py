from tkinter import *
ventana = Tk()
ventana.title('Labels')
label1=Label(ventana,text="Intro to Tkinter")
label1.grid(row=1,column=1)
label2=Label(ventana,text="Otro")
label2.grid(row=2,column=1)
boton1=Button(ventana,text="Boton 1")
boton1.grid(row=3,column=2)
ventana.mainloop()