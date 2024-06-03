"""
controller.py by Ryan Nicolas
Some functions to control our GPA calculator app
"""
# Functions
def get_gradegpa(grades: list) -> float:
    """Takes averages"""
    grade_points = sum(grades)
    class_amount = len(grades)
   
    if not grades:
        print("No grades available!")
   
    gpa = round((grade_points / class_amount),2)
    display = f"Your GPA is... {gpa}"
    return display
