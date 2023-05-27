def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def is_even(number):
    return number % 2 == 0

def count_even_numbers(numbers):
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
