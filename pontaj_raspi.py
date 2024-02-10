import tkinter as tk
from threading import Thread
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from helpers import afiseaza_mesaj, ids_nume
import time

def citire_nfc_continua(root, mesaj_var, reader):
    try:
        while True:
            id, text = reader.read_no_block()  # Încercăm citirea non-blocantă, dacă este disponibilă
            if id:
                print(f"ID citit: {id}")  # Pentru debugging
                root.after(0, lambda: afiseaza_mesaj(root, mesaj_var, str(id)))
                time.sleep(2)  # O pauză pentru a evita citiri multiple rapide
    finally:
        GPIO.cleanup()  # Curățăm pinii GPIO la final

def main():
    root = tk.Tk()
    root.geometry("800x480")
    root.configure(bg="black")
    mesaj_var = tk.StringVar(root, "Buna ziua!")
    mesaj_label = tk.Label(root, textvariable=mesaj_var, fg="white", bg="black", font=("Helvetica", 24))
    mesaj_label.pack(expand=True)

    reader = SimpleMFRC522()
    
    # Inițializăm și pornim thread-ul pentru citirea NFC
    thread_citire_nfc = Thread(target=citire_nfc_continua, args=(root, mesaj_var, reader))
    thread_citire_nfc.daemon = True  # Asigurăm că thread-ul se închide odată cu programul principal
    thread_citire_nfc.start()

    root.mainloop()

if __name__ == "__main__":
    main()
