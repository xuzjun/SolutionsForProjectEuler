# -*- coding: utf-8 -*-
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



if __name__ == '__main__':
    c = 0
    for one in range(10):
        for two in range(10):
            if two == one:
                continue
            for three in range(10):
                if three == two or three == one:
                    continue
                for four in range(10):
                    if four == three or four == two \
                       or four == one:
                        continue
                    for five in range(10):
                        if five == four or five == three \
                           or five == two or five == one:
                            continue
                        for six in range(10):
                            if six == five or six == four \
                               or six == three or six == two \
                               or six == one:
                                continue
                            for seven in range(10):
                                if seven == six or seven == five \
                                   or seven == four or seven == three \
                                   or seven == two or seven == one:
                                    continue
                                for eight in range(10):
                                    if eight == seven or eight == six \
                                       or eight == five or eight == four \
                                       or eight == three or eight == two \
                                       or eight == one: \
                                        continue
                                    for nine in range(10):
                                        if nine == eight or nine == seven \
                                           or nine == six or nine == five \
                                           or nine == four or nine == three \
                                           or nine == two or nine == one:
                                            continue
                                        for ten in range(10):
                                            if ten == nine or ten == eight \
                                               or ten == seven or ten == six \
                                               or ten == five or ten == four \
                                               or ten == three or ten == two \
                                               or ten == one:
                                                continue
                                            c += 1
                                            print('{} {} {} {} {} {} {} {} {} {}'.format(one, two, three, four, five, six, seven, eight, nine, ten))
                                            if c == 1000000:
                                                print(one * 1000000000 + two * 10000000 + three * 10000000 + four * 1000000 + five * 100000 + six * 10000 + seven * 1000 + eight * 100 + nine * 10 + ten)
                                                exit()
