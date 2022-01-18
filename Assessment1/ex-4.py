import math

numbers = input("Enter the value for D:")
numbers = numbers.split(',')
#print(numbers)
result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)
