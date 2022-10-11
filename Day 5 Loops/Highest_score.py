# 🚨 Don't change the code below 👇
from pickle import HIGHEST_PROTOCOL

from pygments import highlight


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#print(max(student_scores))



#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
         highest_score = score

print(f"The higheest score in the class is: {highest_score}")
