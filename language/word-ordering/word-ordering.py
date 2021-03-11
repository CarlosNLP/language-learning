from utils import *
from nltk.tokenize import word_tokenize
import sqlite3
import random

# Path and opening database
db_path = "../../docs/databases/books.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Selecting all the sentences from books categorized as level A1
cur.execute("SELECT sentence FROM books WHERE level = 'A1'")
sentences = cur.fetchall()

shuffled_sentences = []

for sentence in sentences:
    sentence_tokenized = word_tokenize(sentence[0]) # we do [0] because "sentence" is a tuple consisting of only one element/column from the database
    sentence_generated = generator(sentence_tokenized) # generating shuffled sentence
    shuffled_sentences.append(sentence_generated) # updating a list with shuffled sentences and the correct order


# Activity for the user
random_entry = random.randint(0, len(shuffled_sentences) - 1)

correct_sentence = sentences[random_entry][0]
shuffled_sentence = shuffled_sentences[random_entry]

print('Please put the words in the correct order. Remember to include punctuation, if any. Word capitalization is optional.')
print(shuffled_sentence[0], '\n')

answer = input()

if answer.strip().lower() == correct_sentence.strip().lower():
    print('Correct! Yay!')
else:
    print('Oh, I am afraid the answer is wrong...')
    print('Correct sentence:', correct_sentence)
