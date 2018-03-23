'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
Using the attached words.txt file, a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
What is the largest square number formed by any member of such a pair?
Please note: All anagrams formed must be contained in the given text file.
'''

# import csv module for parsing the file
import csv

# open words.txt file
wordlist = open("./words.txt", "r")

# csvreader = csv.reader(wordlist)

with open('words.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    words = []
    for word in readCSV:
        words.append(word)

    print(words)

# With open(‘words.txt’, ‘rb’) as f:
# reader = csv.reader(f)
# for row in reader:
# print row