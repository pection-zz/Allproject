from nltk.corpus import inaugural 
from nltk.corpus import stopwords
import nltk
import pandas as pd 
wordsStop = ['this','will','that','must','may','and']
worddict,a2,a3=dict(),dict(),dict()
countloop=0
speech,listword,nametxt,nameyear,listall=dict(),[],[],[],[]
countbigloop = 0
global State 
State = True
def conlisttodic(lst):
	dct= dict()
	for i in range(0, len(lst)):
		for j in range(0,1):
			dct.update({lst[i][j]:lst[i][j+1]})
	return dct
    
def makeStopWords():
	sw = stopwords.words('english')
	for i in wordsStop :
		sw.append(i)ห
	return sw
stopWord = makeStopWords()
for fileID in inaugural.fileids()[-12:]:
	wordList=list()
	for word in inaugural.words(fileID):
		word = word.lower()
		if word.isalpha() and word not in stopWord:
			wordList.append(word)
	speech[fileID] = nltk.FreqDist(wordList)
# 			print(type(speech))

for i,k in speech.items() :
	print(i,k)
	nameyear.append(i)
	worddict[countloop] = k
	countloop = countloop+1
intersectionn= worddict[0] & worddict[1] & worddict[2] &worddict[3] & worddict[4] & worddict[5] &worddict [6] & worddict[7] & worddict[8] & worddict[9] & worddict[10] & worddict[11] 
intersectionnsort = sorted(intersectionn)
for i in range(len(nameyear)):
	for j in intersectionnsort:
# 		print (j,worddict[i][j])
		nametxt.append((worddict[i][j]))
for i in worddict:
		sumWord = sumWord + worddict[i]
# 	print (sumWord)
for i in worddict:
		print (j,Dctword[j],"%.2f" % (worddict[j]*100/sumWord))
		Dctword[j]="%.2f" % (worddict[j]*100/sumWord)
for i in range(0,11):
	for j in range(1,12):
		listall.append([nameyear[i],nametxt[:j*21]])
print (listall)
df_fdist=pd.DataFrame([listall],orient='index')

# df_fdist = pd.DataFrame(nametxt[:21],nameyear[:0],intersectionnsort)
# 
# # df_fdist = df_fdist.'transpose()

print (df_fdist)		
export_csv = df_fdist.to_csv(q3output.csv)
		
		
		