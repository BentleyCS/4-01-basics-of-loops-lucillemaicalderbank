import random

def oddNumbers(n):
    result = ""
    for i in range(1, n + 1):
        if i % 2 == 1:
            if result:
                result += " "
            result += str(i)
    return result


def backwards(n):
    if n < 1:
        return ""

    result = ""
    for i in range(n, 0, -1):
        if result:
            result += " "
        result += str(i)
    return result


def reverse(word):
    result = ""
    for char in word:
        result = char + result
    return result


def randomRepeating():
    tries = 0
    num = 0
    result = ""

    while True:
        num = random.randint(1, 10)
        if result:
            result += " "
        result += str(num)
        tries += 1
        if num == 10:
            break

    result += " It took " + str(tries) + " tries to get a 10"
    return result


def randomRange(n):
    if n <= 0:
        return "Give a positive number"

    lowest = 100
    highest = 1
    result = ""

    for _ in range(n):
        num = random.randint(1, 100)
        result += "rolled: " + str(num) + "\n"

        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    result += "Highest number rolled = " + str(highest) + "\n"
    result += "Lowest number rolled = " + str(lowest)
    return result


def fizzBuzzContinuous(n):
    result = ""

    for i in range(1, n + 1):
        if i % 15 == 0:
            value = "fizzbuzz"
        elif i % 3 == 0:
            value = "fizz"
        elif i % 5 == 0:
            value = "buzz"
        else:
            value = str(i)

        if result:
            result += " "
        result += value

    return result


def collatz(n):
    if n <= 0:
        return ""

    result = ""
    while True:
        if result:
            result += " "
        result += str(n)

        if n == 1:
            break
        elif n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

    return result


def fibonacci(n):
    if n <= 0:
        return ""
    if n == 1:
        return "0"

    result = "0 1"
    a, b = 0, 1
    count = 2

    while count < n:
        c = a + b
        result += " " + str(c)
        a, b = b, c
        count += 1

    return result
