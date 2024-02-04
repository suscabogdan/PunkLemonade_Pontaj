import threading
from pontaj import read_nfc
from flask_app import start_flask_app

# Creează un thread pentru cititorul NFC
nfc_thread = threading.Thread(target=read_nfc)

# Creează un thread pentru Flask
flask_thread = threading.Thread(target=start_flask_app)

# Porneste thread-urile
nfc_thread.start()
flask_thread.start()

# Așteaptă ca ambele thread-uri să se finalizeze (opțional)
nfc_thread.join()
flask_thread.join()
