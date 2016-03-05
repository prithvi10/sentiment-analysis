f=open("/home/prithviraj/sentiment analysis/file.txt","r+")
f1=open('/home/prithviraj/sentiment analysis/my_senti_wordnet.txt','r+')
import re
for i,line in  enumerate(f):
		line1=line.split("\t")															#separates the list objects at tab
		del line1[5]																	#deletes the meaning,example,parts_of_speech specified in a line
		del line1[1]
		del line1[0]

		words=line1[2]																    #separates the words 
		del line1[2]																	
		regex=re.compile("#1$")															#finds the regex to match the words first meaning
		words=words.split(" ")

		senti_value_list=[]							#list of sentiment values of the words with first meaning ..in a line 
		words_with_hashtag=[]
		final_words=[]								#final words to be put in the file

		words_with_hashtag=[i for i in words for j in [regex.search(str(i))] if j]			#finds the #1 tag
		
		senti_value_list=line1
		if len(words_with_hashtag) :
			for i in words_with_hashtag:
				final_words.append(str(i).replace("#1",''))										#removes the #1 tag

		for i in final_words:
			f1.write(str(i)+"\t\t"+str(senti_value_list[0])+"\t\t"+str(senti_value_list[1])+"\n")		#putting the final word:scorep:scoren trio in a file

f1.close()
f.close()