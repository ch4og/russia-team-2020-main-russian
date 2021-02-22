months = int(input())

def check(mama):
	st = str(mama)
	uniq = list((set(st)))
	uniq.sort()
	maxChars = 0

	for char in uniq:
		a = st.count(char)
		if a > maxChars:
			maxChars = a
			break


	return maxChars

for month in range(months):
	x = -1
	fr, to = map(int, input().split())
	some = 0
	for CHISLO in range(to, fr + 1, -1):
		pov = check(CHISLO)

		if pov != 0:
			some += 1
			if pov > x:
				x = pov

	some = 0

	for CHISLO in range(to, fr + 1, -1):
		pov = check(CHISLO)
		if pov == x:
			some += 1

	print(x, some)