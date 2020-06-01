from tkinter import *
from tkinter import ttk

root = Tk()
progbar = ttk.Progressbar(root,orient=HORIZONTAL,length=200)
progbar.pack(pady=20)
progbar.config(mode='indeterminate')
progbar.start()
progbar.stop()
progbar.config(mode='determinate',maximum=50.0,value=10)
progbar.start()
progbar.stop()
value = DoubleVar()
progbar.config(variable=value)
scale = ttk.Scale(root, orient=HORIZONTAL,length=200,var=value,from_=0.0,to_=50.0)
scale.pack()

root.geometry("450x450+650+350")
root.mainloop()

