import tkinter as tk
import tkinter.ttk as ttk
import typing

class InputField:
    def __init__(self, root : tk.Tk, title : str) -> None:
        #create widgets
        self.font = ("*Font", 13)
        self.colour = "#ffffff"
        self.textOrientation = "center"
        self.relWidth = 0.5
        self.var = tk.StringVar()
        self.check_frame = ttk.LabelFrame(root, text=title, padding=(5, 5))
        self.entry = tk.Entry(self.check_frame, font=self.font, relief="flat", fg=self.colour, justify=self.textOrientation, textvariable=self.var)

    def place(self, rely : float):
        self.check_frame.place(relx = 0.5, rely = rely, anchor = 'center', relwidth=self.relWidth)
        self.entry.pack()

    def destroy(self):
        self.check_frame.destroy()

    def get(self):
        return self.var.get()

    def colour(self, colour):
        self.entry.configure(fg=colour)
