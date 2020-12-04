# LogisticEncryptor

## A cryptography method based on the logistic equation

I wrote this program totally inspired on Baptista's article "Cryptography with Chaos", in which the author suggests a cryptographic method using the logistic equation. It is very interesting, since it takes full advantage of this equation's chaotic behavior (sensitivity on initial conditions) for security implementations.

However, it isn't a completely independent cryptographic method, as it relies on sending, alongside the encrypted message, the initial conditions (keys) used for the encryption, which would require some other (independent) form of cryptography. Still, an interesting read, and proposal, regardless.

A more detailed explanation on the algorithm is given in LogisticEncryptor.pdf, as well as in the original paper referenced below.

## Encryption #1

* Original message:

Estranho seria se eu não me apaixonasse por você
O sal viria doce para os novos lábios
Colombo procurou as Índias mas a Terra avisto em você
O som que eu ouço são as gírias do seu vocabulário
Estranho é gostar tanto do seu All Star azul
Estranho é pensar que o bairro das Laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
Continuar aquela conversa
Que não terminamos ontem, ficou pra hoje
Estranho, mas já me sinto como um velho amigo seu
Seu All star azul combina com o meu, preto, de cano alto
Se o homem já pisou na Lua, como ainda não tenho seu endereço
O tom que eu canto as minhas músicas na sua voz parece exato
Estranho é gostar tanto do seu All Star azul
Estranho é pensar que o bairro das Laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
Continuar aquela conversa
Que não terminamos ontem, ficou nas laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
E continuar aquela conversa
Que não terminamos ontem, ficou pra hoje, hoje, hoje


* Encrypted Message with keys b = 3.7, Xo = 0.7, No = 500

