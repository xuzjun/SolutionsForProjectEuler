# -*- coding: utf-8 -*-



if __name__ == '__main__':
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print('{} {} {}'.format(a, b, c))


