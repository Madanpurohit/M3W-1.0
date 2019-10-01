# Part 1 Data Preprocessing 
# Creating Dictionary line and Conversations of Database
# Date : 30-09-2019


import numpy as np
import re
import time

#Creating Variable of Database by reading 2 datafile
#Spliting every line with respect to \n

lines = open("movie_lines.txt", encoding = 'utf-8', errors = 'ignore').read().split('\n')  
conversations = open("movie_conversations.txt", encoding = 'utf-8', errors = 'ignore').read().split('\n')

#Creating Dictonaries of Lines and Conversations in neat and clean way

id2line = {}

for line in lines :
  _line = line.split(' +++$+++ ')                              # Every line in Datasheet are in Format 
  if len(_line) == 5 :                                         # L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
    id2line[_line[0]] = _line[4]                               # So We have to split the data with respect to ' +++$+++ '

# Creating List of Conversations Its Similar to Creating Dictionary

conversations_ids = []

for conversation in conversations[:-1] :
  _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")   
  conversations_ids.append(_conversation.split(",")) 
  
# u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L194', 'L195', 'L196', 'L197']
# The Lines in Conversation are in above Format so we only need ID part which are
# the list in the end. So to retreve it First we Split with respect to ' +++$+++ '
# and then retreve the last column by [-1][1:-1]. Then we Replace '' in List and slpit it with respect to ,
# to append it.

# By the end we will get two Clean data variable of line and conversation which will be easy to use #



# Creating List of Question and Answer
# The answer of Queston in Question list of index i will be in index i in answer List.

# Creating List Variable of question and Answer
questions = []
answers = []

# id2line contain every Lines with Key. It contains question and answer.

for conversation in conversations_ids :                    # Now here we are creating two List of Question and Answer
  for i in range(len(conversation) - 1) :                  # id2line contain data in this form
    questions.append(id2line[conversation[i]])             # |Key     Type    Size        Value          |
    answers.append(id2line[conversation[i+1]])             # |L1000    str     1    Because he called me.|
                                                           # And conversations_ids are in this format.
                                                           # |index    type    size              Value                   |
                                                           # |  0      list     4      ['L194', 'L195', 'L196', 'L197']  |
                                                           # Ignore type and size its only for explaination the table only 
                                                           # contain Key and Value in id2line and Value in conversations_ids
          
# Explaination :
# In converations_ids part we hae |Values| as a list of Key or kinda Index Pointer.
# Here in Example ['L194', 'L195', 'L196', 'L197'].  'L194' id a pointer or index
# The thing is every next Index points to answer of previous Index.
# Like 'L195' is answer of 'L194' & 'L196' is answer of 'L195' ans so on
# So to create question and answer list we need two loop 



# Cleaning The Text (Removing Unnecessary elements from text)
# Cleaning also include Converting text into lower case
# We are Creating clean_text function

def clean_text(text) :
  text = text.lower()                                                # Converting Into Lower Case
  text = re.sub(r"i'm", "i am", text)                                # Creating Substitute for complex word and replacing it
  text = re.sub(r"he's", "he is", text)                              # For Example : 
  text = re.sub(r"she's", "she is", text)                            # i'm = i am, she's = she is
  text = re.sub(r"that's", "that is", text)                          # won't = will not etc.
  text = re.sub(r"what's", "what is", text)
  text = re.sub(r"where's", "where is", text)
  text = re.sub(r"\'ll", "will", text)
  text = re.sub(r"\'ve", "have", text)
  text = re.sub(r"\'re", "are", text)
  text = re.sub(r"\'d", "would", text)
  text = re.sub(r"won't", "will not", text)
  text = re.sub(r"can't", "cannot", text)
  text = re.sub(r"[-()\-#/@:;<>+=|.?,]", "", text)                   # Removing Special Characters
  return text                                                        # Returning cleaned text

#Part : 2 (Data Processing)
#Date : 30-09-2019

#@Cleaning the Questions

#List which will save the cleaned questions after all the questions goes through the Function named as "clean_text"
list_of_clean_questions = []

#Loop for taking each and every question in the list named as questions
for question in questions:
	list_of_clean_questions.append(clean_text(question))#after going through the clean_text function appending the cleaned question in the New list named as list_of_clean_questions

#@Cleaning the Answers

#List which will save the cleaned answers after all the answers goes through the Function named as "clean_text"
list_of_clean_answers = []

#Loop for taking each and every answer in the list named as answers
for answer in answers:
	list_of_clean_answers.append(clean_text(answer))       #after going through the clean_text function appending the cleaned answer in the New list named as list_of_clean_answers

#Till now We've got our Cleaned questions and answers list

#@Ceating a dictionary to map the frequency of each word
#we're doing this to optimize the training and to optimize training we need only essential Vocabulary

#dictionary which will save the frequency of each and every word in the list_of_clean_questions and list_of_clean_answers
word2frequency = {}

# 1st loop will take the each and every question in the list named as list_of_clean_questions
# 2nd loop will take the each and every word of the question selected by the 1st loop
# split function is used because question selected by the 1st loop is in sentence form but we need each and every word of that sentence so function split will split all the words in that sentence
# if condition is used to check whether the word that is selected by loop is present in dictionary called as word2frequency or not
# if Not present then make that word as key and give the value/frequency as 1 because that word is found 1 time till
# if present than increment the value/frequency of that word 
for question in list_of_clean_questions:
	for word in question.split():
		if word not in word2frequency:
			word2frequency[word] = 1
		else:
			word2frequency[word] += 1

