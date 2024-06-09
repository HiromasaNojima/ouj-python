import Adafruit_DHT
import time
import csv

# センサーの設定
sensor = Adafruit_DHT.DHT22
pin = 2

# センサーデータ取得関数
def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    return humidity, temperature

# ログデータ保存関数
def log_data(timestamp, temperature, humidity):
    with open('temperature_data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, humidity])

# メインループ
while True:
    humidity, temperature = get_sensor_data()
    if humidity is not None and temperature is not None:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        temperature_int = int(temperature)
        humidity_int = int(humidity)
        log_data(timestamp, temperature, humidity)
        print(f'Time: {timestamp}, Temperature: {temperature:.1f}C (int: {temperature_int}C), Humidity: {humidity:.1f}% (int: {humidity_int}%)')
    else:
        print('Failed to get reading. Try again!')
    time.sleep(60)  # 1分ごとにセンサーデータを取得
