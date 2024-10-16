'''
    Lesson: Else if
    Author: Mr. Kalisz
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024
'''

# If Review

num = 15

if num < 20:
    print("run if")

#Else review

num = 25

if num < 20:
    print("run if")
else:
    print("run else")

#Else if

num = 25

#Only one of these conditions can run.
if num < 20: # num < 20
    print("run if")
elif num < 30: #not (num < 20) and num < 30
    #num >= 20 and num < 30
    print("first elif")
elif num < 40: #not (num < 20) and not (num < 30) and num < 40
    #num >= 20 and num >= 30 and num < 40
    #num >= 30 and num < 40
    print("second elif")
else: #num >= 40
    print("run else")

#Unreachable conditions

if num < 50: 
    print("run if")
elif num < 20: #num >= 50 and num < 20 -> unreachable because it can never be true
    print("first elif")
elif num == 25:
    print("second elif")

#Most specific conditions to least specific
#Smaller range to Larger range

if num == 25: #only 1 number satsifies this condition 
    print("run if")
elif num < 20: #Because it has 30 less than numbers than the next condition
    print("first elif")
elif num < 50: #incluedes everything from num < 20 AND 20-49
    print("second elif")