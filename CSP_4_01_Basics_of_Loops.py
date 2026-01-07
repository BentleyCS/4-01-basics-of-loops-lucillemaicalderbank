import random

# All questions must use a loop for full points.

def oddNumbers(n):
    result = ""
    for i in range(1, n + 1):
        if i % 2 == 1:
            if result:
                result += " "
            result += str(i)
    return result


def backwards(n):
    result = ""
    for i in range(n, 0, -1):
        if result:
            result += " "
        result += str(i)
    return result


def randomRepeating():
    tries = 0
    result = ""

    while True:
        num = random.randint(1, 10)
        tries += 1
        result += str(num) + " "
        if num == 10:
            break

    result += f"It took {tries} tries to get a 10"
    return result


def randomRange(n):
    if n <= 0:
        return "Give a positive number"

    lowest = 100
    highest = 1
    result = ""

    for _ in range(n):
        num = random.randint(1, 100)
        result += f"rolled: {num}\n"

        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    result += f"Highest number rolled = {highest}\n"
    result += f"Lowest number rolled = {lowest}"
    return result


def reverse(word):
    reversed_word = ""
    for character in word:
        reversed_word = character + reversed_word
    return reversed_word


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
    while n != 1:
        result += str(n) + " -> "
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    result += "1"
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
