######################################################################################
 ####################### Part 1 : BUILDING THE SEQ2SEQ MODEL ########################
"""
Created on Tue Oct  1 22:34:51 2019
@author: VARUN MISHRA
"""

# CREATING PLACEHOLDER FOR THE INPUTS AND THE TARGETS

'''we are going to do it through a function that we'll call model input and 
inside this function we will create a placeholder for the input a placeholder for
the targets and then we will add a learning rate and even more hybrid parameters'''

def model_input():
    inputs = tf.placeholder(tf.int32, [NONE,NONE], name = 'input')
    targets = tf.placeholder(tf.int32, [NONE,NONE], name = 'target')
    lr = tf.placeholder(tf.float32, name = 'learning_rate')
    keep_prob = tf.placeholder(tf.float32, name = 'keep_prob')
    return inputs, targets, lr, keep_prob
# tf.int32--> type of input, [NONE,NONE]-->2-Dimension of the matrix of the input data
# lr--> learning rate
    
########################## PREPROCESSING THE TARGETS ############################# 
def preprocess_targets(targets, word2int, batch_size):
    # word2int-->dictionary word that maps the tokens to integers
    left_side = tf.fill([batch_size, 1], word2int['<SOS>'])
    #batch_size-->choose a batch size for the size of the batches of targets
    right_side = tf.strided_slice(targets, [0,0], [batch_size, -1], [1,1])
    #tf.strided_slice()-->it extract a subset of a tensor
    preprocessed_targets = tf.concat([left_side, right_side], 1)
    return preprocessed_targets

---------------------------------------END-------------------------------------------
