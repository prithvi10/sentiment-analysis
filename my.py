import nltk as nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import string
import re

neg_words=[]
wordlist=[]
parse_input_data()



def parse_input_data():

	f=open("news.txt",'r+')
	string_text=f.read()

	
	neg_words=ngrams(string_text) 						#separates the not and never	

	string_text=string_text.replace('\n',' ')  			#replacing the special characters

	ch=set(string.punctuation)
	l1=''.join(c for c in string_text if c not in ch)	#removing the punctuation marks

	list_text=l1.split(" ")
	stopset=stopwords.words('english')    				#importing stopwords

	for words in list_text:								#generating a corpus  of the words that we need
		if words not in stopset:
			wordlist.append(words)
	print wordlist,neg_words




def ngrams(string_text):											#calculates the bigrams to separate the 'not' and 'never' statement
	tokens=nltk.word_tokenize(string_text)								
	bigram_finder=BigramCollocationFinder.from_words(tokens)
	trigram_finder=
	scored=bigram_finder.nbest(BigramAssocMeasures.chi_sq,200)
	neg_words=[]
	regex=re.compile("('never',|'not',)")
	neg_words.append([l for l in scored for m in [regex.search(str(l))] if m])
	return neg_words



def assign_scores():
	
