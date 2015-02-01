limit = 4000000
sum = 0

term1 = 1
term2 = 1
temp = 0

while term2 < limit:
	if term2 % 2 == 0:
		sum += term2
	temp = term1
	term1 = term2
	term2 += temp

print sum