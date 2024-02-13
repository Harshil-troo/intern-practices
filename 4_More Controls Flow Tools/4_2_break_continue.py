"""
for n in range(2, 10):
    for x in range(2, n):
          if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
"""
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
"""
"""
for number in range(10):
    if number == 5:
        # break
        print('Number is ' + str(number))
        print('Out of loop')
        break

print('Number is ' + str(number))
"""
