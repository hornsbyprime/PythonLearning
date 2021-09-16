def hello(name):

    print('Hello ' + name)
hello('Matt')
hello('James')
def add(var1, var2):
    print(var1 + var2)
add(4, 7)
def oddOrEven(num):
    if num%2 == 0:
        print('Even')
    else:
        print('Odd')
oddOrEven(8)
def fizzBuzz(fizzRange):
    for i in range(fizzRange):
        if i%3 == 0:
            if i%5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
fizzBuzz(50)

