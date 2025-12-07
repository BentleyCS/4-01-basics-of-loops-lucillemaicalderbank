#All questions must use a loop for full points.
from T2.CSP_4_01_Basics_of_Loops import result


def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
result=""

for i in range (1,n+1):
    if i%2==1:
        if result:
            result+=""
        result+=str(i)
    return result

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
if n<1:
    return
for i in range(n,0,-1):
    print(i,end="")


def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    num=0
    while num!=10:
        num=random.randint(1,10)
        print(num)
        tries+=1
    print(f"it took {tries} tries to get a 10")
def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    if n<=0
        print(Give a positive number)
        return
    lowest=100
    highest=1
    for _ in range(n):
        num=random.randint(1,100)
        print(f"rolled:{num}")
        if num>highest:
            highest=num
        if num<lowest:
            lowest=num

    print(f"Highest number rolled= {highest}")
    print(f"Lowest number rolled= {lowest}")
def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    reversed_word=""
    for character in word:
        reversed_word=character+reversed_word
    return reversed_word

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            result+="fizzbuzz"
        elif i%3==0:
            result+="fizz"
        elif i%5==0:
            result+=str(i)+""
    return result.strip()

def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    if n<=0:
        return
    while n!=1:
        print(n,end="->")
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
    print(n)


def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n<=0:
        return""
    elif n==1:
        return"0"
    fibonacciseq=[0,1]
    while len(fibonacciseq)<n:
        nextnum=fibonacciseq[-1]+fibonacciseq[-2]
        fibonacciseq.append(nextnum)

    return"".join(str(num) for num in fibonacciseq[:n])

print(fibonacci(300))