"""
Module to add function
"""

def add(a: float, b: float) -> float:
    """
    Function to add two numbers and return the result
    """

    result = a + b
    return result


if __name__ == "__main__":
    RESULT_ADD = add(10.0, 5.0)
    print(RESULT_ADD)
