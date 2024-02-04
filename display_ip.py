import Adafruit_GPIO.SPI as SPI
import Adafruit_ILI9341 as ILI9341
from PIL import Image, ImageDraw, ImageFont

# Configurați conexiunea SPI
DC = 18
RST = 17
SPI_PORT = 0
SPI_DEVICE = 0

# Inițializați display-ul TFT
disp = ILI9341.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Creare de imagine goală
image = Image.new('RGB', (disp.width, disp.height))
draw = ImageDraw.Draw(image)

# Inițializați fontul și setați culoarea textului
font = ImageFont.load_default()
text_color = (255, 255, 255)

# Scrie "Hello" pe imagine
text = "Hello"
draw.text((10, 10), text, fill=text_color, font=font)

# Afișează imaginea pe display
disp.display(image)

# Așteptați câteva secunde înainte de a închide
input("Apasă Enter pentru a închide display-ul...")

# Eliberați resursele
disp.cleanup()