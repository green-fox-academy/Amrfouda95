def get_minTemp(values, years):
	minTemp = 1000
	year = 0
	for t ,y in zip(values,years):
		if t < minTemp:
			year = y
			minTemp = t
	return year, minTemp

def get_maxTemp(values, years):
	maxTemp = -1000
	year = 0
	for t,y in zip(values,years):
		if t > maxTemp:
			year = y
			maxTemp = t
	return year, maxTemp

def temp(fname):
	fs = open(fname, 'r')
	france = []
	sweden = []
	germany = []
	years = []
	for line in fs:
		dat = fs.readline().split(' ')
		print(dat)
		france.append(int(dat[0]))
		sweden.append(int(dat[1]))
		germany.append(int(dat[2]))
		years.append(int(dat[3]))
	fs.close()
	return france, sweden, germany, years

if __name__=="__main__":

	france, sweden, germany, years = temp('results.txt')
	print('France => %d, %d' %(get_minTemp(france, years)[0], get_maxTemp(france, years)[0]))
	print('Sweden => %d, %d' %(get_minTemp(sweden, years)[0], get_maxTemp(sweden, years)[0]))
	print('Germany => %d, %d' %(get_minTemp(germany, years)[0], get_maxTemp(germany, years)[0]))