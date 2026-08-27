def triangle(n):
    for row in range(1, n + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()


def multiplication_table(*numbers):
    for number in numbers:
        print("\nTable of", number)

        for i in range(1, 11):
            print(number, "x", i, "=", number * i)


def fibonacci(limit):
    numbers = []

    first = 0
    second = 1

    while first < limit:
        print(first, end=" ")
        numbers.append(first)

        next_number = first + second
        first = second
        second = next_number

    print()
    return numbers


def collatz(n):
    steps = 0

    while n != 1:

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps = steps + 1

    return steps


print("TRIANGLE")
triangle(5)

print("\nMULTIPLICATION TABLES")
multiplication_table(2, 5, 10)

print("\nFIBONACCI SERIES")
fib_numbers = fibonacci(50)
print("List:", fib_numbers)

print("\nCOLLATZ")
steps = collatz(27)
print("Steps:", steps)