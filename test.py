import matplotlib.pyplot as plt
import numpy as np

a = float(input())
b = float(input())
c = float(input())
d = float(input())
pr = float(input())
k = 0
idx = 0
pr_e = 200
q_e = 100
prices_0 = []
prices_1 = []
products = []


def demand(p):
    return a - b * p


def supply(p):
    return c + d * p


if d > b:
    print('Модель с раскручивающейся спиралью')  # т.е.колебания растут
elif d == b:
    print('Модель с постоянными колебаниями')
else:
    print('Модель с закручивающейся спиралью')  # d<b колебания затухают

if pr == pr_e:
    print('Модель находится в равновесии')
    print(f'{k} циклов понаобится')
else:
    for i in range(0, 1000):
        prices_0.append(supply(pr))
        print(prices_0)
        idx = (idx + 1) % len(prices_0)
        print(idx)
        prices_1.append(demand(prices_0[idx]))
        k += 1
        if pr in prices_0 or prices_1:
            print('Модель находится в равновесии')
            print(f'{k} циклов понаобится')
            break
        else:
            continue
fig, ax = plt.subplots()
ax.set_xlabel('Q')
ax.set_ylabel('P')
