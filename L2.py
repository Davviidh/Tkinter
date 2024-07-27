import tkinter as tk

win = tk.Tk()
win.geometry("300x400+100+200")
win.title("Barev")

label_1 = tk.Label(win, text = '''Hello!
World''',
                   bg = 'red',
                   fg = 'white',
                #    font = ('')
                    # padx = 20,
                    # pady = 40,
                    width = 20,
                    height = 40,
                    anchor="n",
                    relief = tk.RAISED,
                    bd = 10,
                    justify=tk.LEFT,


                   )
label_1.pack()


win.mainloop()