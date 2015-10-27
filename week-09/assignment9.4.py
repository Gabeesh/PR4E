#PR4E
#Author: Md Akil Mahmod Tipu
#Email: amtipu.bb@gmail.com

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def doCount(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    counts[line[1]] = counts.get(line[1],0) + 1
    return counts

def max(dictionary):
    max = None 
    highest = None
    #print the  dictionary
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    #print "new maximum is", max
	    highest = key
    return highest

fh = openFile()
sw = startsWith()

dictionary = doCount(fh,sw)
key = max(dictionary)
print key, dictionary[key]