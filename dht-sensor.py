import dht
from machine import Pin
import time

# Define the pin connected to the DHT22 sensor
dht_pin = Pin(4, Pin.IN)  # Assuming DHT22 sensor is connected to GPIO 4

# Initialize the DHT sensor
dht_sensor = dht.DHT22(dht_pin)

# Function to read temperature and humidity from DHT22 sensor
def read_dht22_data():
    try:
        dht_sensor.measure()  # Perform a measurement
        temperature = dht_sensor.temperature()  # Get temperature reading in Celsius
        humidity = dht_sensor.humidity()  # Get humidity reading in percentage
        return temperature, humidity
    except Exception as e:
        print("Error reading DHT22:", e)
        return None, None

# Main loop
while True:
    temperature, humidity = read_dht22_data()
    if temperature is not None and humidity is not None:
        print("Temperature: {:.1f} °C, Humidity: {:.1f} %".format(temperature, humidity))
    else:
        print("Failed to read DHT22 data.")
    time.sleep(2)  # Wait for 2 seconds before next reading