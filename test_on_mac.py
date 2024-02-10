import tkinter as tk
from helpers import afiseaza_mesaj, ids_nume

def simulare_scanare(root, mesaj_var):
    root.bind("<Key>", lambda event: afiseaza_mesaj(root, mesaj_var, event.char))

def main():
    root = tk.Tk()
    root.geometry("800x480")
    root.configure(bg="black")
    mesaj_var = tk.StringVar(root, "Buna ziua!")
    mesaj_label = tk.Label(root, textvariable=mesaj_var, fg="white", bg="black", font=("Helvetica", 24))
    mesaj_label.pack(expand=True)

    simulare_scanare(root, mesaj_var)
    root.mainloop()

if __name__ == "__main__":
    main()
