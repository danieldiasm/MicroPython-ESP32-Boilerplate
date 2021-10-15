from neopixel import NeoPixel as neo_pixel

# TODO Make this become Object Oriented

state_led = neo_pixel(pin(27), 1)

def colour(colour: tuple):
    global state_led
    state_led[0] = colour
    state_led.write()
    return