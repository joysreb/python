def permute(nums):
     result_perms=[[]]
     for n in numbers:
        new_perms=[]
        for perm in result_perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i]+[n]+perm[i:])
                result_perms=new_perms
     return result_perms           




numbers=[1,2,3]
print(permute(numbers))
