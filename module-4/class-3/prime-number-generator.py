count = 0
for n in range(2, 1001):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        print(n)

print(f"Total Prime Numbers Between 1 to 1000 is - {count}")