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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


text_set = set()
call_set = set()

for text in texts:
    text_set.add(text[1])
    text_set.add(text[2])

for call in calls:
    call_set.add(call[1])
    call_set.add(call[2])

total = len(text_set) + len(call_set)
print(f"There are {total} different telephone numbers in the records.")
