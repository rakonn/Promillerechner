import tkinter as tk
import tkinter.ttk as ttk


class Utils:
    def calcAlcMass(volume: float, alcoholPercentage: float) -> float:
        return 10.0 * volume * alcoholPercentage

    def calcBloodAlc(massAlcohol: float, massPerson: float, reductionFactor: float) -> float:
        return massAlcohol / (massPerson * reductionFactor)

    def getReductionFactor(sortPerson: str) -> float:
        if sortPerson == "jugendlich":
            return 0.6
        elif sortPerson == "männlich":
            return 0.7
        elif sortPerson == "weiblich":
            return 0.6


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Promillerechner")
        tk.Tk.iconbitmap(self, "../res/beer_3630.ico")
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "dark")
        self.geometry("300x485")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (MainPage, ResultsPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.place(anchor="nw", relwidth=1, relheight=1)

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def setBloodAlc(self, alc):
        frame = self.frames[ResultsPage]
        frame.changeBloodAlc(alc)


class MainPage(tk.Frame):
    def __init__(self, root, controller: Window) -> None:
        tk.Frame.__init__(self, root)

        self.controller = controller
        self.createPage()

    def createPage(self):
        # Input 1
        self.volVar = tk.StringVar()
        self.check_frame = ttk.LabelFrame(
            self, text="Liter getrunken (l)", padding=(5, 5))
        self.volumeInput = tk.Entry(self.check_frame, font=(
            "*Font", 13), relief="flat", fg="#ffffff", justify="center", textvariable=self.volVar)
        self.check_frame.place(relx=0.5, rely=0.15,
                               anchor='center', relwidth=0.52)
        self.volumeInput.pack()

        # Input 2
        self.alcVar = tk.StringVar()
        self.check_frame = ttk.LabelFrame(
            self, text="Alkoholanteil (%)", padding=(5, 5))
        self.alcInput = tk.Entry(self.check_frame, font=(
            "*Font", 13), relief="flat", fg="#ffffff", justify="center", textvariable=self.alcVar)
        self.check_frame.place(relx=0.5, rely=0.32,
                               anchor='center', relwidth=0.52)
        self.alcInput.pack()

        # Input 3
        ttk.Entry().place(relx=0.5, rely=0.49, anchor='center', relwidth=0.52)
        # self.massVar = tk.StringVar()
        # self.check_frame = ttk.LabelFrame(
        #     self, text="Gewicht der Person (kg)", padding=(5, 5))
        # self.massInput = tk.Entry(self.check_frame, font=(
        #     "*Font", 13), relief="flat", fg="#ffffff", justify="center", textvariable=self.massVar)
        # self.check_frame.place(relx=0.5, rely=0.49,
        #                        anchor='center', relwidth=0.52)
        # self.massInput.pack()

        # Combobox
        self.cmb = ttk.Combobox(self, values=(
            "männlich", "weiblich", "jugendlich"), state="readonly")
        self.cmb.current(0)
        self.cmb.place(relx=0.5, rely=0.66, anchor='center',
                       relwidth=0.4, relheight=0.07)

        # Buttion
        self.button = ttk.Button(
            self, text="Berechnen...", style="Accent.TButton", command=self.manageInputs)
        self.button.place(relx=0.5, rely=0.85, anchor='center',
                          relwidth=0.52, relheight=0.1)

    def manageInputs(self):
        goOn = True
        try:
            volumeDrank = float(self.volVar.get())
            self.volumeInput["fg"] = "#ffffff"
        except ValueError:
            self.volumeInput["fg"] = "red"
            goOn = False

        try:
            alcoholPercentage = float(self.alcVar.get())
            self.alcInput["fg"] = "#ffffff"
            if alcoholPercentage > 100.00:
                raise ValueError()
        except ValueError:
            self.alcInput["fg"] = "red"
            goOn = False

        try:
            massPerson = float(self.massVar.get())
            self.massInput["fg"] = "#ffffff"
        except ValueError:
            self.massInput["fg"] = "red"
            goOn = False

        sortPerson = self.cmb.get()

        if not goOn:
            return

        reductionFactor = Utils.getReductionFactor(sortPerson)
        massAlcohol = Utils.calcAlcMass(volumeDrank, alcoholPercentage)
        bloodAlcohol = round(Utils.calcBloodAlc(
            massAlcohol, massPerson, reductionFactor), 6)

        self.controller.setBloodAlc(bloodAlcohol)
        self.controller.show_frame(ResultsPage)


class ResultsPage(tk.Frame):
    def __init__(self, root, controller: Window) -> None:

        tk.Frame.__init__(self, root)

        self.controller = controller
        self.bloodAlcohol = 0
        self.createPage()

    def createPage(self):
        tk.Label(self, text="Der Blutalkoholspiegel beträgt ungefähr", justify="center", font=(
            "*Font", 13), wraplength=230).place(relx=0.52, rely=0.15, anchor='center')

        self.alcLabel = tk.Label(self, text="", justify="center", font=(
            "*Font", 14), wraplength=220, fg="#369aff")
        self.alcLabel.place(relx=0.5, rely=0.3, anchor='center')

        self.button = ttk.Button(
            self, text="Zurück", command=lambda: self.controller.show_frame(MainPage))
        self.button.place(relx=0.5, rely=0.85, anchor='center',
                          relwidth=0.52, relheight=0.1)

    def changeBloodAlc(self, alc):
        self.alcLabel["text"] = f"{alc} ‰"


def main():
    Window().mainloop()


if __name__ == "__main__":
    main()
