def grades_to_words(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.5:
        return "Good"
    elif grade < 5.5:
        return "Very Good"
    elif grade < 6:
        return "Excellent"



grade = float(input())
print(grades_to_words(grade))