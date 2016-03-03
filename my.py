import nltk as nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import string
def parse_input_data():

	f=open("news.txt",'r+')
	string_text=f.read()
	string_text=string_text.replace('\n','')  #replacing the special characters
	ch=set(string.punctuation)
	l1=''.join(c for c in string_text if c not in ch)	#removing the punctuation marks
	list_text=l1.split(" ")

	stopset=stopwords.words('english')    #importing stopwords
	wordlist=[]
	for words in list_text:								#generating a corpus  of the words that we need
		if words not in stopset:
			wordlist.append(words)
	print wordlist





parse_input_data()
