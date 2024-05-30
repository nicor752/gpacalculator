"""
controller.py by Ryan Nicolas
Some functions to control our GPA calculator app
"""
# imports

# Functions
def get_gradegpa(grade1: int, grade2: int, grade3: int, grade4: int, grade5: int, grade6: int, grade7: int, grade8: int) -> float:
    """Takes averages"""
    class_amount = 8
    gradegpa = round(((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 ) / (class_amount)),2)
    results = f"Your GPA is... {gradegpa}"
    return results
# Global scope
if __name__ == "__main__":
    results = get_gradegpa(4.00, 3.33, 3.54, 3.64, 3.82, 3.44, 3.21, 3.55)
    print(results)
