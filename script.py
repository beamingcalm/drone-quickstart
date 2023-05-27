"""
This script demonstrates calculating.
"""

def calculate_average(nums):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: Average value.
    """
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)

def is_even(number):
    """
    Check if a number is even.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

def count_even_numbers(nums):
    """
    Count the number of even numbers in a list.

    Args:
        numbers (list): List of numbers.

    Returns:
        int: Count of even numbers.
    """
    count = 0
    for number in nums:
        if is_even(number):
            count += 1
    return count

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    average = calculate_average(nums)
    print(f"Average: {average}")
    EVEN_COUNT = count_even_numbers(nums)
    print(f"Number of even numbers: {EVEN_COUNT}")
