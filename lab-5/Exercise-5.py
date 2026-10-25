#Exercise-2
"""
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

#1
def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid Marks"

    return sum(marks) / len(marks)
#2
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
#3
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

        average = calculate_average(marks)

        if average == "Invalid Marks":
            print(student_id, name, "Invalid Marks", "Not Classified")
            continue

        category = classify_performance(average)

        print(student_id, name, round(average, 2), category)

#testing
display_report(students)

print("Testing empty marks:")
print(calculate_average([]))

print("Testing invalid marks:")
print(calculate_average([70, -5, 80]))

print("Testing tied averages:")
print(calculate_average([80, 80, 80]))

"""
#Exercise-1


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


#1. Display all resources
def display_resources(resources):
    if len(resources) == 0:
        print("No resources available.")
        return

    for resource in resources:
        print("ID:", resource[0])
        print("Name:", resource[1])
        print("Category:", resource[2])
        print("Available Quantity:", resource[3])
      


#2. Search resources by category
def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if found == False:
        print("No resources found in this category.")


#3. Find resources with zero available quantity

def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if found == False:
        print("All resources are available.")


# Testing 
print("all resources")
display_resources(resources)

print("Audio resource")
search_by_category(resources, "Audio")

print("Unavailable")
find_unavailable(resources)


