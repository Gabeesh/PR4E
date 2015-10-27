#PR4E
#Author: Md Akil Mahmod Tipu
#Email: amtipu.bb@gmail.com

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None

while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done': 
        break

    try:
        num = int(inp)
    except:
        print 'Invalid input'
        continue                            

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

print 'Maximum is', largest
print 'Minimum is', smallest