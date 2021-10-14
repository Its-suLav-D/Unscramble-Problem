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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

nonDuplicate = set()


def add_fixed_line(bracket):
    spllited_string = list(bracket)
    right = 0
    for char in range(len(spllited_string)):
        if spllited_string[char] == ")":
            right = char

        nonDuplicate.add(bracket[1:right])


def add_telephone(phone):
    splitted_string = phone.split(" ")
    nonDuplicate.add(splitted_string[0])


def add_landline(landline):
    nonDuplicate.add(landline[:4])


def run_program():
    fixed_call_count = 1
    total_calls = 0
    for count, call in enumerate(calls):
        if '080' in call[0]:
            fixed_call_count += 1
            print(call[0])
            if call[1].startswith('('):
                add_fixed_line(call[1])

            elif " " in call[1]:
                add_telephone(call[1])

            else:
                add_landline(call[1])
        total_calls = count
    return fixed_call_count, total_calls


if __name__ == "__main__":
    fixed_call, total_call = run_program()
    sorted_list = sorted(nonDuplicate)

    print("The numbers called by people in have codes:")
    for item in sorted_list:
        print(item)
    print("**********************************************")

    print("Part B")
    percent = (fixed_call / total_call) * 100
    print(f"{round(percent,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore")
