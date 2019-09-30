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
answer = []

# id2line contain every Lines with Key. It contains question and answer.

for conversation in conversations_ids :                    # Now here we are creating two List of Question and Answer
  for i in range(len(conversation) - 1) :                  # id2line contain data in this form
    questions.append(id2line[conversation[i]])             # |Key     Type    Size        Value          |
    answer.append(idl2line[conversation[i+1]])             # |L1000    str     1    Because he called me.|
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
