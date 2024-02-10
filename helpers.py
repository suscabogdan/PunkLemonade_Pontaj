import tkinter as tk

# Dicționar pentru ID-uri și nume
ids_nume = {
    "1": "Demi",
    "2": "Matia",
    "3": "Bogdan",
}

def afiseaza_mesaj(root, mesaj_var, id=None):
    if id and id in ids_nume:
        mesaj_var.set(f"Salut {ids_nume[id]}!")
        root.after(2000, lambda: mesaj_var.set("Buna ziua!"))
    else:
        mesaj_var.set("Buna ziua!")
