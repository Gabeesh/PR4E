#PR4E
#Author: Md Akil Mahmod Tipu
#Email: amtipu.bb@gmail.com

#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#  X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def computeAverage(fh):
    average = None
    count = 0
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:") :
            count = count + 1
            columnPos = line.find(":")
            number = line[columnPos+1::1]
            snumber = number.lstrip()
            if average is None:
                average = 0
            snumber = float(snumber.rstrip())
            average = ( (average * ((count -1)) + snumber) / count )
    return average

fh = openfile()
print "Average spam confidence:", computeAverage(fh)