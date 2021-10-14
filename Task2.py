"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

highest_sec = None
telephone = ''

for second in calls:
    if highest_sec is None or int(second[3]) > highest_sec:
        highest_sec = int(second[3])
        telephone = second[1]


print(f"{telephone} spent the longest time, {highest_sec} seconds, on the phone during September 2016.")
