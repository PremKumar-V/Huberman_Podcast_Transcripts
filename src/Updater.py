import os
import sqlite3


def transform_string(input_string):
    words = input_string.split("_")
    capitalized_words = [word.capitalize() for word in words]
    transformed_string = " ".join(capitalized_words)
    return transformed_string


def updater():
    conn = sqlite3.connect("files.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS files
                (id INTEGER PRIMARY KEY, filename TEXT)"""
    )

    folder_path = "data"
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    for file in files:
        c.execute("INSERT INTO files (filename) VALUES (?)", (transform_string(file),))

    conn.commit()
    conn.close()
