import tkinter as tk
from tkinter.constants import RADIOBUTTON
import tkinter.ttk as ttk
import pathlib, os


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


class App(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, width=300, height=485)

        self.frames = {}

        for F in (MainPage, ResultsPage):

            frame = F(self)

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
    def __init__(self, root) -> None:
        tk.Frame.__init__(self, root)

        self.root = root
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
        self.massVar = tk.StringVar()
        self.check_frame = ttk.LabelFrame(
            self, text="Gewicht der Person (kg)", padding=(5, 5))
        self.massInput = tk.Entry(self.check_frame, font=(
            "*Font", 13), relief="flat", fg="#ffffff", justify="center", textvariable=self.massVar)
        self.check_frame.place(relx=0.5, rely=0.49,
                               anchor='center', relwidth=0.52)
        self.massInput.pack()

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
            volumeDrank = float(self.volVar.get().replace(",", "."))
            self.volumeInput["fg"] = "#ffffff"
        except ValueError:
            self.volumeInput["fg"] = "red"
            goOn = False

        try:
            alcoholPercentage = float(self.alcVar.get().replace(",", "."))
            self.alcInput["fg"] = "#ffffff"
            if alcoholPercentage > 100.00:
                raise ValueError()
        except ValueError:
            self.alcInput["fg"] = "red"
            goOn = False

        try:
            massPerson = float(self.massVar.get().replace(",", "."))
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
            massAlcohol, massPerson, reductionFactor), 3)

        self.root.setBloodAlc(bloodAlcohol)
        self.root.show_frame(ResultsPage)


class ResultsPage(tk.Frame):
    def __init__(self, root) -> None:
        tk.Frame.__init__(self, root)

        self.root = root
        self.bloodAlcohol = 0
        self.createPage()

    def createPage(self):
        tk.Label(self, text="Der Blutalkoholspiegel beträgt ungefähr", justify="center", font=(
            "*Font", 13), wraplength=230).place(relx=0.52, rely=0.15, anchor='center')

        self.alcLabel = tk.Label(self, text="", justify="center", font=(
            "*Font", 14), wraplength=220, fg="#369aff")
        self.alcLabel.place(relx=0.5, rely=0.3, anchor='center')

        self.button = ttk.Button(
            self, text="Zurück", command=lambda: self.root.show_frame(MainPage))
        self.button.place(relx=0.5, rely=0.85, anchor='center',
                          relwidth=0.52, relheight=0.1)

    def changeBloodAlc(self, alc):
        self.alcLabel["text"] = f"{alc} ‰"


def main():
    root = tk.Tk()
    root.title("Promillerechner")
    root.geometry("300x485")
    root.iconbitmap("res\\beer_3630.ico")
    root.resizable(False, False)

    # set the theme
    themeFilename = "azure.tcl"
    currentDir = pathlib.Path(__file__).parent.resolve()
    themePath = os.path.join(currentDir, themeFilename)
    root.tk.call(
        "source", themePath)
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    # root.update()
    # root.minsize(root.winfo_width(), root.winfo_height())
    # x_cordinate = int((root.winfo_screenwidth() / 2) -
    #                   (root.winfo_width() / 2))
    # y_cordinate = int((root.winfo_screenheight() / 2) -
    #                   (root.winfo_height() / 2))
    # root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()


if __name__ == "__main__":
    main()
