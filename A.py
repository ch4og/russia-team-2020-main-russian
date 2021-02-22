k = int(input())
sd = 25
prk = k * 0.01
gg = sd + prk
if gg < 100:
	print('100.00')
elif gg > 2000:
	print('2000.00')
else:
	gg = str(gg) + '0'
	print(gg)