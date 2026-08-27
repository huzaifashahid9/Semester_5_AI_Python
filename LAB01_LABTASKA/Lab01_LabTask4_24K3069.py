def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def digit_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n

    return total


def classify(n, threshold=100):
    if n < threshold:
        return "small"
    else:
        return "large"


def summarise(*numbers):

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:

        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

        total += number

    average = total / len(numbers)

    return {
        "smallest": smallest,
        "largest": largest,
        "average": average
    }


def describe(**details):

    for key in details:
        print(key, ":", details[key])

    return None


for number in range(1, 11):
    if is_prime(number):
        print(number, "is prime")


print("\nDigit sum:", digit_sum(1234))

print("\nClassify with default:", classify(50))

print("Classify positionally:", classify(150, 120))

print("Classify with keyword:", classify(150, threshold=200))

result = summarise(10, 25, 5, 40, 15)
print("\nSummary:", result)

print("\nDetails:")
describe(name="Nadeem", age=28)