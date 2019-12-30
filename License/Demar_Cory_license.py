# Programmer: Cory DeMar
# ComSc 20
# Assognment #14
# Part 2: Driver’s License Exam
# 4-26-17

#for debugging, prompt for name of student input file

correct = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
           'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
num_correct = 0
student = []
answered_wrong = []
text_file = input("Enter the txt file: ")
filename = open(text_file, 'r')

for line in filename:
    student.append(line.strip())  
filename.close()

for i in range(len(correct)):
    if correct[i] == student[i]:
        num_correct += 1
    else:
        answered_wrong.append(i + 1) # question numbers start with 1 for people

num_incorrect = 20 - num_correct

print("Number of correct answes:", num_correct)
print("Number of incorrect answers:", num_incorrect)
if num_correct >= 15:
    print("you passed the test.")
else:
    print("you did not pass the test.")
if num_correct == 20:
    print("you did not miss any questions.")
else:
    print("Questions answered incorrectly: ", end='')
    wrong = ''
    for item in answered_wrong:
        wrong = wrong + str(item) + ', '
    wrong = wrong[0:-2] # get rid of last comma and blank
    print(wrong)
