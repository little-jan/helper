"""
mean squared error code
"""

def mse(actual, data):
    n = len(actual)
    current = 0
    for i in range(len(actual)):
        curr = float(actual[i]) - float(data[i])
        curr = curr ** 2
        current += curr
    meanse = current / n
    return meanse

def rmse(meanse):
    r = float(meanse) ** (1/2)
    return r

if __name__ == '__main__':
    actual = input().strip().split(' ')
    data = input().strip().split(' ')
    messmse = f"MSE = {mse(actual, data)}."
    print(messmse)
    messrmse = f"RMSE = {rmse(mse(actual, data))}."
    print(messrmse)