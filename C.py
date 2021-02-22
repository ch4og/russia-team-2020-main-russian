t = int(input())
for i in range(t):
	n = int(input())
	mnp = list(map(int, input().split()))
	mp = list(map(int, input().split()))
	for i in range(len(mp)):
		if mnp[i] == 1:
			mnp[i] = 0
		elif mnp[i] <= mp[i] * 2:
			
