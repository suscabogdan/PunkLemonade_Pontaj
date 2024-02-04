import Adafruit_GPIO.SPI as SPI
import Adafruit_ILI9341 as ILI9341
import RPi.GPIO as GPIO

MISO = 22
LED = 2
SCK = 5
MOSI = 26
DC = 18
RESET = 17
CS = 7
SPI_PORT = 0
SPI_DEVICE = 0

def setupDisplay():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)
    GPIO.setup(DC, GPIO.OUT)
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.setup(CS, GPIO.OUT)

setupDisplay()
spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz = 64000000)
tft = ILI9341.ILI9341(DC, rst = RESET, spi = spi)

def showDisplay():
    tft.begin()
    tft.setRotation(1)
    tft.fillScreen(tft.color565(255, 0, 255))

showDisplay()