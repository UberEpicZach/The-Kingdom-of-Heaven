import re
import os

#function to find ck3 characters in the history files
def charfinder(textlines):
    linenum = 0
    chardict = dict()
    for line in textlines:
        linenum = linenum + 1
        match = re.search("^\d+ = \{", line)
        if match:
            character = match.string[:-4]
            if character not in chardict:
                chardict[character] = list() 
            chardict[character].append(str(linenum))
    return chardict

#function to find all characters in the list which appear on >1 lines
def dupefinder(chardict):
    for character in chardict:
        if len(chardict[character]) > 1:
            print(character +" appears on these lines:" + str(chardict[character])[1:-1])

path = input("enter the filepath for the character history file you want to check: ")
assert os.path.exists(path), "The path entered was invalid"
with open(path, encoding="utf8") as textfile:
    textlines = [x.rstrip() for x in textfile]

dupefinder(charfinder(textlines))
