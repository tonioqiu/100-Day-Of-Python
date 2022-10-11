from functools import total_ordering
import numbers
from re import S
from turtle import st


student_heights = input("Input a list of student heights, separated by space").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


#total_height = sum(student_heights)    
#average_heights = total_height/len(student_heights)

total_height = 0
for height in student_heights:
    total_height += height

numbers_of_student = 0
for student in student_heights:
    numbers_of_student += 1

average_heights = total_height/numbers_of_student
print (average_heights)