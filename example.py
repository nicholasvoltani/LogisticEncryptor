import string
from funcs import *

#######################################################################################
# b = 3.7 is in the chaotic regime
# left, right = 0.25668751333174394, 0.9249999957609717

b = 3.7
Ttrans = 500
T = 3000
xn = 0.6 ## Initial point
for _ in range(Ttrans):
	xn = Logistic(b,xn)
chaoticAttractor = []
for _ in range(T):
	xn = Logistic(b,xn)
	chaoticAttractor.append(xn)

left,right = min(chaoticAttractor), max(chaoticAttractor)

#########################################################################################
arquivo = input("Qual texto encriptar? ")
lido = open(arquivo,'r')
texto = lido.read()
#allstar = list(allstar)

alphabet = list(string.ascii_letters)
punctuation = string.punctuation
alphabet += list(punctuation)
alphabet.append(" ")
alphabet.append('\n')
alphabet.append("à")
alphabet.append("â")
alphabet.append('ã')
alphabet.append('á')
alphabet.append('í')
alphabet.append("ç")
alphabet.append('é')
alphabet.append('ê')
alphabet.append("Í")
alphabet.append('ó')
alphabet.append('ô')
alphabet.append('ú')

alphabet = alphabet + list(map(str,list(range(10))))
#########################################################################################

Xo = 0.70

#print(f"Mensagem original: \n{listToString(allstar)}\n")
encrypted = Encryptor(alphabet, b, Xo,Ttrans,texto)
#print(f"Mensagem encriptada: {encrypted}\n")

decrypted_exact = Decryptor(alphabet,b,Xo,Ttrans,encrypted)
print(f"Mensagem decriptada:\n{decrypted_exact}\n")

decrypted_intercepted = Decryptor(alphabet,b,Xo+1e-16,Ttrans,encrypted)
print(f"Mensagem decriptada+1e-16:\n{decrypted_intercepted}\n")
