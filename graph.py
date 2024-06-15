import csv
import matplotlib.pyplot as plt
import datetime

# ファイルのパス
file_path = '/Users/hiromasa/Documents/open-university/ouj-python/temperature_data.csv'

# 日付と気温を格納するリスト
dates = []
temperatures = []

# CSVファイルを開いて読み込む
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        date_str = row[0]  # 日付の文字列
        temperature = float(row[1])  # 気温
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')  # 日付の文字列をdatetimeオブジェクトに変換
        dates.append(date)
        temperatures.append(temperature)

# グラフの描画
plt.figure(figsize=(10, 5))
plt.plot(dates, temperatures, marker='o')
plt.title('Temperature Over Time')
plt.xlabel('Date and Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.xticks(rotation=45)  # X軸のラベルを45度回転させる
plt.tight_layout()
# グラフを表示
plt.show()
