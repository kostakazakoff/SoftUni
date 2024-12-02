divisor = int(input())
boundary = int(input())
# Check the numbers in the reverse order, keeping system resources (the maximum multiple number is obviously in the last positions of the boundary):
for n in range(boundary, divisor, -1):
    if n % divisor == 0:
        break
print(n)
