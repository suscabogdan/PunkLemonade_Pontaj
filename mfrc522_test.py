import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Hold a card near the reader")
    id = reader.read_id()
    print(f"Card ID: {id}")
finally:
    GPIO.cleanup()
