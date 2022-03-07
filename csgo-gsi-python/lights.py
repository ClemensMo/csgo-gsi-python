from rpi_ws281x import Color, PixelStrip, ws

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_BRG


# LED_STRIP = ws.SK6812W_STRIP

def set_flash_color(flash_value):
    c = Color(flash_value, flash_value, flash_value)
    for i in range(200, strip.numPixels()):
        strip.setPixelColor(i, c)
    strip.show()


def set_fire_color(fire_value):
    c = Color(int(255 * (255/fire_value)), 0, int(165 * (255/fire_value)))
    for i in range(200, strip.numPixels()):
        strip.setPixelColor(i, c)
    strip.show()


def set_base_color(r, b, g):
    c = Color(r, b, g)
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, c)
    strip.show()


def handle_light_events(flashed, health, bomb, fire, i):
    if flashed > 0:
        set_flash_color(flashed)
    elif fire > 0:
        set_fire_color(fire)
    elif health < 10:
        set_base_color(10, 0, 0)
    elif bomb == 'planted':
        if i % 20 < 10:
            set_base_color(60, 0, 30)
        else:
            set_base_color(60, 0, 0)
    else:
        set_base_color(10, 10, 10)


strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()
set_flash_color(0)
