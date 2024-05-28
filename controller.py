"""
controller.py by Ryan Nicolas
Some functions to control our GPA calculator app
"""
# imports

# Functions
def get_gradegpa(grade1: int, grade2: int, grade3: int) -> float:
    """Takes averages"""
    class_amount = 3
    gradegpa = ((grade1 + grade2 + grade3) // (class_amount))
    results = f"Your GPA is... {gradegpa}"
    return results
# Global scope
if __name__ == "__main__":
    results = get_gradegpa(4.00, 3.33, 3.54)
    print(results)
