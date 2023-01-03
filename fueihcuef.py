arr1 = [4, 5, 6]
arr2 = [5, 9, 8]
num3 = 0
num2 = 0
num1 = 0
num_rem = 0
index = -1

while index >= -3:
    temp_num = arr1[index] + arr2[index]
    print(temp_num)
    if index == -1:
        num3 = temp_num - 10
        num2 += temp_num // 10
    elif index == -2:
        num2 += temp_num - 10
        num1 += temp_num // 10
    elif index == -3:
        num1 += temp_num
    index -= 1
print(''.join([str(x) for x in [num1, num2, num3]]))