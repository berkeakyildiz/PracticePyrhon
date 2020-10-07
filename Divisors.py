num = int(input("Enter a number\n"))

array = list(range(2, num + 1))
print(array)
divisors = []

for i in array:
    if(num % i == 0):
        divisors.append(i)

print(divisors)