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

#region Calculate tag probablity of tags
count_for_tag=0
tag_frequency = [] 
new_tuple = tuple()

for i in range(len(array_of_tuple)):
  for j in range(len(array_of_tuple)):
    if array_of_tuple[i][1] == array_of_tuple[j][1]:
      count_for_tag += 1

  new_tuple = (array_of_tuple[i][1],count_for_tag)
  tag_frequency.append(new_tuple)
  count_for_tag = 0
  new_tuple = tuple()
#endregion

df = pd.DataFrame(tag_frequency, columns =['   TAG', '   TAG FREQUENCY'])
#print(df)

f = open("posTags.txt", "x")
f.write('TAG TAG_FREQUENCY \n')
np.savetxt(r'C:\Users\alakb\Desktop\NLP HOMETASK POS TAGGING WITH HMM\final\posTags.txt', df.values, fmt='%s')