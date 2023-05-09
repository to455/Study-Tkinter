from tkinter import *

def function1():
    h = txt0.get()
    w = txt1.get()

    # Convert data type from string to integer
    h = int(h)
    w = int(w)

    h = h/100
    bmi = w / (h * h)

    # Call function named func_bmi with argument
    # bmi is argument
    comment = func_bmi(bmi)

    output = "Your BMI is " + str(bmi) + " and my comment is " + comment
    # d = "walla walla bing bang, supercalifragilisticexpialidocious"

    txt3.insert('1.0', output)
    return


def func_bmi(bmi):
    if bmi >= 25:
        result = 'Hey, you are too fat Stop to eat!!'
    elif bmi >= 23 and bmi <25:
        result = "You are a little bit heavy, why don't you consider losing weight"
    elif bmi >=18.5 and bmi <23:
        result = 'Good for you, you are normal'
    else:
        result = 'You eat harder'

    return result


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
lbl0 = Label(root, text="Input Your Height", width=15)
lbl0.grid(row=0, column=0)
txt0 = Entry(root)
txt0.grid(row=0, column=1)

# Tkinter Row 1 - Label and Entry
lbl1 = Label(root, text="Input Your Weight", width=15)
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
