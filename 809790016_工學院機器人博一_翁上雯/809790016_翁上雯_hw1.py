#Quesetion1:
print("\n====Question1: [set]====")
math_passed = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
english_passed = {'John', 'Mary', 'Tony', 'Bob', 'Pony', 'Tom', 'Alice'}
math_passed_eng_failed = math_passed - english_passed
math_failed_eng_passed = english_passed - math_passed
math_passed_eng_passed = math_passed & english_passed
students = math_passed | english_passed
total_students = len(students)

print("math_passed_eng_failed = ", math_passed_eng_failed)
print("math_failed_eng_passed = ", math_failed_eng_passed)
print("math_passed_eng_passed = ", math_passed_eng_passed)
print("total number of students = ", total_students)


#Question2:
print("\n====Question2: [dict, list]====")
scores = {"Tom": [80, 100, 90, 95], "John": [100, 93, 75, 80]}
for key in scores:
    sum = 0
    for num in scores[key]:
        sum += num
    size = len(scores[key])
    avg_score = sum / len(scores[key])
    print(key,"'s score average = ", avg_score)
