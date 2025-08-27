def calculate_average(numbers):
    """Return the arithmetic mean of numbers, or None if input is empty.

    Accepts any iterable of numbers; converts to list once to support len().
    """
    numbers_list = list(numbers)
    if len(numbers_list) == 0:
        return None
    total = 0
    for value in numbers_list:
        total += value
    return total / len(numbers_list)


def main():
    data = [10, 20, 30, 40, 50]
    avg = calculate_average(data)
    print("Average is:", avg)

    empty_data = []
    empty_avg = calculate_average(empty_data)
    if empty_avg is None:
        print("Average of empty list is: undefined (no data)")
    else:
        print("Average of empty list is:", empty_avg)


if __name__ == "__main__":
    main()

