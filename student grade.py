def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding performance "
    elif marks >= 80:
        return "B", "Very Good! Keep it up "
    elif marks >= 70:
        return "C", "Good job! You can do even better "
    elif marks >= 60:
        return "D", "You passed! Work a little harder "
    else:
        return "F", "Don't give up! Try again "

print(" STUDENT GRADE CALCULATOR ")
name = input("Enter student name: ")
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print(" Invalid marks! Please enter between 0 and 100.")
        else:
            break
    except ValueError:
        print(" Invalid input! Please enter numbers only.")
grade, message = calculate_grade(marks)