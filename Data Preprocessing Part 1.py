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
