# Create a program to read a file which contains large set of some noval.
# Get the frequencies of all words in the file and finally show the frequencies
# for each word in a pandas dataframe.

import pandas as pd
import re
from collections import Counter


def word_filter(worddata):
    return re.findall(r"\b[\w’-]+\b", worddata.lower())


def word_count(worddata):
    return Counter(worddata)

try:
    #Open the Novel file
    with open("novel.txt", "r", encoding="utf8") as file:
        file_data = file.read()
except FileNotFoundError:
    print("'Novel.txt' file not found.")
#Filter the word data
word_data = word_filter(file_data)
word_count_data = word_count(word_data)

# Final dataframe
print(pd.DataFrame(list(word_count_data.items()), columns=["Word", "Count"]))