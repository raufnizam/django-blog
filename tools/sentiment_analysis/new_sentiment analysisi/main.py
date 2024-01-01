import string
from collections import Counter

import matplotlib.pyplot as plt

text = open('read.txt',encoding='utf-8').read()

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

tokenized_text = text.split()
print(tokenized_text)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


final_words = []
for word in tokenized_text:
    if word not in stop_words:
        final_words.append(word)

# print(final_words)

emotion_list = []
with open('emotions.txt', 'r') as f:
    for line in f:
        clean_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clean_line.split(':')
        print("Word: " + word + " , " + "Emotion: " + emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
emotion_list = Counter(emotion_list)
print(emotion_list)
