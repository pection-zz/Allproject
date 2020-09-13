from nltk.corpus import inaugural 
from nltk.corpus import stopwords
import nltk
import pandas as pd 
# a=[america,american,future,god,government,great,life,long,nation,new,one,people,president,strength,time,today,together,us,way,work,world]
# nltk.download()
wordsStop = ['this','will','that','must','may','and']
speech,wordList,nametxt,nameyear=dict(),list(),dict(),list()
countbigloop = 0
def conlisttodic(lst):
	dct= dict()
	for i in range(0, len(lst)):
		for j in range(0,1):
			dct.update({lst[i][j]:lst[i][j+1]})
	return dct
    
def makeStopWords():
	sw = stopwords.words('english')
	for i in wordsStop :
		sw.append(i)
	return sw
stopWord = makeStopWords()
for fileID in inaugural.fileids()[-12:]:
	nameyear=list()
	wordList = list()
	sumWord = 0
	countloop = 0
	for word in inaugural.words(fileID):
		word = word.lower()
		if word.isalpha() and word not in stopWord:
			wordList.append(word)
		speech[fileID] = nltk.FreqDist(wordList)
	for k,v in speech.items():
# 		print(f'{k} {v.most_common()}')
# 		print (type(v.most_common()))
		nameyear.append(k)
		wordlist = v.most_common(10)
	Dctword= conlisttodic(wordlist)	
	for i in stopWord:
		Dctword.pop(i, None)    
	for i in Dctword:
		sumWord = sumWord + Dctword[i]
# 	print (sumWord)
	for j in Dctword:
		print (j,Dctword[j],"%.2f" % (Dctword[j]*100/sumWord))
		Dctword[j]="%.2f" % (Dctword[j]*100/sumWord)
	df = pd.DataFrame.from_dict(Dctword,orient='index')
# 	print(nameyear)
	df.columns=nameyears
	df = df.transpose()
	print (df)	
# 	print (nameyear)
