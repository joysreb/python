def sum(x,y,z):
    sum=x+y+z
    if (x==y==z):
      sum=sum*3
      return sum
    else:
        return "entered values are not equal"


x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the third number:"))
print(sum(x,y,z))
