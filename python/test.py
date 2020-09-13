
from nltk.corpus import inaugural
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
stopwords = stopwords.words('english')
def makeStopWords():
  sw = stopwords.words('english')
  sw.append('this')
  sw.append('will')
  sw.append('that')
  sw.append('must')
  sw.append('may')
  sw.append('and')
  return sw

stopWord = makeStopWords()
speech = dict()

for fileID in inaugural.fileids()[-12:]:
  wordList = list()
  for word in inaugural.words(fileID):
    word = word.lower()
    if word.isalpha() and word not in stopWord:
      wordList.append(word)
  speech[fileID] = nltk.FreqDist(wordList)

for k,v in speech.items():
  print(f'{k} {v.most_common(10)}')