######################################################################################
####################### Part 2 : BUILDING THE SEQ2SEQ MODEL ########################
"""
Created on Fri Oct  11
@author: MADAN SINGH
"""
#creating the encoder RNN Layer
#we will create some layers to train boat
def encoder_rnn_layer(rnn_input,rnn_size,num_layers,keep_prob,sequence_length):
    lstm=tf.contrib.rnn.BasicLSTMCell(rnn_size)
    lstm_dropout=tf.contrib.rnn.DropoutWrapper(lstm,input_keep_prob=keep_prob)
    encoder_cell=tf.contrib.rnn.MultiRNNCell([lstm_dropout]*num_layers)
    _, encoder_state=tf.nn.bidirectional_dynamic_rnn(cell_fw=encoder_cell,cell_bw=encoder_cell,sequence_length=sequence_length,inputs=rnn_input,dtype=tf.float32)
    return encoder_state

# Decoding the training set

def decode_training_set(encoder_state,decoder_cell,decoder_embedded_input,sequence_length,decoding_scope,output_function,keep_prob,batch_size):
    attention_states=tf.zeros([batch_size,1,decoder_cell.output_size])
    attention_keys,attention_values,attention_score_function,attention_construct_function=tf.contrib.seq2seq.prepare.attention(attention_states,attention_option='bahdanau',num_units=decoder_cell.output_size)
    training_decoder_function=tf.contrib.seq2seq.attention_decoder_fn_train(encoder_state[0],attention_keys,attention_values,attention_score_function,attention_construct_function,name="attn_dec_train")
    decoder_output,decoder_final_state,decoder_final_context_state=tf.contrib.seq2seq.dynamic_rnn_decoder(decoder_cell,training_decoder_function,decoder_embedded_input,sequence_length,scope=decoding_scope)
    decoder_output_dropout=tf.nn.dropout(decoder_output,keep_prob)
    return output_function(decoder_output_dropout)
