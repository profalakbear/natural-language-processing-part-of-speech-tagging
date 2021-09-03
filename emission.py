#region Import libraries
import nltk
import os
import pprint 
import time
import random
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from IPython.display import display
#endregion

#region Open 3 train datasets and merge them in one string
path_to_train_data = 'C:\\Users\\alakb\\Desktop\\NLP HOMETASK POS TAGGING WITH HMM\\brown_hw\\Train\\'
train_data_list = os.listdir(path_to_train_data)
train_set_limit = 3
train_string = ""
limit = 1

for files in train_data_list:
        if limit != 2: # First 3 file of train data set
            with open(path_to_train_data + (str(files)), 'r') as f:
                fileData = f.read()
                train_string = train_string + fileData
                limit = limit + 1
        else:
            break
#endregion

#region Convert merged string to lowercase
train_string = train_string.lower()
#endregion

#region Take tagged string, convert it (word,tag) list of tuple and after convert that list to array
word_and_tag_tuple = [nltk.tag.str2tuple(t) for t in train_string.split()]
array_of_tuple = np.array(word_and_tag_tuple)
#endregion

tags_set = set()
tags_array = []

for i in range(len(array_of_tuple)):
    tags_set.add(array_of_tuple[i][1])

tags_array = list(tags_set)

def tagCount(sx):
    ctr = 0
    for i in range(len(array_of_tuple)):
        if array_of_tuple[i][1] == sx:
            ctr +=1
    return ctr


counter = 0
emission = []
insert_em = tuple()

for i in range(len(array_of_tuple)):
    for j in range(len(array_of_tuple)):
        tags_counter = 0
            if array_of_tuple[i][0] == array_of_tuple[j][0] and array_of_tuple[j][1] == tags_array[tags_counter]:
                counter +=1
            y = tagCount(tags_array[tags_counter])
            res = counter/y
            insert_em  = (array_of_tuple[i][0], tags_array[tags_counter], res)
            emission.append(insert_em)
            tags_counter += 1
            insert_em = tuple()
            counter = 0




df = pd.DataFrame(emission, columns =['   WORD', '   TAG', '   WORD_GIVEN_TAG'])

f = open("emission.txt", "x")
f.write('WORD  TAG   WORD_GIVEN_TAG' '\n')
np.savetxt(r'C:\Users\alakb\Desktop\NLP HOMETASK POS TAGGING WITH HMM\final\emission.txt', df.values, fmt='%s')
