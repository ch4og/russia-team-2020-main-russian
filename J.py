n, m, s = map(int, input().split())
clearCards = list(map(int, input().split()))
clearCards.sort()
errors = 0
aaaaaaaa = 0



for i in range(2, s + 1):
	for _ in range(1, s + 1):
		if clearCards[i] - clearCards[i - 1] == _:
			for z in range(_):
				clearCards.append(i + z)


clearCards.sort()

for i in range(2, s + 1):
	if (clearCards[i] - clearCards[i - 1] == 1) or (clearCards[i] == clearCards[i - 1]):
		aaaaaaaa += 1
	else:
		errors += 1

	if errors >= s:
		break

print(aaaaaaaa)