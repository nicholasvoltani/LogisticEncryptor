import string
from funcs import *

#######################################################################################
# b = 3.7 is in the chaotic regime
# left, right = 0.25668751333174394, 0.9249999957609717

b = 3.7
Ttrans = 500
T = 10000

#########################################################################################
arquivo = input("Qual arquivo encriptar? ")
with open(arquivo,'r') as lido:
    texto = lido.read()

alphabet = ImportAlphabet()
#########################################################################################

Xo = 0.70

#print(f"Mensagem original: \n{listToString(allstar)}\n")
encrypted = Encryptor(alphabet, b, Xo,texto, Ttrans = Ttrans, T = T)
print(f"Mensagem encriptada: {encrypted}\n")


decrypted_exact = Decryptor(alphabet,b,Xo,encrypted, Ttrans = Ttrans, T = T)
print(f"Mensagem decriptada:\n{decrypted_exact}\n")

decrypted_intercepted = Decryptor(alphabet,b,Xo+1e-16, encrypted, Ttrans = Ttrans, T = T)
print(f"Mensagem decriptada+1e-16:\n{decrypted_intercepted}\n")
