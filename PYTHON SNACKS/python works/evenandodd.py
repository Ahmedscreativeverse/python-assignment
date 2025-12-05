
n = int(input("How many numbers do you want to enter? "))


sum_even = 0
sum_odd = 0

for i in range(n):
    num = int(input("Enter a number: "))
    
    
    if num % 2 == 0:
        sum_even = sum_even + num
    else:
        sum_odd = sum_odd + num


print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
