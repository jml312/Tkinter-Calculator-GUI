from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

# root
root = tk.ThemedTk()
root.get_themes()
root.set_theme('clam')
root.configure(bg='black')
root.geometry("380x550+850+200")
root.resizable(False, False)
root.title("Calculator")

# entry
entry_box = ttk.Entry(font='verdana 14 bold', width=30, justify=RIGHT, style='my.TEntry')
entry_box.insert(0, "O")
entry_box.place(x=20, y=10)

# buttons
b = ttk.Style()
b.configure('my.TButton', font='times 15 bold')
buttons = []


def enterNumber(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


for i in range(10):
    buttons.append(ttk.Button(width=6, text=str(i), style='my.TButton', command=lambda x=i: enterNumber(x)))

btn_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        buttons[btn_text].place(x=6 + j * 96, y=70 + i * 70)
        btn_text += 1

# operator buttons
btn_operator = []


def enterOperator(x):
    if entry_box.get() != 'O':
        length = len(entry_box.get())
        entry_box.insert(length, btn_operator[x]['text'])


for i in range(4):
    btn_operator.append(ttk.Button(width=6, style='my.TButton', command=lambda x=i: enterOperator(x)))

btn_operator[0]['text'] = "+"
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=290, y=70 + i * 70)

# zero button
btn_zero = ttk.Button(width=30, text='0', style='my.TButton', command=lambda x=0: enterNumber(x))
btn_zero.place(x=5, y=280)


# clear button
def funcClear():
    entry_box.delete(0, END)
    entry_box.insert(0, 'O')


btn_clear = ttk.Button(width=7, text='Clear', style='my.TButton', command=funcClear)
btn_clear.place(x=5, y=340)

# dot
btn_dot = ttk.Button(width=6, text='.', style='my.TButton', command=lambda x='.': enterNumber(x))
btn_dot.place(x=101, y=340)

result = 0
result_list = []


# equals
def funcOperator():
    content = entry_box.get()
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text='History : ' + ' | '.join(result_list[:5]))


btn_equals = ttk.Button(width=7, text='=', style='my.TButton', command=funcOperator)
btn_equals.place(x=189, y=340)


# delete
def funcDelete():
    length = len(entry_box.get())
    entry_box.delete((length - 1), 'end')
    if length == 1:
        entry_box.insert(0, 'O')


icon = PhotoImage(file='Icons/arrow.png', width=50)
btn_delete = ttk.Button(width=6, style='my.TButton', command=funcDelete, image=icon)
btn_delete.place(x=290, y=334)

# status bar
statusBar = Label(root, text='History : ', relief=SUNKEN, height=3, anchor=W, font='verdana 11 bold')
statusBar.pack(side=BOTTOM, fill=X)
root.mainloop()
