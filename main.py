from tkinter import *

#
def function1():
    a = txt0.get()
    b = txt1.get()
    c = txt2.get()
    d = "walla walla bing bang, supercalifragilisticexpialidocious"
    e = a + b + c + d
    print(e)
    txt3.insert('1.0', e)
    return

def function2():
    txt0.delete(0, 'end')
    txt1.delete(0, 'end')
    txt2.delete(0, 'end')
    txt3.delete('1.0', 'end')
    return

# Declare Tkinter
root = Tk()
root.title('Title')
root.geometry('500x400')
root.resizable(True, True)

# Tkinter Row 0 - Label and Entry
lbl0 = Label(root, text="Input 1", width=10)
lbl0.grid(row=0, column=0)
txt0 = Entry(root)
txt0.grid(row=0, column=1)

# Tkinter Row 1 - Label and Entry
lbl1 = Label(root, text="Input 2", width=10)
lbl1.grid(row=1, column=0)
txt1 = Entry(root)
txt1.grid(row=1, column=1)

# Tkinter Row 2 - Label and Entry
lbl2 = Label(root, text="Input 3", width=10)
lbl2.grid(row=2, column=0)
txt2 = Entry(root)
txt2.grid(row=2, column=1)

# Tkinter Row 3 - Button
btn0 = Button(root, text="Button 1", width=10, command=function1)
btn0.grid(row=3, column=1)

# Tkinter Row 4 - Text
txt3 = Text(root, width=25, height=10)
txt3.grid(row=4, column=1)

# Tkinter Row 5 - Button
btn1 = Button(root, text="Button 2", width=10, command=function2)
btn1.grid(row=5, column=1)

root.mainloop()