# 1st loop will take the each and every answer in the list named as list_of_clean_answers
# 2nd loop will take the each and every word of the answer selected by the 1st loop
# split function is used because answer selected by the 1st loop is in sentence form but we need each and every word of that sentence so function split will split all the words in that sentence
# if condition is used to check whether the word that is selected by loop is present in dictionary called as word2frequency or not
# if Not present then make that word as key and give the value/frequency as 1
# if present than increment the value/frequency of that word 
for answer in list_of_clean_answers : 
	for word in answer.split():
		if word not in word2frequency:
			word2frequency[word] = 1
		else:
			word2frequency[word] +=1

#By the end of this section we will have all the words in list of clean questions and answers with their frequencies

#@Creating 2 Dictionaries that map the question words and answer words to a unique intezer
#In this section we are doing very essential and Important tasks that is Tokenization and filtering the non-frequent words

#This is the min frequency if frequency of any of the word in the dictionary word2frequency is unable to pass this frequency that word will be disqualified
#Threshold Freq can be increased in order to Decrease the training time
#Threshold freq can be decrease if You have great processor because decreasing threshold can lead to increase in time of training chatbot
threshold = 15 
word_number = 0 #This is the Unique number that will be given to those words that cross the threshold i.e >=15

questions_words_2_uniq_int = {} #This dictionary will hold all the words in the question that will cross the threshold frequency

#In dictionary we have Keys and the Values so the Variable Word will hold the Key and Count will hold the value/frequency of that word
#If condition will check if the frequency of word is >= threshold or not
# If yes then it will be pushed to new dictionary called questions_words_2_uniq_int and increment the unique number
# If not then disqualified
for word , count in word2frequency.items():
	if count >= threshold:
		questions_words_2_uniq_int[word] = word_number
		word_number += 1

answers_words_2_uniq_int = {} #This dictionary will hold all the words in the answer that will cross the threshold frequency

word_number = 0 #This is the Unique number that will be given to those words that cross the threshold i.e >=15

#In dictionary we have Keys and the Values so the Variable Word will hold the Key and Count will hold the value/frequency of that word
#If condition will check if the frequency of word is >= threshold or not
# If yes then it will be pushed to new dictionary called answers_words_2_uniq_int and increment the unique number
# If not then disqualified
for word , count in word2frequency.items():
	if count >= threshold:
		answers_words_2_uniq_int[word] = word_number
		word_number += 1

#At the end of this section we have 2 lists of question and answer words with unique Intezers

# Part : 3(DATA PROCESSING)
"""
Created on Mon Sep 30 22:11:32 2019
@author: VARUN MISHRA
"""
# Adding the last tokens to these two dictionaries
tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
##EOS = End Of string, OUT = filter out, SOS = star of string 
for token in tokens:
    questions_words_2_uniq_int[token] = len(questions_words_2_uniq_int)+1
for token in tokens:
    answers_words_2_uniq_int[token] = len(answers_words_2_uniq_int)+1
''' we now have our final tokens the essential tokens for the sectors 
    like added to our two dictionaries'''

# Creating the inverse dictionary of the answerswords2int dictionary
'''Beacause we will need inverse mapping from the integers to the answers
words in the implementation of the sectors like model and we actually just
need for the answers words in dictionary and not the questions words, so
this will be very quick :) '''
answersints2word = {w_i : w for w, w_i in answers_words_2_uniq_int.items()}
#w_i corresponding to word integers

# Adding the End of string token to the end of every answer
for i in range(len(list_of_clean_answers)):
    list_of_clean_answers[i] += '<EOS>'
'''End of string token is needed at the end of the decoding layers of the 
sect to sect model'''
#part 4: (Data Processing)
''' Created on MON SEP 29 2019
@author Madan Singh
'''
# Translating all the question and the answer into integer
# and replacing all the words that were filtered out bt <OUT>

questions_into_int=[] #created a list to store integer part of questions
for question in list_of_clean_questions:
    ints=[] #to contain integer of each word
    for word in question.split():# select words separated by space
        if word not in questions_words_2_uniq_int: # it will select those words which are filtered
            ints.append(questions_words_2_uniq_int['<OUT>'])
        else:
            ints.append(questions_words_2_uniq_int[word])
    questions_into_int.append(ints)
#same for the answer
answers_into_int=[] #created a list to store integer part of answer
for answer in list_of_clean_answers:
    ints=[] #to contain integer of each word
    for word in answer.split():# select words separated by space
        if word not in answers_words_2_uniq_int: # it will select those words which are filtered
            ints.append(answers_words_2_uniq_int['<OUT>'])
        else:
            ints.append(answers_words_2_uniq_int[word])
    answers_into_int.append(ints)

#sorting answers and questions by the length of questions
sorted_clean_questions=[]
sorted_clean_answers= []
for length in range(1,26): #becoz of length of question can be minimum 1 or maximum can be 25
    for i in enumerate(questions_into_int): #enumerate function returns couple of index and data of list
        if len(i[1])==length: #at i[0] there will be index of element and at i[1] there will be itself
            sorted_clean_questions.append(questions_into_int[i[0]])
            sorted_clean_answers.append(answers_into_int[i[0]]) #becoz answer of question and question will be at same index


