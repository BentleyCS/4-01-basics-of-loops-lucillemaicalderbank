import random

# All questions must use a loop for full points.

def oddNumbers(n):
    result = ""
    for i in range(1, n + 1):
        if i % 2 == 1:
            if result != "":
                result += " "
            result += str(i)
    return result


def backwards(n):
    if n < 1:
        return ""

    result = ""
    for i in range(n, 0, -1):
        if result != "":
            result += " "
        result += str(i)
    return result


def randomRepeating():
    tries = 0
    num = 0

    while num != 10:
        num = random.randint(1, 10)
        print(num)
        tries += 1

    print("It took", tries, "tries to get a 10")


def randomRange(n):
    if n <= 0:
        print("Give a positive number")
        return

    lowest = 100
    highest = 1

    for i in range(n):
        num = random.randint(1, 100)
        print("rolled:", num)

        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    print("Highest number rolled =", highest)
    print("Lowest number rolled =", lowest)


def reverse(word):
    reversed_word = ""
    for character in word:
        reversed_word = character + reversed_word
    return reversed_word


def fizzBuzzContinuous(n):
    result = ""

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            value = "fizzbuzz"
        elif i % 3 == 0:
            value = "fizz"
        elif i % 5 == 0:
            value = "buzz"
        else:
            value = str(i)

        if result != "":
            result += " "
        result += value

    return result


def collatz(n):
    if n <= 0:
        return

    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)


def fibonacci(n):
    if n <= 0:
        return ""
    if n == 1:
        return "0"

    result = "0 1"
    a = 0
    b = 1
    count = 2

    while count < n:
        c = a + b
        result += " " + str(c)
        a = b
        b = c
        count += 1

    return result