from tkinter import*
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
               value=eval(scvalue.get()) 
            except Exception as e:
               scvalue.set("Error")
               screen.update() 

        scvalue.set(value)
        screen.update()      

    elif text=="C":
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        screen.pack()      
root=Tk()
root.title('Calculator')
root.configure()
root.geometry("340x450")
root.maxsize(340,450)
root.maxsize(340,450)
scvalue=StringVar()
scvalue.set("")
screen=Entry(root, bg="white",borderwidth = 0,justify="right",textvariable=scvalue,font="lucida 30")
screen.pack(fill=X, ipadx=5, pady=10 , padx=5)
fsc=Frame(root, bg="light blue")
but=Button(fsc, text="C", font ="arial 30",borderwidth = 0,fg="white", bg="#72d574",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
but=Button(fsc, text="( ", font ="lucida 30",borderwidth = 0, bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
but=Button(fsc, text=")" ,font ="lucida 30",borderwidth = 0, bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
but=Button(fsc, text="/", font ="lucida 30",borderwidth = 0, bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
fsc.pack()
fsc=Frame(root, bg="black")
i = 7
while (i <= 9):
    but=Button(fsc, text=str(i), font ="arial 30",borderwidth = 0, bg="white",width=3, height=1)
    but.pack(side=LEFT)
    but.bind("<Button-1>", click)
    i+=1
but=Button(fsc, text="*", font ="lucida 30",borderwidth = 0, bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)     
fsc.pack()    
fsc=Frame(root, bg="black")
i = 4
while (i <= 6):
    but=Button(fsc, text=str(i), font ="lucida 30",borderwidth = 0, bg="white",width=3, height=1)
    but.pack(side=LEFT)
    but.bind("<Button-1>", click)
    i+=1
but=Button(fsc, text="-", font ="lucida 30",borderwidth = 0, bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)     
   
fsc.pack()
fsc=Frame(root, bg="black")
i = 1
while (i <= 3):
    but=Button(fsc, text=str(i), font ="lucida 30",borderwidth = 0, bg="white",width=3, height=1)
    but.pack(side=LEFT)
    but.bind("<Button-1>", click)
    i+=1
but=Button(fsc, text="+", font ="lucida 30",borderwidth = 0,bg="#c1f4c2",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)     
fsc.pack()
fsc=Frame(root, bg="black")
but=Button(fsc, text="0", font ="lucida 30",borderwidth = 0, bg="white",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
but=Button(fsc, text=".", font ="lucida 30",borderwidth = 0, bg="white",width=3, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)
but=Button(fsc, text="=", font ="lucida 30",fg="white",borderwidth = 0,padx=3.5, bg="#72d574",width=6, height=1)
but.pack(side=LEFT)
but.bind("<Button-1>", click)

fsc.pack()
root.mainloop()
