'''
This is the scoring criteria: 
- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 
'''
student_scores = {
    'Harry': 88, #"Exceeds Expectations" 
    'Ron': 78, #"Acceptable" 
    'Hermione': 95, #Outstanding
    'Draco': 75, #Acceptable
    'Neville': 60 #Fail
}

student_grades = {}
for student in student_scores:
    student_grade = student_scores[student]
    if student_grade >= 91 and student_grade <= 100:
        student_grades[student] = "Outstanding"
    elif student_grade >= 81 and student_grade <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_grade >= 71 and student_grade <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)