[243, 193, 505, 157, 82, 210, 32, 80, 84, 171, 231, 282, 177, 10, 36, 1013, 112, 30, 5, 8, 69, 264, 40, 52, 123, 272, 35, 63, 55, 7, 4, 108, 244, 72, 460, 65, 337, 727, 156, 74, 265, 141, 463, 29, 140, 75, 170, 33, 85, 120, 13, 81, 10, 19, 17, 59, 90, 6, 365, 10, 52, 5, 302, 49, 136, 23, 75, 4, 354, 14, 99, 677, 130, 67, 73, 155, 594, 119, 400, 47, 246, 29, 291, 194, 85, 718, 21, 70, 115, 53, 198, 22, 4, 235, 62, 158, 102, 51, 246, 425, 18, 99, 129, 38, 39, 580, 45, 184, 111, 31, 156, 39, 125, 205, 262, 30, 545, 71, 13, 74, 275, 133, 86, 114, 18, 12, 18, 125, 32, 10, 198, 185, 15, 60, 120, 38, 450, 216, 56, 107, 112, 415, 44, 69, 121, 299, 44, 160, 70, 82, 91, 34, 41, 104, 352, 347, 5, 13, 515, 53, 21, 3, 117, 56, 195, 146, 82, 110, 60, 84, 36, 62, 5, 119, 117, 94, 53, 101, 38, 53, 148, 34, 139, 40, 7, 403, 218, 95, 217, 254, 98, 35, 36, 37, 82, 162, 22, 50, 253, 263, 37, 205, 116, 183, 261, 146, 185, 41, 37, 38, 91, 184, 7, 148, 521, 86, 5, 12, 86, 218, 108, 60, 64, 448, 32, 571, 5, 157, 209, 8, 98, 122, 20, 399, 258, 76, 68, 356, 344, 10, 45, 42, 115, 151, 205, 15, 177, 65, 33, 212, 95, 151, 20, 35, 84, 123, 631, 24, 39, 45, 260, 36, 129, 288, 184, 18, 184, 28, 525, 75, 335, 5, 210, 2, 24, 19, 7, 55, 117, 117, 131, 16, 158, 18, 149, 54, 93, 12, 6, 160, 6, 45, 110, 110, 205, 94, 159, 20, 560, 54, 426, 68, 127, 99, 8, 635, 57, 43, 58, 20, 334, 135, 113, 148, 18, 66, 254, 10, 1, 57, 172, 42, 166, 198, 329, 12, 16, 224, 19, 27, 292, 164, 4, 660, 34, 53, 315, 41, 403, 28, 11, 53, 130, 6, 22, 73, 51, 177, 186, 61, 426, 695, 392, 105, 24, 73, 106, 57, 54, 22, 51, 13, 186, 18, 109, 51, 223, 257, 20, 236, 83, 179, 99, 48, 45, 111, 375, 103, 107, 99, 18, 37, 107, 253, 427, 22, 93, 143, 8, 91, 2584, 229, 11, 131, 67, 41, 30, 195, 376, 76, 12, 240, 37, 1117, 94, 18, 204, 121, 274, 59, 37, 451, 134, 11, 7, 544, 124, 32, 17, 96, 5, 249, 38, 442, 40, 142, 259, 10, 10, 77, 413, 172, 11, 171, 24, 3, 84, 169, 213, 129, 716, 37, 6, 4, 68, 271, 198, 17, 252, 18, 88, 394, 10, 291, 29, 238, 559, 341, 167, 27, 91, 11, 185, 24, 281, 207, 143, 86, 25, 217, 2293, 216, 870, 86, 12, 32, 134, 488, 144, 33, 298, 43, 416, 23, 73, 128, 29, 546, 74, 18, 205, 4, 12, 304, 1115, 216, 5, 65, 42, 86, 15, 470, 96, 108, 13, 10, 217, 368, 10, 74, 23, 22, 26, 218, 227, 52, 33, 169, 216, 42, 505, 54, 18, 447, 38, 2, 309, 122, 63, 54, 34, 132, 229, 13, 103, 155, 32, 167, 103, 375, 426, 48, 123, 6, 13, 101, 5, 154, 398, 27, 419, 38, 305, 12, 170, 307, 32, 87, 274, 4, 68, 123, 87, 12, 97, 35, 46, 5, 18, 217, 545, 117, 66, 79, 28, 52, 268, 103, 121, 11, 49, 188, 340, 32, 62, 203, 1090, 73, 84, 49, 4, 330, 11, 209, 700, 231, 19, 272, 4, 138, 9, 254, 15, 514, 18, 122, 77, 541, 386, 100, 63, 138, 59, 46, 12, 114, 118, 178, 532, 257, 275, 8, 159, 223, 250, 100, 353, 202, 89, 9, 485, 37, 296, 184, 263, 4, 11, 206, 84, 208, 194, 305, 142, 622, 25, 145, 1048, 368, 77, 38, 149, 166, 15, 14, 191, 225, 349, 158, 37, 184, 5, 29, 177, 134, 149, 16, 559, 66, 30, 78, 231, 4, 149, 38, 16, 24, 197, 19, 153, 104, 441, 8, 534, 144, 146, 157, 62, 180, 4, 24, 4, 107, 55, 233, 57, 49, 19, 266, 22, 65, 114, 494, 233, 69, 106, 30, 279, 50, 41, 228, 106, 143, 279, 133, 144, 62, 112, 26, 84, 28, 102, 662, 193, 15, 187, 127, 81, 135, 42, 59, 40, 164, 2, 191, 166, 233, 207, 16, 329, 68, 20, 350, 32, 60, 13, 370, 562, 242, 91, 32, 31, 97, 44, 199, 202, 70, 153, 170, 116, 251, 104, 11, 81, 40, 151, 84, 42, 21, 210, 15, 9, 35, 10, 438, 60, 85, 11, 52, 79, 37, 216, 2, 555, 16, 83, 39, 175, 25, 51, 36, 208, 5, 314, 15, 932, 25, 40, 31, 102, 300, 24, 221, 61, 152, 12, 34, 385, 18, 64, 114, 446, 96, 15, 7, 111, 288, 29, 17, 163, 67, 153, 402, 69, 25, 110, 402, 1, 902, 15, 143, 280, 183, 121, 138, 103, 19, 369, 30, 80, 37, 10, 64, 24, 63, 16, 21, 65, 67, 44, 136, 38, 1026, 304, 269, 26, 73, 131, 112, 29, 45, 159, 22, 284, 306, 47, 67, 47, 251, 15, 125, 407, 33, 11, 13, 134, 193, 76, 82, 203, 447, 13, 406, 72, 167, 71, 12, 1001, 172, 11, 245, 60, 126, 70, 20, 61, 49, 146, 15, 318, 131, 21, 28, 169, 40, 287, 216, 101, 75, 95, 1097, 102, 63, 82, 176, 93, 88, 101, 62, 17, 381, 109, 13, 153, 68, 142, 75, 20, 168, 17, 51, 131, 552, 91, 201, 157, 48, 15, 78, 56, 254, 161, 97, 30, 3, 147, 621, 76, 132, 81, 35, 385, 4, 123, 56, 382, 5, 135, 32, 83, 126, 366, 47, 92, 27, 6, 25, 145, 98, 124, 56, 4, 105, 28, 359, 25, 112, 12, 98, 13, 184, 18, 522, 18, 65, 234, 18, 52, 181, 64, 29, 45, 77, 242, 189, 173, 126, 162, 79, 370, 27, 378, 129, 59, 25, 167, 8, 16, 31, 122, 16, 33, 505, 299, 184, 20, 116, 13, 16, 280, 24, 137, 187, 126, 129, 72, 72, 240, 39, 70, 91, 47, 163, 471, 10, 506, 16, 150, 46, 229, 8, 91, 79, 43, 30, 16, 581, 82, 26, 387, 80, 36, 199, 93, 65, 207, 81, 35, 132, 60, 55, 588, 160, 144, 98, 113, 252, 20, 200, 55, 12, 855, 135, 153, 13, 29, 33, 481, 116, 67, 122, 39, 11, 40, 97, 12, 62, 12, 369, 219, 15, 58, 200, 271, 177, 206, 196, 44, 185, 117, 123, 72, 28, 7, 53, 205, 9, 27, 14, 108, 122, 69, 67, 29, 8, 432, 30, 84, 476, 64, 60, 43, 25, 39, 97, 264, 42, 35, 164, 608, 33, 47, 12, 41, 139, 222, 341, 272, 117, 161, 123, 752, 180, 43, 325, 78, 6, 32, 42, 253, 213, 58, 198, 204, 419, 71, 6, 72, 98, 142, 146, 10, 574, 414, 29, 192, 318, 53, 10, 17, 170, 548, 36, 332, 367, 89, 60, 379, 566, 322, 35, 256, 10, 113, 218]

