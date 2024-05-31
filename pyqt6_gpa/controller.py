"""
controller.py by Ryan Nicolas
Some functions to control our GPA calculator app
"""
# imports

# Functions
def get_gradegpa(grades: list) -> float:
    """Takes averages"""
    class_amount = len(grades)
    results = f"Your GPA is... {gradegpa}"
    return results
# Global scope
if __name__ == "__main__":
    results = get_gradegpa(4.00, 3.33, 3.54, 3.64, 3.82, 3.44, 3.21, 3.55)
    print(results)
