import sqlite3
import os
from nltk.tokenize import word_tokenize, sent_tokenize

# Path and opening database
db_path = "../../docs/databases/books.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Creating table if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS "books" (
            "sentence"    TEXT,
            "level"  TEXT,
            "book"  TEXT
            );""")


# Retrieving files to be processed (TXT files with book's content)
books_folder = "../../docs/books/"

fileList = []
for root, dirs, files in os.walk(books_folder):
    for name in files:
        if name.endswith('.txt'):
            fileList.append(os.path.join(root, name))

print('Number of books:', len(fileList))

print('Converting books into database model...')
for file in fileList:
    with open(file, 'r', encoding="utf-8") as open_file:
        content = open_file.read()

        # Getting language level
        if "books/a1" in file:
            level = "A1"
        elif "books/a2" in file:
            level = "A2"
        elif "books/b1" in file:
            level = "B1"
        elif "books/b2" in file:
            level = "B2"
        elif "books/c1" in file:
            level = "C1"
        elif "books/c2" in file:
            level = "C2"

        # Getting book name
        base = os.path.basename(file)
        book = os.path.splitext(base)[0]
        
        for sentence in sent_tokenize(content):
            # Inserting entries into our database
            cur.execute("INSERT INTO books VALUES (?, ?, ?)", (sentence, level, book))

    # Committing the change into the database
    conn.commit()

print('Process finished.')

# Closing database connection
cur.close()
conn.close()
