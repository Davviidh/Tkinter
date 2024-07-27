def say_hello():
    print ("Hello")
def add_label():
    label = tk.Label(win, text = "new")
    label.pack()
def counter():
    global count
    count += 1
    btn4['text'] = f'Counter {count}'
    btn1['state'] = tk.NORMAL
    btn2['state'] = tk.NORMAL
    if count % 2 == 1:
        btn1['state'] = tk.DISABLED
    else:
        btn2['state'] = tk.DISABLED
count = 0

import tkinter as tk

win = tk.Tk()
win.geometry("400x500+100+200")
win.title('Barev')

btn1 = tk.Button(win, text='Hello',
                command= say_hello)
btn2 = tk.Button(win, text='add_label',
                command= add_label)
btn3 = tk.Button(win, text='add_label lambda',
                command= lambda: tk.Label(win, text = "new").pack()
                )
btn4 = tk.Button(win, text = f'Counter {count}',
                 command = counter,
                 bg = 'red',
                )
btn1.pack() 
btn2.pack()
btn3.pack()
btn4.pack()


win.mainloop()