def unique_chars(string1):
	set1 = ''.join(set(string1))
	out = []
	for char1 in set1:
		if string1.count(char1) == 1:
			out.append(char1)
	return out

print('Unique characters in anagram: ', unique_chars('anagram')) # test 1

print('Unique characters in AmrAtifFouda: ', unique_chars('amratiffouda')) # test 2