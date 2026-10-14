"""Program 30: Convert a decimal integer to binary without bin()."""

def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    return binary


if __name__ == "__main__":
    number = int(input("Enter a non-negative decimal integer: "))

    try:
        print("Binary:", decimal_to_binary(number))
    except ValueError as error:
        print(error)