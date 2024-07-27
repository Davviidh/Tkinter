import tkinter as tk

win = tk.Tk()
# photo = tk.PhotoImage(file = "aa.png")
# win.iconphoto(False, photo)
win.config(bg = "blue")
# win.config(bg = "#....")
win.title("Barev")
win.geometry("500x600+100+100")
win.resizable(True, True)
win.minsize(300, 400)
win.maxsize(700, 800)

win.mainloop()