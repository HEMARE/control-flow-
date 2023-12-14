fruits=["apple","bannana","cherry"]
fruits1=["grape","apple","apple"]
for x in fruits:
    if x=="bannana":
        continue
print(x)
for x in "bannana":
   print(x) 
for i in range(6):
    print(i) 
for x in range(2,8):
    print(x)
for h in range(2,15,5):
    print(h)  
else:
    print("finally finished")  
for a in fruits:
    for y in fruits1:
        print(y,a)    
for b in []:
    pass
for c in fruits1:
    print(fruits1)
d=dict()
d['xyz']=123
d['abc']=456
for e in d:
    print("%s %d" %(e,d[e]))
for index in range(len(fruits)):
    print(fruits[index])
else:
    print("innsiide the else block")
for fruits in 'apple':
    if fruits=='p'or fruits=='e':
        break
    print(fruits)

 


 