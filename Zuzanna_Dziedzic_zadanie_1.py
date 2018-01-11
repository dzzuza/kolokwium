alphabet="aąbcćdeęfghijklłmnoóprqsśtuvwxyzźż"
alphabetbig="AĄBCĆDEĘFGHIJKLŁMNOÓPRQSŚTUVWXYZŹŻ"
#tojestzmiana1
word=str("kajak")
sentence=("Napotkała typa. Zapytała: 'Kto Pan?'")
word2=''
for znak in sentence:
  if(znak in alphabet):
    word2+=znak
  elif(znak in alphabetbig):
    word2+=alphabet[alphabetbig.index(znak)]
#print(word2)

def palindrom(word):
  n=len(word)
  flag=0
  for i in range(n//2):
    #print(i)
    #print(n-i)
    if(word[i]!=word[n-1-i]):
      flag=1
  if(flag==0):
    print("to jest palindrom")
  else:
    print("to nie jest palindrom")
    
word3="toniebedziepalindromem"

print(word)
palindrom(word)
print('\n')
print(word3)
palindrom(word3)
print('\n')
print("teraz sprawdzam zdanie:\n")
print(sentence)
palindrom(word2)
