
"""Program 28: Find the intersection of two collections."""

def set_intersection(first, second):
    return list(set(first) & set(second))


if __name__ == "__main__":
    first = list(map(int, input("Enter first numbers separated by spaces: ").split()))
    second = list(map(int, input("Enter second numbers separated by spaces: ").split()))
    print("Intersection:", set_intersection(first, second))