* Decrypted message with correct keys

Estranho seria se eu não me apaixonasse por você
O sal viria doce para os novos lábios
Colombo procurou as Índias mas a Terra avisto em você
O som que eu ouço são as gírias do seu vocabulário
Estranho é gostar tanto do seu All Star azul
Estranho é pensar que o bairro das Laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
Continuar aqu**f**la conversa
Que não terminamos ontem, ficou pra hoje
Estranho, mas já me sinto com**p** um velho amigo seu
Seu All star azul combina com o meu, preto, de cano alto
Se o homem já pisou na Lua, como ainda não tenho seu endereço
O tom que eu canto as minhas músicas na sua voz parece exato
Estranho é gostar tanto do seu All Star azul
Estranho é pensar qve o bairro das Laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
Continuar aquela conversa
Que não terminamos ontem, ficou nas laranjeiras
Satisfeito sorri, quando chego ali
E entro no elevador, aperto o 12, que é o seu andar
Não vejo a hora de te encontrar
E continuar aquela conversa
Que não terminamos ontem, ficou pra hoje, hoje, hoje


* Decrypted message with Xo = 0.7 + 1e-16

xG}na@ç. ãK1+3g?W9~<[`)Í;G;9\9/5.@l6?0/hãá9j :5R7={/K`U_9@ã.1L|i
7tmaIbV8^Me}çsúYn{59Í3]ó5~áà?8699éGq6BÍô{â2Y@3<98Yd"bF{í}394\]a0<é_S8/>aâba90[7
'd)\NF~$ ;Í M-5P-çe'#`gI\,?o e
ç#e@í\{D,|*|<êrlNô9O5}
VX}%e}N{Xê9S^-\7D@çG89;Eb|f~ds}m32j?.Í9OíwCiã1r3.\\{7?/+9{*68`JêW{âú|]`=(};6R9'9}@b&<ó^ú9]^#|&81â17ã|naçê9càRe 7
Uuóe{3\d9G[J7@9i[á
l989>9vã;a5g|5e8Qe|ad9
?($<p\á^dEU_b]\á1âE`}ãaZ
[ô}:^_7 8\9féã{\i8%+99_L9"í``{9?Q"b`ôÍ8Z8[];a22âPnâOl}QB
C92
ó?!56V<CáW]8 6+3[_"!9$NJó[p`óô,r$ç_9S5Wía.8_épóà3.[c]@68m<âô]a|u_.5Q9\0ççáS:àWNOR_}9n[br~af8v
}?93`>d?3k[9áR;74ô/:~.b%4âS@5
ix.9 ékRó968|^]éQ``9[qaÍ59.bc`{4
e.$@21a2L_WÍ
l@âb0}I{93&ÍT2}"<9^V71í@9|859Bq16A1CY9je\@ywím!8
~,4`^:>á\=<1^7^>óÍÍ"à17]]`ç9>[``a?â_YJ.@|í!r^{Q{a?>x4à_3kí\ÍÍ{[9dÍ\/99[ae5e9`{m,:76@xs[
FY`a7p{)U*`m]}Q8Wb]8a?â)[Rbo9@d@}aó9WÍ~eãR'd=Iá6[rf6` H|çFa_ô~}|êô7áàyg0jU\^á@|@Ej9ç=*8mbâgó].úo>\_Fy:k}aá9~ãe8^Q?69)7[{9{a}/~çc|p9^`ã%i|h9{va`ÍZ@9`p|Í|}=>éê32&X5\aoí
ê\=~69Ré4![6D93e^[75iãh9J[_@[[4d64}é,@Í.x24#í4]az*9G?.99ç79b~9-&9?0|&>af
ô|@ê9_{9^PO2b],7Rú%vú/1iâ,6!nóBE_úc5{7'ahIóaKêÍê
9;_'ú7íó@`u9Í99DE^c5á9:Í]R\|$tBRãL[qí89{A9?sH]*í{!fb#B<``|?@~$`Y;Í4 $bHAúô9[[>QH3E/b)ê[#ê9Íg94b4Í@3ç9;|||=ap]:S^In|_b\óaá#]6\gà`i;6[`ô@\.`c^^+9


## Sources 
* BAPTISTA, M. S. [Cryptography with chaos](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.9974&rep=rep1&type=pdf). Physics letters A, v. 240, n. 1-2, p. 50-54, 1998.
