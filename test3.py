print("These are the scores of a class: ")
scores = {"Luke" : 44,"Eva" : 80, "Jess" : 51,"Charlie" : 97,"Jack" : 26}
print(scores)
total_sum = 0
total_student = 0
for name, grade in scores.items():
    total_sum = total_sum + grade
    total_student = total_student + 1
avg = total_sum / total_student
print("The average of this class is: ", avg)
if avg >= 50:
    print("This class has passed!")
else:
    print("This class has not passed")

a = str(input("Which student would you want to look for?"))
for name in scores:
    if a == name:
        print("Student Found")
    else:
        print("Sorry! Student not found!")