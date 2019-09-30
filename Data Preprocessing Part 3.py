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

----------------------------------------------------END--------------------------------------------------
