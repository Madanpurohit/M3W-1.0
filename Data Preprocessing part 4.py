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

#----------------------------------------------------------------------------END---------------------------------------------
