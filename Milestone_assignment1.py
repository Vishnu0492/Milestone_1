import pandas as pd
import re
from collections import Counter

#Function to read CSV
df=pd.read_csv(r'C:\Users\Administrator\Desktop\UST_Training\Day10\Novel.csv')
#Combine all rows in to specific large string
text_data=' '.join(df.astype(str).values.flatten())
text_data=re.sub(r'[a-zA-Z\s]','',text_data)
#remove non alpha character
text_data=text_data.lower()
    
#tokanize word into text
word=text_data.split()
word_counts=Counter(word)
word_frequencies=pd.DataFrame(word_counts.items(),columns=['word','Frequency'])
word_frequencies=word_frequencies.sort_values(by='Frequency',ascending=false)
print(word_frequencies)
