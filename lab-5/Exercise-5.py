students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    if len(marks) == 0:
        return None

    return sum(marks) / len(marks)

def classify_performance(average):
    if average is None:
        return "No Marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(students):
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        if len(marks) == 0:
            average = calculate_average(marks)
            category = classify_performance(average)
            print(student_id, name, "No Marks", category)
            continue

        if any(mark < 0 or mark > 100 for mark in marks):
            print(student_id, name, "Invalid Marks", "Not Classified")
            continue

        average = calculate_average(marks)
        category = classify_performance(average)

        print(student_id, name, round(average, 2), category)

display_report(students)