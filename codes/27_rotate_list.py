
"""Program 27: Rotate a list right by k positions."""

def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)
    return items[-k:] + items[:-k] if k else items.copy()


if __name__ == "__main__":
    items = input("Enter items separated by spaces: ").split()
    k = int(input("Enter rotation count (k): "))
    print("Rotated list:", rotate_list(items, k))
