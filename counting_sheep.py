
T = int(input())
for i in range(1,T+1):
	N = int(input())
	set={int(str(N)[0])}
	bool = False
	_N=N
	if(N==0):
		print("Case #"+str(i)+": INSOMNIA")
		bool = True

	while(bool == False):
		for x in str(N):
			set.add(int(x))
		if(len(set)==10):
			print("Case #"+str(i)+": "+str(N))
			bool = True
		N+=_N


