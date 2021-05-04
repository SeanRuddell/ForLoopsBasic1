# Basic - Print all integers from 0 to 150.
count = 0
while count < 151:
    print(count)
    count += 1

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5, 1001, 1):
    if x % 5 == 0:
        print(x)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else: 
        print(x)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
count = 0
while count < 500001:
    count += 1
    sum = sum + count
else:
    print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
count = 2018
while count >= 0:
    print(count)
    count -= 4

"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""
lowNum = 22
highNum = 690
mult = 8
for x in range(lowNum, highNum, mult):
        print(x)