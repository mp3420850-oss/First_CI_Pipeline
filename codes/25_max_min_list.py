
"""Program 25: Find maximum and minimum without max() or min()."""

def find_max_min(numbers):
    if not numbers:
        raise ValueError("List must not be empty")

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    try:
        largest, smallest = find_max_min(numbers)
        print("Maximum:", largest)
        print("Minimum:", smallest)
    except ValueError as error:
        print(error)
