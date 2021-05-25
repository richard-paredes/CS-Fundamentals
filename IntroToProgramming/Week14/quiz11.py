
'''
num = []
for i in range(1000):
    if (i % 3 == 0):
        num.append(i)
    elif (i % 5 == 0):
        num.append(i)

print(sum(num))


def isPrime(num):
    if (num == 2 or num == 1):
        return True
    elif (num % 2 == 0):
        return False
    elif (num > 1):
        count = 3
        sqroot = int(num ** (1/2))
        
        while(count <= sqroot):
            if (num % count == 0):
                return False
            count += 2
        return True
    
    else:
        return False

primes=[]
count = 2
while (len(primes) < 500):
    if (isPrime(count)):
        primes.append(count)
    count += 1

print(sum(primes))

prime=[]
count = 2
while (len(prime) < 10001):
    if (isPrime(count)):
        prime.append(count)
    count += 1

print(prime.pop())
'''
'''
freq = dict.fromkeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0)
with open('yawl.txt') as file:
    for line in file:
        word = line.strip()
        firstLetter = word[0]
        freq[firstLetter] += 1

print(freq)

words = []
points = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
with open('yawl.txt') as file:
    for line in file:
        word = line.strip()
        if (len(word) == 8):
            words.append(word)

maxScore = -1
maxWord = ''
for word in words:
    score = 0
    for letter in word:
        score += points[letter]
    if (maxScore < score):
        maxScore = score
        maxWord = word

print(maxScore, maxWord)
'''
def invert_dict(a_dict):

    inverted = {}

    for key in a_dict:
        print(inverted)
        inverted[a_dict[key]] = key 

    return inverted

test = {1: "A", 2: "B", 3: ["C", "D"]}
invert_dict(test)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = 0

cypher = {}

for letter in alphabet:
    cypher[letter] = num
    num += 1
print(cypher)