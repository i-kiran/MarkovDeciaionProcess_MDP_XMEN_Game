import random 

def rand():
	r = random.choice(['w','e','n','s'])
	return r

def randompolicy():
	p = []
	for i in range(5):
		policy = []	
		for j in range(5):
			policy.append(rand())
		p.append(policy)
	return p

def newpolicy():
	n_p = []
	for i in range(5):
		np = []
		for j in range(5):
			np.append(0)
		n_p.append(np)
	return n_p

