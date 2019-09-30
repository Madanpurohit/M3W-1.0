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

------------------------------------------------END---------------------------------------------------


