dict={1:10,2:20,3:30}
print("key value count")
for count,(key,value)in enumerate(dict.items(),1):
   print(key,'',value,'',count)
