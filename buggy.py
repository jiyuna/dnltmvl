def divide_numbers(a, b):
    """Return a / b, or None if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def main():
    numbers = [10, 0, 5]
    for n in numbers:
        result = divide_numbers(100, n)
        if result is None:
            print("Cannot divide by", n, "- division by zero")
        else:
            print("100 divided by", n, "=", result)


if __name__ == "__main__":
    main()

