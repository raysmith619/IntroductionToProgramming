from tkinter import * 
root = Tk() 
root.geometry('500x500') 
c=Canvas(root, bg="red", width=400, height=400, relief='solid', bd=4) 
c.pack() 
d=Label(c, text="Hello", relief='sunken', bd=2) 
d.pack() 
c.update_idletasks() 
print(c.winfo_height(), c.winfo_width()) 
root.mainloop() 
