from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes
import sage

outputFile = 'output.txt'

f = open(outputFile,'rb')
cipherText = f.read()
cipherText = long_to_bytes(int(cipherText,16))
n=len(cipherText)

L_lenK=[]
L_PlainText=[]

#Factors : 2**5  3**5  79**1
#Helps to find the possible Key length sizes

fac = factor(n)
fac=list(fac)
fac.append((1,1))

possible_PlainTexts = 0

for i in range(len(fac)):
    for j in range(i+1,len(fac)):

        lenK = fac[i][0]**fac[i][1]

        lenK *= fac[j][0]**fac[j][1]
        
        if (10<=lenK<=100):
            L_lenK.append(lenK)
            
print(L_lenK)

for KeySize in L_lenK:

    lenK = KeySize
    lenP = n // lenK
    #used b'amateurs' only because once all possible keys are found,
    #I need to determine which is the correct key, its the one that contains the following bytes b'amateursCTF{'

    word = b'amateurs'

    Keys=[]

    for i in range(lenP - 7):

        Key = [b' ']*lenK

        for j in range(i, lenP * lenK, lenP):

            #pos helps determine which key bytes of the 79 or 32 key length bits are encrypting the plaintext in variable 'word'
            pos = j % lenK

            T = strxor(word, cipherText[j : j + 8])

            offset = 0

            while((pos + offset < lenK)and (offset < 8)):

                Key[pos + offset] = T[offset]

                offset += 1

            if not(b' ' in Key):

                Keys.append(Key)
                break


        print('step :' + str(i) + ' / ' + str(lenP - 7))

    for i in Keys:
        key=b''

        for j in i:
            key+=long_to_bytes(j)

        keylength = KeySize
        key = key * lenP
        plaintext = strxor(cipherText, key)[: lenP]

        if(b'amateursCTF{' in plaintext):
            L_PlainText.append(plaintext)
            possible_PlainTexts += 1

for i in L_PlainText:
    print(i)

print('\nPossible number of Plaintexts: ', possible_PlainTexts)