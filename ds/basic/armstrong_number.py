num = int(input("enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"Yes its armstrong number")
else:
    print(num,"no its not an armstrong number")