dic1={0:1,1:0}
dic2={2:3,3:2}
dic3={3:4,4:3}
dic4={}
for d in (dic1,dic2,dic3):
   dic4.update(d)
print(dic4)
