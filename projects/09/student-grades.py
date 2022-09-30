student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Excellent"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

def getGrade(score):
    if score > 90:
        return "Outstanding"
    if score > 80:
        return "Excellent"
    if score > 70:
        return "Acceptable"
    return "Fail"

for grade in student_scores:
    student_grades[grade] = getGrade(student_scores[grade])    

print(student_grades)
