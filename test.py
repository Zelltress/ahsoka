import ru_local as ru
import matplotlib.pyplot as plt

a = float(input('функция вида QD = a-bp, где a - свободный член. (Количество людей, которые хотят купить данный товар) '))
b = float(input('функция вида QD = a-bp, где b - коэф. наклона (Он всегда отрицателен, поэтому запишите положительное число. т.е Если a - 6p, то запишите просто 6) '))
c = float(input('функция вида QS = c-dp, где c - свободный член. (Количество людей, которые хотят продавать данный товар) '))
t = float(input('функция вида QS = c-dp, где t - коэф. наклона (Он всегда положителен) '))
price = float(input())
prices = []
demands = []
supplies = []
i = 0 #счетчик

def demand(p):
    return a-b*p


def supply(p):
    return c+t*p

def main():
    price_e = (a-c)/(t+b)
    quantity_e = demand(price_e)

    print('Равновесная цена:', price_e, 'Равновесный объём:', quantity_e)

    if price == price_e:
        print('Модель находится в равновесии')

    else:
        print('Модель не находится в равновесии')

        if t == b:
            print('Модель с постоянными колебаниями')
            for j in range(2):
                demands.append(supply(price))
                price = (a - c - t*price)/b
                supplies.append(supply(price))
                prices.append(price)

        elif t > b:
            print('Модель с раскручивающейся спиралью')
            for k in range(5):
                demands.append(supply(price))
                price = (a - c - t*price)/b
                supplies.append(supply(price))
                prices.append(price)
        else:
            print('Модель с закручивающейся спиралью')
            while price != price_e:
                i += 1
                demands.append(supply(price))
                price = (a - c - t*price)/b
                supplies.append(supply(price))
                prices.append(price)

        print(i, 'цикла(ов) понадобится')

    plt.figure()
    plt.title('Паутинообразная модель динамики цен и объёма производства')
    plt.ylabel('Цена товара')
    plt.xlabel('Количество товара')
    plt.plot(demands, prices)
    plt.plot(supplies, prices)
    plt.scatter(demands, prices)
    plt.scatter(supplies, prices)

    for m in demands:
        for n in supplies:
            if m == n:
                plt.quiver(n, prices[supplies.index(n)], 0, prices[demands.index(m)]-prices[supplies.index(n)],
                       angles='xy', scale_units='xy', scale=1, width=0.005) #рисуем вектор
    for q in prices:
        plt.quiver(demands[prices.index(q)], q, supplies[prices.index(q)]-demands[prices.index(q)], 0,
               angles='xy', scale_units='xy', scale=1, width=0.005)
    plt.show()

if __name__ == '__main__':
    main()
