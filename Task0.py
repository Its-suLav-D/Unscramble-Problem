"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

for number in texts:
    print(
        f"First record of texts, {number[0]} texts {number[1]} at time {number[2]}")

for number in calls:
    print(
        f"Last record of calls, {number[0]} calls {number[1]} at time {number[2]}, lasting {number[3]} seconds")
