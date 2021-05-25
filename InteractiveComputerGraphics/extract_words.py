import re
#load in the sherclock holmes text file
with open("SherlockHolmes.txt", "r") as SherHolmes:
  text = SherHolmes.read()

#clean the data using the regular expression library
outText = re.findall(r'[a-zA-Z]+', text)

#lowercase each word using a temp variable to store the lowercased words
temp = []
for item in outText: 
    temp.append(item.lower())
outText = temp
outString = "\n".join(outText)

#create a dictionary of all the words and the number of occurances
wordDict = {}
for item in outText:
	if item in wordDict:
		wordDict[item] = wordDict.get(item)+1
	else:
		wordDict[item] = 1

uniqueWords = ""
#create a dictionary of the frequencies to take the frequencies of the frequencies
freqDict = {}
for item in wordDict:
	if wordDict[item] == 1: #appending unique words to the unique words string to later print
		uniqueWords = uniqueWords + "\n" + item
	if wordDict[item] in freqDict: #adding elements to library and indexing the number of occurances
		freqDict[wordDict[item]] = freqDict.get(wordDict[item]) + 1
	else:
		freqDict[wordDict[item]] = 1

#run through frequency dictuonary to append the word frequencies to print to file
frequency = ""
for item in sorted(freqDict):
	frequency = frequency + str(item) + ": " + str(freqDict[item]) + "\n"

#print string to respective text files
with open("allWords.txt","w") as allWords:
	allWords.write(outString)
with open("uniqueWords.txt","w") as UniqueWords:
	UniqueWords.write(uniqueWords)
with open("wordFrequency.txt","w") as wordFrequency:
	wordFrequency.write(frequency)

  
  
