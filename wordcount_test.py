#Team Members: Adam Scerra, Elenor Drak, Tyler Giordani


file=open('extracted.txt')
wordcount={}
count = 0
hapexCount = 0
uniqueCount = 0
maxLength = 0
maxWord = ''

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for word in wordcount:
	uniqueCount = uniqueCount + 1
	count = count + wordcount[word]
	if(wordcount[word] == 1):
		hapexCount = hapexCount + 1
	#if(len(word) > maxLength):
		#maxLength = len(word)
		#maxWord = word

#print number of words, and number of unique words
print('The total number of words:', count)
print('The total number of hapex words:', hapexCount)

hapexPercent = 100 * hapexCount / uniqueCount

#Print percent of unique words
print(hapexPercent,'% of unique corpus words were hapex')

#Print the longest word and displays its length
print('The longest word was: \'', maxWord, '\' with a length of:', maxLength, 'characters')

#below we find the 10 most frequent words
words = open('extracted.txt').read().lower().split()

uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

counts = []
for unique in uniques:
  count = 0             
  for word in words:     
    if word == unique:   
      count += 1         
  counts.append((count, unique))

counts.sort()            
counts.reverse()         

percentCount = 0

print('The 10 most commonly used words in the corpus with corresponding occurences were: ')
for i in range(min(10, len(counts))):
  count, word = counts[i]
  print('%s %d' % (word, count))
  percentCount = percentCount + count

print('The percent of these 10 words against the corpus total is: ',percentCount/count, '%')

file.close();
