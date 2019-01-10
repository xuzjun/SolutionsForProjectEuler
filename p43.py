# -*- coding: utf-8 -*-


if __name__ == '__main__':
	s = 0
	for one in range(1, 10):
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
									   or eight == one:
										continue
									for nine in range(10):
										if nine == eight or nine == seven \
										   or nine == six or  nine == five \
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
											if (two * 100 + three * 10 + four) % 2 == 0 \
												and (three * 100 + four * 10 + five) % 3 == 0 \
												and (four * 100 + five * 10 + six) % 5 == 0 \
												and (five * 100 + six * 10 + seven) % 7 == 0 \
												and (six * 100 + seven * 10 + eight) % 11 == 0 \
												and (seven * 100 + eight * 10 + nine) % 13 == 0 \
												and (eight * 100 + nine * 10 + ten) % 17 == 0:
												s += one * 1000000000 + two * 100000000 + three * 10000000 + four * 1000000 + five * 100000 + six * 10000 + seven * 1000 + eight * 100 + nine * 10 + ten * 1

	print(s)
