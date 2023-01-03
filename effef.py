num = 123456789


num_2 = 0

while num > 10:
    num_2 += num % 10
    num //= 10
print(num_2 + num)