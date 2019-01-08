# -*- coding: utf-8 -*-


if __name__ == '__main__':
    r = 0
    l = 0
    for th in range(0, 2):
        for h in range(0, 3):
            for f in range(0, 5):
                for t in range(0, 11):
                    for te in range(0, 21):
                        for ff in range(0, 41):
                            for tw in range(0, 101):
                                l = 0
                                for o in range(0, 201):
                                    l = 1 * o  + 2 * tw + 5 * ff + 10 * te + 20 * t + 50 * f + 100 * h + 200 * th
                                    if l == 200:
                                        r += 1
                                        #print('{} {} {} {} {} {} {} {}'.format(o, tw, ff, te, t, f, h, th))
                                        break

    print(r)
