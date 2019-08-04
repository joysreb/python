def numbers(num1,num2):
    if num1==num2 or abs(num1-num2)==5 or (num1+num2)==5:
        return True
    else:
        return False







print(numbers(7,2))
print(numbers(3,2))
print(numbers(1,1))
print(numbers(6,2))
