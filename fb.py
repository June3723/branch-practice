for i in range(1,15+1):
    if i % 5 == 0:
        print('Buzz' * (i % 5 == 0))
    elif i % 3 == 0:
        print('Fizz' * (i % 3 == 0))
    elif i % 15 == 0:
        print('FizzBuzz' * (i % 15 == 0))
    else:
        print(f'{i}')


