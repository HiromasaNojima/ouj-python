import csv

# ファイルのパス
file_path = './ouj-python/temperature_data.csv'
# 最大気温を格納する変数
max_temperature = float('-inf')
# 計算量をカウントする変数
order = 0 

# CSVファイルを開いて読み込む
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        temperature = float(row[1])
        order += 1
        
        # 現在の気温が最大気温より高ければ更新
        if temperature > max_temperature:
            max_temperature = temperature

# 最大気温を表示
print(f"最大気温は: {max_temperature}")
print(f"計算量: {order}")
