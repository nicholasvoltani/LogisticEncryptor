import string
import random

def Logistic(b,x):
	return b*x*(1-x)

def listToString(lst):
	string = ''

	for l in lst:
		string += l

	return string

def ImportAlphabet():
	alphabet = list(string.ascii_letters)
	punctuation = string.punctuation
	alphabet += list(punctuation)
	alphabet.append(" ")
	alphabet.append('\n')
	## PT letters
	alphabet.append("à")
	alphabet.append("â")
	alphabet.append('ã')
	alphabet.append('á')
	alphabet.append('é')
	alphabet.append('ê')
	alphabet.append("Í")
	alphabet.append('í')
	alphabet.append('ó')
	alphabet.append('ô')
	alphabet.append('ú')
	alphabet.append("ç")
	## Numbers
	alphabet = alphabet + list(map(str,list(range(10))))

	return alphabet


def ChaoticAttractor(b,Ttrans=500,T=2000):
	'''
	Iterates the logistic equation $X_{n+1} = b*X_n*(1-X_n)$, firstly for Ttrans iterations, and then for T further iterations.
	'''
	xn = random.random()
	left = 1
	right = 0
	## Removing the transient
	for _ in range(Ttrans):
		xn = Logistic(b,xn)
	## Analyzing the stationary 
	chaoticAttractor = []
	for _ in range(T):
		xn = Logistic(b,xn)
		if xn < left:
			left = xn
		if xn > right:
			right = xn

	return left, right


def IsInInterval(alphabet, x, left,right, n):
	'''
	Checks whether x is in the n-th interval of (left,right), induced by the alphabet.
	We have to check whether x in (left + n*epsilon, left + (n+1)*epsilon),
	where epsilon = (right-left)/len(alphabet). 
	Checking for this is equivalent to saying that x <=> alphabet[n], i.e. x encrypts the n-th letter of the alphabet.
	'''
	epsilon = (right-left)/len(alphabet)
	Left = left + n*epsilon
	Right = Left + epsilon
	return Left<x<Right

def Encryptor(alphabet, b, Xo, Ttrans, message, eta = 0, T = 2000):
	'''
	Given an alphabet, a chaotic logistic parameter b, an interval (left,right) of the chaotic attractor defined by b, 
	some transient time Ttrans, and an initial condition Xo,
	one can encrypt a message by assigning each letter to some interval of the chaotic attractor,
	partitioned into len(alphabet) equally-sized intervals.
	
	A letter p_i is assigned to some number c_i, which will be the first integer such that
	F^{c_i}(X^{i-1}_o) will be in the p_i-th interval of the chaotic attractor.
	
	c_1 => X^1_o = F^{c_1}(Xo) is in the interval assigned to the letter c_1;
	c_2 => F^{c_2}(X^1_o) is in the interval assigned to the letter c_2, etc.

	Eta is in the interval [0,1). If eta != 0, then for each encrypted letter p_n, we get a random.random() number K in [0,1)
	and only accept c^{(m=0)}_n to encrypt p_n if K > eta; else, we keep iterating until we come to
	p_n's interval again, and repeat the process for m=1, m=2, ..., until K > eta, in which case c^{(m)}_n encrypts p_n.

	Returns a list of the encrypting ciphers.
	'''
	msg = list(message)
	left,right = ChaoticAttractor(b, Ttrans=Ttrans, T = T)

	xn = Xo
	## Removing the transient,
	## to ensure that xn's will be within the attractor
	for _ in range(Ttrans):
		xn = Logistic(b,xn)
		
	num_alphabet = list(range(len(alphabet))) ## Associate numbers to each letter in the alphabet
	encrypted = []  ## To-be-encrypted message

	## After removing the transient, we count how many Logistic applications
	## it takes to take X^i_0 to the p_i-th interval of the attractor
	for p in msg:
		count = 0
		xn = Logistic(b,xn)
		count += 1
		
		## Iterate xn until it falls in p's interval 
		## (and, optionally, if randomly-chosen k >= eta)
		while True:
			if IsInInterval(alphabet,xn,left,right, alphabet.index(p)):
				
				## If xn is in p's interval, generate k
				k = random.random()
				## If k >= eta, we consider the current interval, and write down its count
				if k >= eta:
					break
			## Else, keep iterating
			xn = Logistic(b,xn)
			count += 1

		## Write down the letter p's logistic iterate
		encrypted.append(count)

	return encrypted

def Decryptor(alphabet, b, Xo, Ttrans, encrypted, T = 2000):
	'''
	Given an alphabet, a chaotic logistic parameter b, an interval (left,right) of the chaotic attractor defined by b, 
	some transient time Ttrans, and an initial condition Xo, 
	one can dencrypt a message by iterating Xo and assigning each number in the encrypted message
	to its corresponding letter in the alphabet.
	
	Returns the decrypted string.
	'''
	left,right=ChaoticAttractor(b,Ttrans=Ttrans, T = T)
	## Removing the transient
	xn = Xo
	for _ in range(Ttrans):
		xn = Logistic(b,xn)
	
	num_alphabet = list(range(len(alphabet))) ## Associate numbers to each letter in the alphabet
	retrieved = []

	for e in encrypted:
		
		## Iterate 'e' times
		for k in range(e):
			xn = Logistic(b,xn)

		for n in num_alphabet:
			if IsInInterval(alphabet, xn, left,right,n):
				retrieved.append(alphabet[n])
				break

	decrypted = listToString(retrieved)
	return decrypted
