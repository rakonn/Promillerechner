import tkinter as tk


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.wm_title(self, "Promillerechner")
        # tk.Tk.iconbitmap(self, "res/beer_3630.ico")
        # self.tk.call("source", "include/Azure-ttk-theme-main/azure.tcl")
        # self.tk.call("set_theme", "dark")
        # self.geometry("300x485")
        # self.resizable(False, False)

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        self.frames = {}

        for F in (Page1, Page2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.place(anchor="nw", relwidth=1, relheight=1)

        self.show_frame(Page1)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):
    def __init__(self, root, controller : Window) -> None:
        tk.Frame.__init__(self, root)
        
        #createPage

class Page2(tk.Frame):
    def __init__(self, root, controller : Window) -> None:

        tk.Frame.__init__(self, root)
    	
        #create page
        
    

def main():
    Window().mainloop()

if __name__ == "__main__":
    main()