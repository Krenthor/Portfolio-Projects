# fibinacci

def fib(num):
    first = 0
    second = 1
    count = 0
    temp = 0

    while count <= num:
        print(first)
        temp = first + second
        first = second
        second = temp
        count = count + 1
fib(10)
