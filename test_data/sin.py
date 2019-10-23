import numpy as np
import matplotlib.pyplot as plt

# CounterPeriod
resolution = 2303
s = 0
# 周波数決定係数
interval = 1

# グラフ作成用
x = range(resolution)
y = []

i = 0
print("{")
while s < resolution:
	val = round((1 + np.sin((((360.0/resolution)*int(i))*np.pi)/180.0)) * (resolution / 2.0), 0)
	print(int(val), end=",\n")
	y.append(val)
	i += interval
	s += 1
print("};")
plt.plot(x, y, label="base_sin")
plt.grid()

plt.show()
