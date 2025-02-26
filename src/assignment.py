# Grade Calculator Assignment
# This script calculates a student's academic standing based on their scores and assignment completion.

# Do not modify these test scores and settings
test_score = 85
exam_score = 78
all_assignments_completed = True

# TASK 1: Calculate the final score as the average of test_score and exam_score
# ===== YOUR CODE HERE =====

almost_final_score = test_score + exam_score
final_score = almost_final_score / 2
  # Replace None with the calculation

# ===== END YOUR CODE =====

# TASK 2: Determine if the student passed
# A student passes if their final_score is 60 or higher
# ===== YOUR CODE HERE =====

passed = final_score >= 50  # Set to True or False using an if statement

# ===== END YOUR CODE =====

# TASK 3: Assign a letter grade based on the final_score
# Score 90-100: "A"
# Score 80-89: "B"
# Score 70-79: "C"
# Score 60-69: "D"
# Score below 60: "F"
# ===== YOUR CODE HERE =====

letter_grade = "B"  # Set the letter grade using if-elif-else

# ===== END YOUR CODE =====

# TASK 4: Determine honor roll status
# To be on the honor roll, a student needs:
# - A final_score of 90 or higher
# - All assignments completed
# ===== YOUR CODE HERE =====

honor_roll = False
if final_score >= 90:
    print("False")

if final_score <= 90:
    print("True")
# Set to True or False using an if statement

# ===== END YOUR CODE =====

# TASK 5: Determine if the student can take the advanced course
# Students can take the advanced course if:
# - They passed (final_score >= 60)
# - AND they either:
#   - Have a letter grade of "A" OR
#   - Have a letter grade of "B" AND have completed all assignments
# ===== YOUR CODE HERE =====

can_take_advanced = True   # Set to True or False using if statements with AND/OR
if final_score >= 60:
    print("True")

if final_score <= 60:
    print("False")
# ===== END YOUR CODE =====

# This prints the results (do not modify)
print("Final Score:", final_score)
print("Passed:", passed)
print("Letter Grade:", letter_grade)
print("Honor Roll:", honor_roll)
print("Can Take Advanced Course:", can_take_advanced)