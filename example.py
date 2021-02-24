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
encrypted = Encryptor(alphabet, b, Xo,Ttrans,texto)
print(f"Mensagem encriptada: {encrypted}\n")


decrypted_exact = Decryptor(alphabet,b,Xo,Ttrans,encrypted)
print(f"Mensagem decriptada:\n{decrypted_exact}\n")

decrypted_intercepted = Decryptor(alphabet,b,Xo+1e-16,Ttrans,encrypted)
print(f"Mensagem decriptada+1e-16:\n{decrypted_intercepted}\n")
