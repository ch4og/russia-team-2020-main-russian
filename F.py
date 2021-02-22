t, v = map(int, input().split())
t1, v1 = map(int, input().split())
if t1 < 0 and v1 >= 10:
	print('A storm warning for tomorrow! Be careful and stay home if possible!')
elif t1 < t:
	print('MCHS warns! Low temperature is expected tomorrow.')
elif v1 > v:
	print('MCHS warns! Strong wind is expected tomorrow.')
else:
	print('No message')