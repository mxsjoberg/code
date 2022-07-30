# Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# https://projecteuler.net/problem=17

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def parse_number(word_lst, n):
    number = str(n)
    size = len(number) - 1
    for i in range(len(number)):
        digit = number[i]
        # convert to teens
        if size == 1 and int(digit + number[i + 1]) in words:
            if i > 0: word_lst.append('and')
            word_lst.append(words[int(digit + number[i + 1])])
            break
        # convert to tens
        elif size == 1 and int(digit + '0') in words:
            if i > 0: word_lst.append('and')
            word_lst.append(words[int(digit + '0')])
        else:
            if int(digit) > 0:
                word_lst.append(words[int(digit)])
        # thousands
        if size == 3:
            word_lst.append(words[1000])
            break
        # hundreds
        if size == 2:
            word_lst.append(words[100])
        size -= 1
    return word_lst

assert parse_number([], 342) == ['three', 'hundred', 'and', 'forty', 'two']
assert parse_number([], 115) == ['one', 'hundred', 'and', 'fifteen']

assert sum(list(map(len, parse_number([], 342)))) == 23
assert sum(list(map(len, parse_number([], 115)))) == 20

# numbers = []
letters = 0
n = 1
while n < len(range(1000)) + 1:
    # number = parse_number([], n)
    # numbers.append(number)
    letters += sum(list(map(len, parse_number([], n))))
    n += 1

print(letters)
# 21124