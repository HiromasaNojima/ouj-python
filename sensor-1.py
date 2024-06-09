import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22
pin = 2

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    return humidity, temperature

humidity, temperature = get_sensor_data()
if humidity is not None and temperature is not None:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'Time: {timestamp}, Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%')
    temperature_int = int(temperature)
    humidity_int = int(humidity)
    print(f'Time: {timestamp}, Temperature: {temperature_int}C, Humidity: {humidity_int}%')
else:
    print('Failed to get reading. Try again!')
