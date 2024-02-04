import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

def log_id(id):
    with open("/home/punklemonade/Desktop/Pontaj/pontaj_output.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Card ID: {id}\n")

def read_nfc():
    reader = SimpleMFRC522()

    try:
        while True:
            print("Hold a card near the reader")
            id = reader.read_id()
            print(f"Card ID: {id}")
            log_id(id)
            time.sleep(3)  # 3-second delay between reads

    except KeyboardInterrupt:
        print("NFC reading stopped.")
        GPIO.cleanup()

# Allow the script to be run standalone
if __name__ == "__main__":
    read_nfc()
