student_scores = [78, 85, 92, 300, 88, 74, 95, 80, 59, 91, 
                  83, 76, 97, 68, 89, 72, 500, 81, 66, 99,
                  200]

total_score = sum(student_scores)
max_score = max(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)

