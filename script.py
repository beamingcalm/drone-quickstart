def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: Average value.

    """
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def is_even(number):
    """
    Check if a number is even.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if the number is even, False otherwise.

    """
    return number % 2 == 0

def count_even_numbers(numbers):
    """
    Count the number of even numbers in a list.

    Args:
        numbers (list): List of numbers.

    Returns:
        int: Count of even numbers.

    """
    count = 0
    for number in numbers:
        if is_even(number):
            count += 1
    return count

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    average = calculate_average(numbers)
    print(f"Average: {average}")
    even_count = count_even_numbers(numbers)
    print(f"Number of even numbers: {even_count}")
