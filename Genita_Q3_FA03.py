students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
subjects = ["Math", "English", "Science"]

scores = [
    [67, 96, 89],
    [88, 81, 89],
    [41, 67, 78],
    [92, 89, 94],
    [81, 76, 84]
]


print("Student Scores:")
print(scores)
print()

# each students total score & average
for i in range(len(scores)):
    print(students[i])
    print(scores[i])

    total = sum(scores[i])
    average = total / len(scores[i])

    print("Total:", total)
    print("Average:", average)
    print()

# highest score
max_score = scores[0][0]

for i in range(len(scores)):
    for j in range(len(scores[i])):
        if scores[i][j] > max_score:
            max_score = scores[i][j]

print("Highest score in the class:", max_score)

