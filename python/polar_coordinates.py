import pandas as pd
import cmath
__author__ = 'annzhong'
# You are given a complex z. Your task is to convert it to polar coordinates.
data_str = input()
data = complex(data_str)
x = data.real
y = data.imag

phi = cmath.phase(data)
r = abs(data)

print(r)
print(phi)
