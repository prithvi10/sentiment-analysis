import nltk as nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import string
import re

neg_words=[]
wordlist=[]
final_list=[]
fp=open('/home/prithviraj/sentiment analysis/my_senti_wordnet.txt','r+')


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
	#trigram_finder=
	scored=bigram_finder.nbest(BigramAssocMeasures.chi_sq,200)
	neg_words=[]
	regex=re.compile("('never',|'not',)")
	neg_words.append([l for l in scored for m in [regex.search(str(l))] if m])
	return neg_words



def assign_scores():												
	all_words_string=fp.read()
	all_words_list=all_words_string.split("\n")
	for i in all_words_list:
		final_list.append(i.split("\t\t"))
	print final_list											#final_list is the list of lists which contains the element as[word,pos_value,neg_value]

	for l in final_list:
		for m in l:
			




parse_input_data()
assign_scores()
fp.close()