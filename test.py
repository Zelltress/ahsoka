# Part of case-study #2: Microeconomics
# Developers: Ivanova A., Gulakova Y., Ilyinykh T., Cherkashina D.

import ru_local as ru
import matplotlib.pyplot as plt

a = float(input(ru.NUMBER_CUSTOMERS))
b = float(input(ru.DEMAND_SLOPE_COEFF))
c = float(input(ru.NUMBER_SELLERS))
t = float(input(ru.SUPPLY_SLOPE_COEFF))

prices = []
demands = []
supplies = []


def demand(p):
    return a - b * p


def supply(p):
    return c + t * p


def main():
    price = float(input(ru.INITIAL_PRICE))
    i = 0

    price_e = (a - c) / (t + b)
    quantity_e = demand(price_e)

    print(ru.EQUILIBRIUM_PRICE, price_e, ru.EQUILIBRIUM_VOLUME, quantity_e)

    if price == price_e:
        print(ru.BALANCE_MODEL)

    else:
        print(ru.IMBALANCE_MODEL)

        if t == b:
            print(ru.CONSTANT_CYCLE)
            for j in range(2):
                demands.append(supply(price))
                price = (a - c - t * price) / b
                supplies.append(supply(price))
                prices.append(price)

        elif t > b:
            print(ru.UNWINDING_SPIRAL)
            for k in range(5):
                demands.append(supply(price))
                price = (a - c - t * price) / b
                supplies.append(supply(price))
                prices.append(price)
        else:
            print(ru.TWISTING_SPIRAL)
            while price != price_e:
                i += 1
                demands.append(supply(price))
                price = (a - c - t * price) / b
                supplies.append(supply(price))
                prices.append(price)

        print(i, ru.NUMBER_CYCLES)

    plt.figure()
    plt.title(ru.MODEL_NAME)
    plt.ylabel(ru.PRODUCT_PRICE)
    plt.xlabel(ru.PRODUCT_NUMBER)
    plt.plot(demands, prices)
    plt.plot(supplies, prices)
    plt.scatter(demands, prices)
    plt.scatter(supplies, prices)

    for m in demands:
        for n in supplies:
            if m == n:
                plt.quiver(n, prices[supplies.index(n)], 0, prices[demands.index(m)] - prices[supplies.index(n)],
                           angles='xy', scale_units='xy', scale=1, width=0.005)  # рисуем вектор
    for q in prices:
        plt.quiver(demands[prices.index(q)], q, supplies[prices.index(q)] - demands[prices.index(q)], 0,
                   angles='xy', scale_units='xy', scale=1, width=0.005)
    plt.show()


if __name__ == '__main__':
    main()
