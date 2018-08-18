import sys

def roots(a, b, c):
    if a != 0:
        x1 = int((-b + (b ** 2 - 4 * a *c ) ** 0.5) / (2 * a))
        x2 = int((-b - (b ** 2 - 4 * a *c ) ** 0.5) / (2 * a))
        print(f'{x1}' + '\n' + f'{x2}')
    else:
        "Уравненеие не является 'квадратным'"

if __name__ == '__main__':
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    roots(a, b, c)