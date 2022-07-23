import re
import os

deathline = 0
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

path = input("Where is the filepath with the duplicate?: ")
newfile = input("Where do you wanna store the new file without the duplicate?: ")
#path = "C:/Users/denny/OneDrive/Desktop/wetransfer_duplicate-finder-py_2022-07-22_1935/asturleonese.txt"
assert os.path.exists(newfile), "The path entered was invalid"
assert os.path.exists(path), "The path entered was invalid"
with open(path, encoding="utf8") as textfile:
    textlines = [x.rstrip() for x in textfile]

def new_file(chardict):
        for character in chardict:
            try:
                if len(chardict[character]) > 1:
                    #print(character +" appears on these lines:" + str(list(chardict[character])[-1]))
                    lin1 = list(chardict[character])[-1]
                    readblock(lin1)
                else:
                    #print(character +" appears on these lines single:" + str(list(chardict[character])[0]))
                    readblock(list(chardict[character])[0])
            except:
                break



def readblock(line):
    z = 1
    x = 0
    word = '{'
    word2 = '}'
    with open(newfile, 'a', encoding='utf-8') as f:
        while z >= 1:
            intline = int(line) - 1
            row = open(path, encoding= 'UTF8').readlines()[intline + x]
            f.write(row)
            x = x +1
            if word in row:
                z = z + 1
            if word2 in row:
                z = z -1
            if z == 1:
                f.close
                break
        


#character is the id
new_file(charfinder(textlines))
print("File is ready!")
#dupefinder(charfinder(textlines))


#NonSon0Italian0#6450