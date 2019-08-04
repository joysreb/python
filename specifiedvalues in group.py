def value_present(n):
  group=[1,2,3,4,5]   
  if n in group:
        print("the number is present in the group")
  else:
        print("the number is outside the group")
    

n=int(input("enter the number:"))
print(value_present(n))

