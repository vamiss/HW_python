num = int(input())

print(((num % 100) % 10) * 100 + ((num % 100) // 10) * 10 + (num // 100))
