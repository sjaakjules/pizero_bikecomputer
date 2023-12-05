from logger import app_logger

from .display_core import Display

_SENSOR_DISPLAY = False

try:
    import ST7789 as ST7789
    from PIL import Image

    _SENSOR_DISPLAY = True
except ImportError:
    pass

app_logger.info(f"Display HAT Mini RPi Display: {_SENSOR_DISPLAY}")

# ISP Display Module for Raspberry Pi 4B/3B+/Zero 2 W version 1.0
class DisplayHATMini(Display):
    # Display HAT Mini actually needs max brightness under sunlights, so there is no implementation of AUTO_BACKLIGHT
    # There's also only two states enabled or disabled
    brightness_index = 1  # we are on by default
    brightness_table = [0, 100]

    epaper = None

    has_color = False
    has_touch = False
    send = True

    size = (320, 240)

    def set_brightness(self, b):
        # Set brightness
        if b == 0:
            self.disp.set_backlight(GPIO.LOW)
        elif b == 100:
            self.disp.set_backlight(GPIO.HIGH)

    def __init__(self, config):
        super().__init__(config)

        # Initialize ST7789 LCD display class
        self.disp = ST7789.ST7789(
            height=240,
            width=320,
            rotation=180,
            port=0,
            cs=1,
            dc=9,
            backlight=13,
            spi_speed_hz=60 * 1000 * 1000,
            offset_left=0,
            offset_top=0
        )
        self.disp.begin()

    def clear(self):
        # Clear the screen. 
        self.disp.reset()

    def update(self, im_array, direct_update=False):
        # Update screen with the image array.
        self.disp.display(
            Image.frombytes(
                "1", (im_array.shape[1] * 8, im_array.shape[0]), (~im_array).tobytes()
            )
        )

    def quit(self):
        self.set_brightness(0)
        self.clear()
