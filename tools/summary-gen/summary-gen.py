import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """The Asgardian Loki encounters the Other, the leader of an extraterrestrial race known as the Chitauri. In exchange for retrieving the Tesseract,[c] a powerful energy source of unknown potential, the Other promises Loki an army with which he can subjugate Earth. Nick Fury, director of the espionage agency S.H.I.E.L.D., arrives at a remote research facility, where physicist Dr. Erik Selvig is leading a team experimenting on the Tesseract. The Tesseract suddenly activates and opens a wormhole, allowing Loki to reach Earth. Loki steals the Tesseract and uses his scepter to enslave Selvig and other agents, including Clint Barton, to aid him.

In response, Fury reactivates the "Avengers Initiative". Agent Natasha Romanoff heads to Kolkata to recruit Dr. Bruce Banner to trace the Tesseract through its gamma radiation emissions. Fury approaches Steve Rogers to retrieve the Tesseract, and Agent Phil Coulson visits Tony Stark to have him check Selvig's research. Loki is in Stuttgart, where Barton steals the iridium needed to stabilize the Tesseract's power, leading to a confrontation with Rogers, Stark, and Romanoff that ends with Loki's surrender. While Loki gets escorted to S.H.I.E.L.D., his adoptive brother Thor arrives and frees him, hoping to convince him to abandon his plan and return to Asgard. Stark and Rogers intervene and Loki is taken to S.H.I.E.L.D.'s flying aircraft carrier, the Helicarrier, where he is imprisoned."""

stopWords = list(STOP_WORDS)

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

word_freq = {}
for word in doc:
    if word.text.lower() not in stopWords and word.text.lower() not in punctuation:
        if word.text not in word_freq:
            word_freq[word.text] = 1
        else:
            word_freq[word.text] += 1
# print(word_freq)

max_freq = max(word_freq.values())
# print(max_freq)

for word in word_freq.keys():
    word_freq[word] =   word_freq[word]/max_freq
# print(word_freq)

sent_tokens = [sent for sent in doc.sents]
# print(sent_tokens)

sent_score = {}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq.keys():
            if sent not in sent_score:
                sent_score[sent] = word_freq[word.text]
            else:
                sent_score[sent] += word_freq[word.text]

# print(sent_score)

select_len = int(len(sent_tokens) * 0.3)
# print(select_len)

summary = nlargest(select_len, sent_score, key=sent_score.get)
# print(summary)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
# print(text)
# print("----------------------")
# print(final_summary)

print("Length of original text: ", len(text.split(' ')))
print("Length of summary text: ", len(summary.split(' ')))
                 