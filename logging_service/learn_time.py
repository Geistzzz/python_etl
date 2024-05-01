import time

"2020-10-20 16:18:30"  # 字符串类型

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strptime("2020-10-20 16:18:30", "%Y-%m-%d %H:%M:%S"))
