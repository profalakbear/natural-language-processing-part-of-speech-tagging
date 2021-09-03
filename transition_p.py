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
tags_count = 0
tag_b_given_a_p = []
insert = tuple()

def tagCount(sx):
    ctr = 0
    for i in range(len(array_of_tuple)):
        if array_of_tuple[i][1] == sx:
            ctr +=1
    return ctr

uz = len(tags_array)
uz_m = uz-1

result = 0
for i in range(1,uz_m):
    for j in range(1,uz_m):
        if tags_array[i]+" "+tags_array[j] == tags_array[j]+" "+tags_array[j+1]:
            tags_count+=1
    tag_a_count = tagCount(tags_array[i])
    if tags_count and tag_a_count != 0:
        result = tags_count/tag_a_count
    insert = (tags_array[i], tags_array[j], result)
    tag_b_given_a_p.append(insert)
    result = 0
    insert = tuple()



df = pd.DataFrame(tag_b_given_a_p, columns =['   TAG_A', '   TAG_B', '   TAG_B_given_a'])

f = open("transition_p.txt", "x")
f.write('TAG_A    TAG_B    TAG_B_given_a' '\n')
np.savetxt(r'C:\Users\alakb\Desktop\NLP HOMETASK POS TAGGING WITH HMM\final\transition_p.txt', df.values, fmt='%s')

print(tag_b_given_a_p)
