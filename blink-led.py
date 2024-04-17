from machine import Pin
import time

# Define the pin connected to the LED
led_pin = Pin(2, Pin.OUT)  # Assuming LED is connected to GPIO 2

# Function to blink the LED
def blink_led(interval, repetitions):
    for _ in range(repetitions):
        led_pin.on()  # Turn on the LED
        time.sleep(interval)  # Wait for interval seconds
        led_pin.off()  # Turn off the LED
        time.sleep(interval)  # Wait for interval seconds

# Set the interval and repetitions
blink_interval = 0.5  # Blink interval in seconds
blink_repetitions = 10  # Number of times to blink

# Blink the LED
blink_led(blink_interval, blink_repetitions)